import warnings
from functools import wraps
from parameterized.parameterized import inspect
from parameterized.parameterized import parameterized
from parameterized.parameterized import default_doc_func
from parameterized.parameterized import default_name_func
from parameterized.parameterized import skip_on_empty_helper
from parameterized.parameterized import reapply_patches_if_need
from parameterized.parameterized import delete_patches_if_need
from parameterized import parameterized_class
from seldom.testdata import conversion
from seldom.logging.exceptions import FileTypeError


def file_data(file, line=1, sheet="Sheet1", key=None):
    """
    Support file parameterization.

    d.json
    ```json
    {
     "login":  [
        ["admin", "admin123"],
        ["guest", "guest123"]
     ]
    }
    ```
    >>  @file_data(file="./d.json", key="login")
    ... def test_case(self, username, password):
    ...     print(username)
    ...     print(password)
    """
    suffix = file.split(".")[-1]
    if suffix == "csv":
        data_list = conversion.csv_to_list(file, line=line)
    elif suffix == "xlsx":
        data_list = conversion.excel_to_list(file, sheet=sheet, line=line)
    elif suffix == "json":
        data_list = conversion.json_to_list(file, key=key)
    elif suffix == "yaml":
        data_list = conversion.yaml_to_list(file, key=key)
    else:
        raise FileTypeError("Your file is not supported: {}".format(file))

    return data(data_list)


def data(input, name_func=None, doc_func=None, skip_on_empty=False, **legacy):
    """ A "brute force" method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.

        >> @data([("foo", 1, 2)])
        ... def test_add1(name, input, expected):
        ...     actual = add1(input)
        ...     assert_equal(actual, expected)
        ...
        >>
        """

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
        stack = inspect.stack()
        frame = stack[1]
        frame_locals = frame[0].f_locals

        paramters = parameterized.input_as_callable(input)()

        if not paramters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(lambda: skip_on_empty_helper())

        digits = len(str(len(paramters) - 1))
        for num, p in enumerate(paramters):
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


def data_class(attrs, input_values):
    """
    Parameterizes a test class by setting attributes on the class.
    """
    return parameterized_class(attrs, input_values)
