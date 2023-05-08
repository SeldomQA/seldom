"""
unittest decorator
"""
import unittest
import functools

__all__ = [
    "skip", "skip_if", "skip_unless", "expected_failure", "depend", "if_depend", "label", "rerun"
]


def skip(reason=None):
    """
    Unconditionally skip a test.
    :param reason:
    :return:
    """
    if reason is None:
        reason = "Skip the use case."
    return unittest.skip(reason)


def skip_if(condition, reason):
    """
    Skip a test if the condition is true.
    :param condition:
    :param reason:
    :return:
    """
    return unittest.skipIf(condition, reason)


def skip_unless(condition, reason):
    """
    Skip a test unless the condition is true.
    :param condition:
    :param reason:
    :return:
    """
    return unittest.skipUnless(condition, reason)


def expected_failure(test_item):
    """
    Expect the test case to failure
    :param test_item:
    :return:
    """
    return unittest.expectedFailure(test_item)


def depend(case=None):
    """
    Use case dependency
    :param case
    :return:
    """
    def wrapper_func(test_func):

        @functools.wraps(test_func)
        def inner_func(self, *args):
            if case == test_func.__name__:
                raise ValueError(f"{case} cannot depend on itself")
            failures = str([fail_[0] for fail_ in self._outcome.result.failures])
            errors = str([error_[0] for error_ in self._outcome.result.errors])
            skipped = str([skip_[0] for skip_ in self._outcome.result.skipped])
            flag = (case in failures) or (case in errors) or (case in skipped)
            test = skip_if(flag, f'{case} failed  or  error or skipped')(test_func)
            try:
                return test(self)
            except TypeError:
                return None
        return inner_func
    return wrapper_func


def if_depend(value):
    """
    Custom skip condition
    :param value
    :return:
    """
    def wrapper_func(function):
        def inner_func(self, *args, **kwargs):
            if not getattr(self, value):
                self.skipTest('Dependent use case not passed')
            else:
                function(self, *args, **kwargs)
        return inner_func
    return wrapper_func


def label(*labels):
    """
    Test case classification label

    Usage:
        @label('quick')
        class MyTest(unittest.TestCase):
            def test_foo(self):
                pass
    """

    def inner(cls):
        # append labels to class
        cls._labels = set(labels) | getattr(cls, '_labels', set())
        return cls

    return inner


def rerun(times: int = 2):
    """
    Repeat a function multiple times.
    Note: The change method cannot count the number of test cases.

    :param times: Number of runs, default 2
    return
    """
    def wrapper(func):

        @functools.wraps(func)
        def decorator(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

        return decorator

    return wrapper
