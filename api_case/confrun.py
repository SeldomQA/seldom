"""
seldom confrun.py hooks function
"""


def base_url():
    """
    http test
    api base url
    """
    return "http://www.httpbin.org"


def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html" or "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "seldom 执行 excel 接口用例"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "api"]


def language():
    """
    setting report language
    return "en" or "zh-CN"
    """
    return "en"


def failfast():
    """
    fail fast
    :return:
    """
    return False
