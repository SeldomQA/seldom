from functools import wraps
from seldom.logging import log


def log_assertions(func):
    """
    Decorator: Adds logging capabilities to assertion methods
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wrapper
        :param args:
        :param kwargs:
        :return:
        """
        args_to_log = []
        if args:
            args_to_log = args[1:]

        log.info(f"👀 {func.__name__}  -> {args_to_log}")
        result = func(*args, **kwargs)
        return result

    return wrapper
