"""
test data driver function
"""
import inspect as sys_inspect
import itertools
import os
import warnings
from functools import wraps
from pathlib import Path

import requests

from seldom.running.config import Seldom
from seldom.extend_lib import parameterized_class
from seldom.extend_lib.parameterized import delete_patches_if_need
from seldom.extend_lib.parameterized import inspect
from seldom.extend_lib.parameterized import parameterized
from seldom.extend_lib.parameterized import parameterized_argument_value_pairs
from seldom.extend_lib.parameterized import reapply_patches_if_need
from seldom.extend_lib.parameterized import short_repr
from seldom.extend_lib.parameterized import skip_on_empty_helper
from seldom.extend_lib.parameterized import to_text
from seldom.logging import log
from seldom.logging.exceptions import FileTypeError
from seldom.testdata import conversion
from seldom.utils import jmespath as utils_jmespath

__all__ = [
    "file_data", "api_data", "data", "data_class", "find_file"
]


def _search_file_path(file_name: str, file_dir: Path) -> str:
    """
    find file path
    :param file_name:
    :param file_dir:
    """
    file_path = ""
    find_root_dir = file_dir.parent.parent

    for root, _, files in os.walk(find_root_dir, topdown=False):
        for file in files:
            if Seldom.env is not None:
                if root.endswith(Seldom.env) and file == file_name:
                    file_path = os.path.join(root, file_name)
                    break
            else:
                if file == file_name:
                    file_path = os.path.join(root, file_name)
                    break
        else:
            continue
        break

    return file_path


def _search_env_file_path(file_dir: Path, file_part_path: str) -> str:
    """
    find environment file path, Seldom.env != None
    :param file_dir:
    :param file_part_path:
    """
    file_path = ""
    find_root_dir = file_dir.parent
    file_name = file_part_path.split("/")[-1]
    file_part = os.path.join(Seldom.env, file_part_path[:-len(file_name) - 1])

    for root, _, files in os.walk(find_root_dir, topdown=False):
        for file in files:
            if root.endswith(file_part) and file == file_name:
                file_path = os.path.join(root, file_name)
                break
        else:
            continue
        break

    return file_path


def find_file(file: str, file_dir: Path) -> str:
    """
    find file
    :param file:
    :param file_dir:
    """
    if os.path.isfile(file) is True:
        return file

    if "/" in file or "\\" in file:
        file = file.replace("\\", "/")

        if Seldom.env is not None:
            file_path = _search_env_file_path(file_dir=file_dir, file_part_path=file)
            return file_path
        else:
            # Starting at file_dir, search up the 5 levels of parent directories
            for _ in range(5):
                current_dir = os.path.join(file_dir, file)
                if os.path.isfile(current_dir):
                    return current_dir
                file_dir = file_dir.parent  # Move up to the parent directory
            else:
                return ""
    else:
        file_path = _search_file_path(file_dir=file_dir, file_name=file)
        return file_path


def file_data(file: str, line: int = 1, sheet: str = "Sheet1", key: str = None, end_line: int = None):
    """
    Support file parameterization.

    :param file: file name
    :param line: Start line number of an Excel/CSV file
    :param end_line:  End line number of an Excel/CSV file
    :param sheet: Excel sheet name
    :param key: Key name of an YAML/JSON file

    Usage:
    d.json
    ```json
    {
     "login":  [
        ["admin", "admin123"],
        ["guest", "guest123"]
     ]
    }
    ```
    >>  @file_data(file="d.json", key="login")
    ... def test_case(self, username, password):
    ...     print(username)
    ...     print(password)
    """
    if file is None:
        raise FileExistsError("File name does not exist.")

    stack_t = sys_inspect.stack()
    ins = sys_inspect.getframeinfo(stack_t[1][0])
    file_dir = Path(ins.filename).resolve().parent

    if Seldom.env is not None:
        log.info(f"env: '{Seldom.env}', find data file: '{file}'")
    else:
        log.info(f"find data file: {file}")

    file_path = find_file(file, file_dir)
    if file_path == "":
        if Seldom.env is not None:
            raise FileExistsError(f"No '{Seldom.env}/{file}' data file found.")
        raise FileExistsError(f"No '{file}' data file found.")

    suffix = file.split(".")[-1]
    if suffix == "csv":
        data_list = conversion.csv_to_list(file_path, line=line, end_line=end_line)
    elif suffix == "xlsx":
        data_list = conversion.excel_to_list(file_path, sheet=sheet, line=line, end_line=end_line)
    elif suffix == "json":
        data_list = conversion.json_to_list(file_path, key=key)
    elif suffix == "yaml":
        data_list = conversion.yaml_to_list(file_path, key=key)
    else:
        raise FileTypeError(f"Your file is not supported: {file}")

    return data(data_list)


