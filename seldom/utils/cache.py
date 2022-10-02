"""
seldom cache
"""
import os
import json
from seldom.logging import log
from seldom.utils import file

DATA_PATH = os.path.join(file.dir, "cache_data.json")


class Cache:
    """
    Cache through JSON files
    """

    def __init__(self):
        is_exist = os.path.isfile(DATA_PATH)
        if is_exist is False:
            with open(DATA_PATH, "w", encoding="utf-8") as json_file:
                json.dump({}, json_file)

    @staticmethod
    def clear(name: str = None) -> None:
        """
        Clearing cached
        :param name: key
        """
        if name is None:
            with open(DATA_PATH, "w", encoding="utf-8") as json_file:
                log.info("Clear all cache data")
                json.dump({}, json_file)
        else:
            with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
                save_data = json.load(json_file)
                del save_data[name]
                log.info(f"Clear cache data: {name}")

            with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
                json.dump(save_data, json_file)

    @staticmethod
    def set(data: dict) -> None:
        """
        Setting cached
        :param data:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            save_data = json.load(json_file)
            for key, value in data.items():
                data = save_data.get(key, None)
                if data is None:
                    log.info(f"Set cache data: {key} = {value}")
                else:
                    log.info(f"update cache data: {key} = {value}")
                save_data[key] = value

        with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
            json.dump(save_data, json_file)

    @staticmethod
    def get(name=None):
        """
        Getting cached
        :param name: key
        :return:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            save_data = json.load(json_file)
            if name is None:
                return save_data

            value = save_data.get(name, None)
            if value is not None:
                log.info(f"Get cache data: {name} = {value}")
            return value


cache = Cache()
