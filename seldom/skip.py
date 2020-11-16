import unittest
import functools


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


def depend(case=None):
    """
    Use case dependency
    :param case
    :return:
    """
    def wrapper_func(test_func):
        @functools.wraps(test_func)
        def inner_func(self):
            if case == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(case))
            failures = str([fail_[0] for fail_ in self._outcome.result.failures])
            errors = str([error_[0] for error_ in self._outcome.result.errors])
            skipped = str([skip_[0] for skip_ in self._outcome.result.skipped])
            flag = (case in failures) or (case in errors) or (case in skipped)
            test = skip_if(flag, '{} failed  or  error or skipped'.format(case))(test_func)
            return test(self)
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
