import io
import sys
import json
import logging


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
    with io.open(file_path, "r+", encoding="utf-8-sig") as f:
        try:
            content_json = json.loads(f.read())
            return content_json["log"]["entries"]
        except (KeyError, TypeError):
            logging.error("HAR file content error: {}".format(file_path))
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
