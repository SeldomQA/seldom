import unittest


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


def depend(value):
    """
    Use case dependency
    :param value:
    :return:
    """
    def deco(function):
        def wrapper(self, *args, **kwargs):
            if not getattr(self, value):
                self.skipTest('Dependent use case not passed')
            else:
                function(self, *args, **kwargs)
        return wrapper
    return deco
