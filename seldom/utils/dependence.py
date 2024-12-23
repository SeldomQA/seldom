from typing import Callable, Text, Tuple
from functools import wraps
from seldom.utils import cache
from seldom.logging import log


def dependent_func(func_obj: Callable, key_name: Text = None, *out_args, **out_kwargs):
    """
    Dependent function decorator.

    :param func_obj: function object.
    :param key_name:
    :param out_args:
    :param out_kwargs:
    :return:
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if isinstance(func_obj, staticmethod):
                depend_func_name = func_obj.__func__.__name__
            else:
                depend_func_name = func_obj.__name__

            key = key_name
            if key_name is None:
                key = depend_func_name

            if not cache.get(key):
                dependence_res = _call_dependence(func_obj, func_name, *out_args, **out_kwargs)
                cache.set({key: dependence_res})

            else:
                log.info(f"🔗 <{depend_func_name}> a has been executed, obtain it in cache through `{key}`.")
            r = func(*args, **kwargs)
            return r

        return wrapper

    return decorator


def _call_dependence(dependent_api: Callable or Text, func_name: Text, *args, **kwargs) -> Tuple:
    """
    Execution dependent method.
    :param dependent_api:
    :param func_name:
    :param args:
    :param kwargs:
    :return:
    """
    if isinstance(dependent_api, staticmethod):
        dependent_api = dependent_api.__func__

    depend_func_name = dependent_api.__name__
    log.info(f"🔗 <{func_name}> depends on <{depend_func_name}>, execute.")
    res = dependent_api(*args, **kwargs)
    return res
