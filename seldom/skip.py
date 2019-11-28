import unittest


def skip(reason=None):
    if reason is None:
        reason = "Skip the use case."
    return unittest.skip(reason)
