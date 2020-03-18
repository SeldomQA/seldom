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
