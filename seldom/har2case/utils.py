"""
har to case utils
"""
import io
import sys
import json
from seldom.logging import log


def load_har_log_entries(file_path):
    """ load HAR file and return log entries list

    Args:
        file_path (str)

    Returns:
        list: entries
            [
                {
                    "request": {},
                    "response": {}
                },
                {
                    "request": {},
                    "response": {}
                }
            ]

    """
    with io.open(file_path, "r+", encoding="utf-8-sig") as file:
        try:
            content_json = json.loads(file.read())
            return content_json["log"]["entries"]
        except (KeyError, TypeError):
            log.error(f"HAR file content error: {file_path}")
            sys.exit(1)


def list_to_dict_str(data: list) -> str:
    """
    list -> dict -> string
    """
    data_dict = {}
    for param in data:
        data_dict[param["name"]] = param["value"]

    if len(data_dict) == 0:
        data_dict_str = "{}"
    else:
        data_dict_str = json.dumps(data_dict)
    return data_dict_str
