"""
seldom cache
"""
import os
import sys
import json
from seldom.logging import log
from seldom.utils import file

WINDOWS = True
if sys.platform != "win32":
    WINDOWS = False
    import fcntl

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
            with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_EX)
                json.dump({}, json_file)
                log.info("Clear all cache data")
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_UN)
        else:
            with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_EX)
                save_data = json.load(json_file)
                del save_data[name]
                json.dump(save_data, json_file)
                log.info(f"Clear cache data: {name}")
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_UN)

            with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_EX)
                json.dump(save_data, json_file)
                if WINDOWS is False:
                    fcntl.flock(json_file, fcntl.LOCK_UN)

    @staticmethod
    def set(data: dict) -> None:
        """
        Setting cached
        :param data:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_EX)
            save_data = json.load(json_file)
            for key, value in data.items():
                data = save_data.get(key, None)
                if data is None:
                    log.info(f"Set cache data: {key} = {value}")
                else:
                    log.info(f"update cache data: {key} = {value}")
                save_data[key] = value

            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_UN)

        with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_EX)
            json.dump(save_data, json_file)
            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_UN)

    @staticmethod
    def get(name=None):
        """
        Getting cached
        :param name: key
        :return:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_EX)
            save_data = json.load(json_file)
            if name is None:
                return save_data

            value = save_data.get(name, None)
            if value is not None:
                log.info(f"Get cache data: {name} = {value}")

            if WINDOWS is False:
                fcntl.flock(json_file, fcntl.LOCK_UN)
            return value


cache = Cache()
