import time
from seldom.logging import log


def timer(func):
    """
    timer decorator
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        log.info(f"{func.__name__} executed in {end_time - start_time:.3f}s")
        return result
    return wrapper
