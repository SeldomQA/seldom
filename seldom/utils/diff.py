"""
diff file
"""
from typing import Any
from seldom.logging import log


class AssertInfo:
    data = []


def diff_json(response_data: Any, assert_data: Any) -> None:
    """
    Compare the JSON data format
    """
    if isinstance(response_data, dict) and isinstance(assert_data, dict):
        # dict format
        for key in assert_data:
            if key not in response_data:
                info = f"❌ Response data has no key: {key}"
                log.info(info)
                AssertInfo.data.append(info)
        for key in response_data:
            if key in assert_data:
                # recursion
                diff_json(response_data[key], assert_data[key])
            else:
                info = f"💡 Assert data has not key: {key}"
                log.info(info)
    elif isinstance(response_data, list) and isinstance(assert_data, list):
        # list format
        if len(response_data) == 0:
            log.info("response is []")
        else:
            if isinstance(response_data[0], dict):
                response_data = sorted(response_data, key=lambda x: x[list(response_data[0].keys())[0]])
            else:
                response_data = sorted(response_data)

        if len(response_data) != len(assert_data):
            log.info(f"list len: '{len(response_data)}' != '{len(assert_data)}'")

        if len(assert_data) > 0:
            if isinstance(assert_data[0], dict):
                assert_data = sorted(assert_data, key=lambda x: x[list(assert_data[0].keys())[0]])
            else:
                assert_data = sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            # recursion
            diff_json(src_list, dst_list)
    else:
        if str(response_data) != str(assert_data):
            info = f"❌ Value are not equal: {response_data}"
            log.info(info)
            AssertInfo.data.append(info)
