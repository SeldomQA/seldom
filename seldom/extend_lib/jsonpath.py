"""
An XPath for JSON
help: https://goessner.net/articles/JsonPath/
GitHub: https://gist.github.com/drewr/783585
"""
from __future__ import annotations

import re
import sys
from typing import Any, List, Union, Dict, Callable
from seldom.logging import log

__all__ = ['jsonpath']


def normalize(x: str) -> str:
    """normalize the path expression; outside jsonpath to allow testing"""
    subx: List[str] = []

    def f1(m: re.Match) -> str:
        n = len(subx)
        g1 = m.group(1)
        subx.append(g1)
        return f"[#{n}]"

    x = re.sub(r"[\['](\??\(.*?\))[\]']", f1, x)
    x = re.sub(r"'?(?<!@)\.'?|\['?", ";", x)
    x = re.sub(r";;;|;;", ";..;", x)
    x = re.sub(r";$|'?\]|'$", "", x)

    def f2(m: re.Match) -> str:
        return subx[int(m.group(1))]

    x = re.sub(r"#([0-9]+)", f2, x)
    return x


def jsonpath(
        obj: Union[Dict, List],
        expr: str,
        result_type: str = 'VALUE',
        debug: int = 0,
        use_eval: bool = True
) -> Union[List[Any], bool]:
    """
    traverse JSON object using jsonpath expr, returning values or paths
    """
    result: List[Any] = []

    def s(x: Union[str, int], y: str) -> str:
        """concatenate path elements"""
        return f"{x};{y}"

    def isint(x: str) -> bool:
        """check if argument represents a decimal integer"""
        return x.isdigit()

    def as_path(path: str) -> str:
        """convert internal path representation to
           "full bracket notation" for PATH output"""
        p = '$'
        for piece in path.split(';')[1:]:
            if isint(piece):
                p += f"[{piece}]"
            else:
                p += f"['{piece}']"
        return p

    def store(path: str, object: Any) -> str:
        if result_type == 'VALUE':
            result.append(object)
        elif result_type == 'IPATH':
            result.append(path.split(';')[1:])
        else:  # PATH
            result.append(as_path(path))
        return path

    def trace(expr: str, obj: Any, path: str) -> None:
        if debug:
            log.debug(f"trace {expr} / {path}")
        if expr:
            x = expr.split(';')
            loc = x[0]
            x = ';'.join(x[1:])
            if debug:
                log.debug(f"\t {loc} {type(obj)}")
            if loc == "*":
                def f03(key: str, loc: str, expr: str, obj: Any, path: str) -> None:
                    if debug > 1:
                        log.debug(f"\tf03 {key} {loc} {expr} {path}")
                    trace(s(key, expr), obj, path)

                walk(loc, x, obj, path, f03)
            elif loc == "..":
                trace(x, obj, path)

                def f04(key: str, loc: str, expr: str, obj: Any, path: str) -> None:
                    if debug > 1:
                        log.debug(f"\tf04 {key} {loc} {expr} {path}")
                    if isinstance(obj, dict):
                        if key in obj:
                            trace(s('..', expr), obj[key], s(path, key))
                    else:
                        if key < len(obj):
                            trace(s('..', expr), obj[key], s(path, key))

                walk(loc, x, obj, path, f04)
            elif loc == "!":
                # Perl jsonpath extension: return keys
                def f06(key: str, loc: str, expr: str, obj: Any, path: str) -> None:
                    if isinstance(obj, dict):
                        trace(expr, key, path)

                walk(loc, x, obj, path, f06)
            elif isinstance(obj, dict) and loc in obj:
                trace(x, obj[loc], s(path, loc))
            elif isinstance(obj, list) and isint(loc):
                iloc = int(loc)
                if debug:
                    log.debug(f"-----> {iloc} {len(obj)}")
                if len(obj) > iloc:
                    trace(x, obj[iloc], s(path, loc))
            else:
                # [(index_expression)]
                if loc.startswith("(") and loc.endswith(")"):
                    if debug > 1:
                        log.debug(f"index {loc}")
                    e = evalx(loc, obj)
                    trace(s(e, x), obj, path)
                    return

                # ?(filter_expression)
                if loc.startswith("?(") and loc.endswith(")"):
                    if debug > 1:
                        log.debug(f"filter {loc}")

                    def f05(key: str, loc: str, expr: str, obj: Any, path: str) -> None:
                        if debug > 1:
                            log.debug(f"f05 {key} {loc} {expr} {path}")
                        if isinstance(obj, dict):
                            eval_result = evalx(loc, obj[key])
                        else:
                            eval_result = evalx(loc, obj[int(key)])
                        if eval_result:
                            trace(s(key, expr), obj, path)

                    loc = loc[2:-1]
                    walk(loc, x, obj, path, f05)
                    return

                m = re.match(r'(-?[0-9]*):(-?[0-9]*):?(-?[0-9]*)$', loc)
                if m:
                    if isinstance(obj, (dict, list)):
                        def max(x: int, y: int) -> int:
                            if x > y:
                                return x
                            return y

                        def min(x: int, y: int) -> int:
                            if x < y:
                                return x
                            return y

                        objlen = len(obj)
                        s0 = m.group(1)
                        s1 = m.group(2)
                        s2 = m.group(3)

                        # XXX int("badstr") raises exception
                        start = int(s0) if s0 else 0
                        end = int(s1) if s1 else objlen
                        step = int(s2) if s2 else 1

                        if start < 0:
                            start = max(0, start + objlen)
                        else:
                            start = min(objlen, start)
                        if end < 0:
                            end = max(0, end + objlen)
                        else:
                            end = min(objlen, end)

                        for i in range(start, end, step):
                            trace(s(i, x), obj, path)
                    return

                # after (expr) & ?(expr)
                if loc.find(",") >= 0:
                    # [index,index....]
                    for piece in re.split(r"'?,'?", loc):
                        if debug > 1:
                            log.debug(f"piece {piece}")
                        trace(s(piece, x), obj, path)
        else:
            store(path, obj)

    def walk(loc: str, expr: str, obj: Any, path: str, funct: Callable) -> None:
        if isinstance(obj, list):
            for i in range(0, len(obj)):
                funct(i, loc, expr, obj, path)
        elif isinstance(obj, dict):
            for key in obj:
                funct(key, loc, expr, obj, path)

    def evalx(loc: str, obj: Any) -> Any:
        """eval expression"""

        if debug:
            log.debug(f"evalx {loc}")

        # a nod to JavaScript. doesn't work for @.name.name.length
        # Write len(@.name.name) instead!!!
        loc = loc.replace("@.length", "len(__obj)")

        loc = loc.replace("&&", " and ").replace("||", " or ")

        # replace !@.name with 'name' not in obj
        # XXX handle !@.name.name.name....
        def notvar(m: re.Match) -> str:
            return f"'{m.group(1)}' not in __obj"

        loc = re.sub(r"!@\.([a-zA-Z@_0-9-]*)", notvar, loc)

        # replace @.name.... with __obj['name']....
        # handle @.name[.name...].length
        def varmatch(m: re.Match) -> str:
            def brackets(elts: List[str]) -> str:
                ret = "__obj"
                for e in elts:
                    if isint(e):
                        ret += f"[{e}]"
                    else:
                        ret += f"['{e}']"
                return ret

            g1 = m.group(1)
            elts = g1.split('.')
            if elts[-1] == "length":
                return f"len({brackets(elts[1:-1])})"
            return brackets(elts[1:])

        loc = re.sub(r'(?<!\\)(@\.[a-zA-Z@_.0-9]+)', varmatch, loc)

        # removed = -> == translation
        # causes problems if a string contains =

        # replace @  w/ "__obj", but \@ means a literal @
        loc = re.sub(r'(?<!\\)@', "__obj", loc).replace(r'\@', '@')
        if not use_eval:
            if debug:
                log.debug("eval disabled")
            raise Exception("eval disabled")
        if debug:
            log.debug(f"eval {loc}")
        try:
            # eval w/ caller globals, w/ local "__obj"!
            v = eval(loc, caller_globals, {'__obj': obj})
        except Exception as e:
            if debug:
                log.debug(repr(e))
            return False

        if debug:
            log.debug(f"-> {v}")
        return v

    # body of jsonpath()
    caller_globals = sys._getframe(1).f_globals

    if not (expr and obj):
        return False

    cleaned_expr = normalize(expr)
    if cleaned_expr.startswith("$;"):
        cleaned_expr = cleaned_expr[2:]

    trace(cleaned_expr, obj, '$')

    return result if result else False


if __name__ == '__main__':
    try:
        import json
    except ImportError:
        import simplejson as json

    if len(sys.argv) not in (3, 4):
        sys.stdout.write("Usage: jsonpath.py FILE PATH [OUTPUT_TYPE]\n")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            object = json.load(f)
    except Exception as e:
        log.error(f"Error loading JSON file: {e}")
        sys.exit(1)

    path = sys.argv[2]
    format = sys.argv[3] if len(sys.argv) > 3 else 'VALUE'

    value = jsonpath(object, path, format, debug=2)

    if not value:
        sys.exit(1)

    with sys.stdout as f:
        json.dump(value, f, sort_keys=True, indent=1)
        f.write("\n")

    sys.exit(0)
