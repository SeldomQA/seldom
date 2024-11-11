import sys
import seldom
from seldom.logging import log
from seldom import data


class TestCase(seldom.TestCase):
    def test_case(self):
        """ sample case """
        sys.stderr.write("3. 进入了test_case1了\n")
        print("4. print msg")
        log.debug("5. log msg")

    def test_case2(self):
        """ sample case """
        log.warning("6. log warning msg")

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_ddt(self, _, keyword):
        """ ddt case """
        print("7. this is print msg")
        log.debug(f"test data: {keyword}")

    def test_failed(self):
        """ ddt case """
        assert 0

    def test_error(self):
        """ ddt case """
        raise IOError("ddd")


if __name__ == '__main__':
    print("1. 逻辑顺序测试开始！🚀")
    log.debug("2. logger的内容不会被吃掉,但是没有进入seldom.main()，所以不会出现在报告中")

    # seldom.main()
    seldom.main(report="report.xml")
