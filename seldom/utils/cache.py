"""
seldom cache
"""
import os
import sys
import json
import uuid
import pickle
import shutil
import tempfile
from seldom.logging import log
from functools import lru_cache
from functools import wraps as func_wraps


WINDOWS = True
if sys.platform != "win32":
    WINDOWS = False
    import fcntl

DATA_PATH = os.path.join(tempfile.gettempdir(), "cache_data.json")


class Cache:
    """
    Disk Cache through JSON files
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
                    fcntl.flock(json_file.fileno(), fcntl.LOCK_EX)
                json.dump({}, json_file)
                log.info("Clear all cache data")
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
                    fcntl.flock(json_file.fileno(), fcntl.LOCK_EX)
                json.dump(save_data, json_file)

    @staticmethod
    def set(data: dict) -> None:
        """
        Setting cached
        :param data:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file.fileno(), fcntl.LOCK_EX)
            save_data = json.load(json_file)
            for key, value in data.items():
                data = save_data.get(key, None)
                if data is None:
                    log.info(f"Set cache data: {key} = {value}")
                else:
                    log.info(f"update cache data: {key} = {value}")
                save_data[key] = value

        with open(DATA_PATH, "w+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file.fileno(), fcntl.LOCK_EX)
            json.dump(save_data, json_file)

    @staticmethod
    def get(name=None):
        """
        Getting cached
        :param name: key
        :return:
        """
        with open(DATA_PATH, "r+", encoding="utf-8") as json_file:
            if WINDOWS is False:
                fcntl.flock(json_file.fileno(), fcntl.LOCK_EX)
            save_data = json.load(json_file)
            if name is None:
                return save_data

            value = save_data.get(name, None)
            if value is not None:
                log.info(f"Get cache data: {name} = {value}")

            return value


cache = Cache()


def memory_cache(maxsize=None, typed=False):
    """ memory (Least-recently-used) cache decorator
    """
    return lru_cache(maxsize=maxsize, typed=typed)


class DiskCache:
    """
    Cache data to disk decorator
    """

    _NAMESPACE = uuid.UUID("c875fb30-a8a8-402d-a796-225a6b065cad")

    def __init__(self, cache_path=None):
        if cache_path:
            self.cache_path = os.path.abspath(cache_path)
        else:
            self.cache_path = os.path.join(tempfile.gettempdir(), ".diskcache")

    def __call__(self, func):
        """
        Returns a wrapped function.
        If there is no cache on disk, the function is called to get the result, cached and returned
        If there is a cache on the disk, the cached result is returned directly
        :param func:
        """
        @func_wraps(func)
        def wrapper(*args, **kw):
            params_uuid = uuid.uuid5(self._NAMESPACE, "-".join(map(str, (args, kw))))
            key = '{}-{}.cache'.format(func.__name__, str(params_uuid))
            cache_file = os.path.join(self.cache_path, key)

            if not os.path.exists(self.cache_path):
                os.makedirs(self.cache_path)

            try:
                with open(cache_file, 'rb') as f:
                    val = pickle.load(f)
            except Exception:
                val = func(*args, **kw)
                try:
                    with open(cache_file, 'wb') as f:
                        pickle.dump(val, f)
                except Exception:
                    pass
            return val
        return wrapper

    def clear(self, func_name: str = None) -> None:
        """
        clear function cache
        :param func_name:
        :return:
        """
        if func_name is None:
            log.info("Clear all function cache")
            if os.path.exists(self.cache_path):
                shutil.rmtree(self.cache_path)
        else:
            log.info(f"Clear function cache: {func_name}")
            for cache_file in os.listdir(self.cache_path):
                if cache_file.startswith(func_name + "-"):
                    os.remove(os.path.join(self.cache_path, cache_file))


disk_cache = DiskCache
