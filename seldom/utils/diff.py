"""
diff file
"""
from typing import Any
from seldom.logging import log


class AssertInfo:
    """
    Save assert warning/error info.
    """
    warning = []
    error = []


def _all_values_are_same(input_list) -> bool:
    """
    Check whether all values in the list are the same amount
    """
    return input_list.count(input_list[0]) == len(input_list)


def _list_sorted(data):
    """
    list sorted
    """
    if isinstance(data[0], dict):
        if len(data[0]) == 0:
            log.info("data is [{}]")
        try:
            # Judgment sort item
            number = 0
            for i in range(len(data[0].keys())):
                all_value = []
                for d in data:
                    v = list(d.values())[i]
                    all_value.append(v)
                if _all_values_are_same(all_value) is False:
                    number = i
                    break
            data = sorted(data, key=lambda x: x[list(data[0].keys())[number]])
        except (TypeError, AttributeError, IndexError, KeyError):
            data = data
    else:
        data = sorted(data)
    return data


def diff_json(response_data: Any, assert_data: Any, exclude: list = None) -> None:
    """
    Compare the JSON data format
    """
    if exclude is None:
        exclude = []

    if isinstance(response_data, dict) and isinstance(assert_data, dict):
        # dict format
        for key in assert_data:
            # skip check
            if key in exclude:
                continue
            if key not in response_data:
                AssertInfo.error.append(f"❌ Response data has no key: {key}")
        for key in response_data:
            # skip check
            if key in exclude:
                continue
            if key in assert_data:
                # recursion
                diff_json(response_data[key], assert_data[key], exclude)
            else:
                AssertInfo.warning.append(f"💡 Assert data has not key: {key}")
    elif isinstance(response_data, list) and isinstance(assert_data, list):
        # list format
        if len(response_data) == 0:
            log.info("response is []")
        else:
            response_data = _list_sorted(response_data)

        if len(response_data) != len(assert_data):
            log.info(f"list len: '{len(response_data)}' != '{len(assert_data)}'")

        if len(assert_data) > 0:
            assert_data = _list_sorted(assert_data)

        for src_list, dst_list in zip(response_data, assert_data):
            # recursion
            diff_json(src_list, dst_list, exclude)
    else:
        # different format
        if str(response_data) != str(assert_data):
            AssertInfo.error.append(f"❌ Value are not equal: {assert_data} != {response_data}")
