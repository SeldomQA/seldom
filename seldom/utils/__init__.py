import os
import inspect


class FindFilePath:

    def __new__(cls, name) -> str:
        if name is None:
            raise NameError("Please specify filename")
        stack_t = inspect.stack()
        ins = inspect.getframeinfo(stack_t[1][0])
        cls.file_dir = os.path.dirname(os.path.dirname(os.path.abspath(ins.filename)))

        file_path = None
        for root, dirs, files in os.walk(cls.file_dir, topdown=False):
            for file in files:
                if file == name:
                    file_path = os.path.join(root, file)
                    break
            else:
                continue
            break
        return file_path


find_file_path = FindFilePath


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
        if len(response_data) == 0:
            print("response is []")
        if len(response_data) != len(assert_data):
            print("list len: '{}' != '{}'".format(len(response_data), len(assert_data)))

        if isinstance(response_data[0], dict):
            response_data = sorted(response_data, key=lambda x: x[list(response_data[0].keys())[0]])
        else:
            response_data = sorted(response_data)
        if isinstance(assert_data[0], dict):
            assert_data = sorted(assert_data, key=lambda x: x[list(assert_data[0].keys())[0]])
        else:
            assert_data = sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            """ recursion """
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            info = "❌ Value are not equal: {}".format(response_data)
            print(info)
            AssertInfo.data.append(info)


