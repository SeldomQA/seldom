import sys
import seldom
from seldom.logging import log
from seldom import data


class TestCase(seldom.TestCase):
    def test_case(self):
        """ sample case """
        sys.stderr.write("4. 最原始的打印，进入了test_case1了\n")
        print("5. print msg")
        log.debug("6. log msg")

    def test_case2(self):
        """ sample case """
        log.warning("7. 进入了test_ddt")

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_ddt(self, _, keyword):
        """ ddt case """
        print("this is print msg")
        log.debug(f"test data: {keyword}")


if __name__ == '__main__':
    print("1. 逻辑顺序测试开始！🚀")
    print("2. print()的内容不会被吃掉")
    log.debug("3. logger的内容不会被吃掉,但是没有进入seldom.main()，所以不会出现在报告中")

    seldom.main()

    print("8. seldom.main()后正常释放了print()")
