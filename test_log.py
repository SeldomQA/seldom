import sys
import seldom
from seldom.logging import log

print("Header: 在__name__=='__main__'外面的打印现状")


class TestCase(seldom.TestCase):
    def test_case(self):
        """ sample case """
        sys.stderr.write("4. 最原始的打印，进入了test_case1了\n")
        print("5. 在seldom框架中print()会被吃掉")
        log.logger.debug("6. 但是在seldom框架中logger内容不会被吃掉")
        print("7. name：")

    def test_ddt(self):
        """ ddt case """
        log.logger.warning("8. 进入了test_ddt")
        pass


if __name__ == '__main__':
    print("1. 逻辑顺序测试开始！🚀")
    print("2. print()的内容不会被吃掉")
    log.logger.debug("3. logger的内容不会被吃掉,但是没有进入seldom.main()，所以不会出现在报告中")

    seldom.main()

    print("9. seldom.main()后正常释放了print()")

print("Footer: 在__name__=='__main__'外面的打印现状")
