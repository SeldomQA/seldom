from logzero import logger


def assert_equal(printer, a, b, ):
    """封装相等"""
    printer(f"assert_equal a: {a}")
    printer(f"assert_equal b: {b}")
    try:
        assert a == b
    except AssertionError:
        assert a == b


def test_case1(printer):
    """测试用例1"""
    assert_equal(printer, 1, 1)


def test_case2(printer):
    """测试用例2"""
    assert_equal(printer, 1, 2)
