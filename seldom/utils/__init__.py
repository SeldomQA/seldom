import os
import inspect


def file_dir() -> str:
    """
    Returns the absolute path to the directory where the current file resides
    """
    stack_t = inspect.stack()
    ins = inspect.getframeinfo(stack_t[1][0])
    return os.path.dirname(os.path.abspath(ins.filename))


class AssertInfo:
    data = []


def diff_json(response_data, assert_data):
    """
    Compare the JSON data format
    """
    if isinstance(response_data, dict):
        """ dict format """
        for key in assert_data:
            if key not in response_data:
                info = "❌ Response data has no key: {}".format(key)
                print(info)
                AssertInfo.data.append(info)
        for key in response_data:
            if key in assert_data:
                """ recursion """
                diff_json(response_data[key], assert_data[key])
            else:
                info = "💡 Assert data has not key: {}".format(key)
                print(info)
    elif isinstance(response_data, list):
        """ list format """
        if len(response_data) != len(assert_data):
            print("list len: '{}' != '{}'".format(len(response_data), len(assert_data)))
        for src_list, dst_list in zip(sorted(response_data), sorted(assert_data)):
            """ recursion """
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            info = "❌ Value are not equal: {}".format(response_data)
            print(info)
            AssertInfo.data.append(info)