def api_data(url: str = None, params: dict = None, headers: dict = None, ret: str = None):
    """
    Support api data parameterization.
    :param url:
    :param params:
    :param headers:
    :param ret:
    :return:
    """

    if url is None and Seldom.api_data_url is None:
        raise ValueError("url is not None")

    url = url if url is not None else Seldom.api_data_url
    resp = requests.get(url, params=params, headers=headers).json()

    if ret is not None:
        data_ = utils_jmespath(resp, ret)
        if data_ is None:
            raise ValueError(f"Error - return {ret} is None in {resp}")
        if isinstance(data_, list) is False:
            raise TypeError(f"Error - {data_} is not list")
        return data(data_)

    if isinstance(resp, list) is False:
        raise TypeError(f"Error - {resp} is not list")
    return data(resp)


def data(input, name_func=None, doc_func=None, skip_on_empty=False, cartesian=False, **legacy):
    """ A "brute force" method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.

        >> @data([("foo", 1, 2)])
        ... def test_add1(name, input, expected):
        ...     actual = add1(input)
        ...     assert_equal(actual, expected)
        ...
        >> locals()
        ... 'test_add1_foo_0': <function ...> ...
        >>
        """
    if cartesian is True:
        input = cartesian_product(input)

    input = conversion.check_data(input)

    if "testcase_func_name" in legacy:
        warnings.warn("testcase_func_name= is deprecated; use name_func=",
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy["testcase_func_name"]

    if "testcase_func_doc" in legacy:
        warnings.warn("testcase_func_doc= is deprecated; use doc_func=",
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy["testcase_func_doc"]

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = inspect.currentframe().f_back.f_locals

        parameters = parameterized.input_as_callable(input)()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False

    return parameterized_expand_wrapper


def data_class(attrs, input_values=None, class_name_func=None):
    """
    Parameterizes a test class by setting attributes on the class.
    """
    return parameterized_class(attrs, input_values=input_values, class_name_func=class_name_func)


def default_name_func(func, num, p):
    """
    return test function name
    """
    base_name = func.__name__
    name_suffix = f"_{num}"

    if len(p.args) > 0 and isinstance(p.args[0], str):
        # name_suffix += "_" + parameterized.to_safe_name(p.args[0])
        name_suffix += ""
    return base_name + name_suffix


def default_doc_func(func, num, p):
    """
    return test function doc
    """
    if func.__doc__ is None:
        return None

    all_args_with_values = parameterized_argument_value_pairs(func, p)
    first_args_with_values = [all_args_with_values[0]]

    # Assumes that the function passed is a bound method.
    descs = ["%s=%s" % (n, short_repr(v)) for n, v in first_args_with_values]

    # The documentation might be a multiline string, so split it
    # and just work with the first string, ignoring the period
    # at the end if there is one.
    first, nl, rest = func.__doc__.lstrip().partition("\n")
    suffix = ""
    if first.endswith("."):
        suffix = "."
        first = first[:-1]
    args = "%s[%s]" % (len(first) and " " or "", ", ".join(descs))
    return "".join(
        to_text(x)
        for x in [first.rstrip(), args, suffix, nl, rest]
    )


def cartesian_product(arr) -> list:
    """
    Cartesian product
    :param arr: Two-dimensional list
    return:
    """
    cp = list(itertools.product(*arr))
    return cp
