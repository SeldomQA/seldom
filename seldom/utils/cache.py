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
            with open(DATA_PATH, "w") as f:
                json.dump({}, f)

    @staticmethod
    def clear(name=None) -> None:
        """
        Clearing cached
        :param name: key
        """
        if name is None:
            with open(DATA_PATH, "w") as f:
                log.info("Clear all cache data")
                json.dump({}, f)
        else:
            with open(DATA_PATH, "r+") as f:
                save_data = json.load(f)
                del save_data[name]
                log.info(f"Set cache data: {name}")

            with open(DATA_PATH, "w+") as f:
                json.dump(save_data, f)

    @staticmethod
    def set(data: dict) -> None:
        """
        Setting cached
        :param data:
        """
        with open(DATA_PATH, "r+") as f:
            save_data = json.load(f)
            for key, value in data.items():
                log.info(f"Delete cache data: {key} = {value}")
                save_data[key] = value

        with open(DATA_PATH, "w+") as f:
            json.dump(save_data, f)

    @staticmethod
    def get(name=None):
        """
        Getting cached
        :param name: key
        :return:
        """
        with open(DATA_PATH, "r+") as f:
            save_data = json.load(f)
            if name is None:
                return save_data
            else:
                value = save_data.get(name, None)
                if value is not None:
                    log.info(f"Get cache data: {name} = {value}")
                return value


cache = Cache()


if __name__ == '__main__':
    cache.clear("token")
    cache.clear()
    token = cache.get("token")
    print(f"token: {token}")
    if token is None:
        cache.set({"token": "123"})
    token = cache.get("token")
    print(f"token: {token}")
    all_token = cache.get()
    print(f"all: {all_token}")
