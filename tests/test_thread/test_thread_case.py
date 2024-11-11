import time
import seldom
from seldom.extend_lib import threads


class MyTest(seldom.TestCase):

    def test_baidu(self):
        self.open("https://www.baidu.com")
        self.sleep(3)

    def test_bing(self):
        self.open("https://www.bing.com")
        self.sleep(4)


if __name__ == "__main__":

    @threads(2)  # !!!核心!!!! 设置线程数
    def run_case(case: str):
        """
        根据传入的case执行用例
        """
        seldom.main(case=case, browser="gc", debug=True)


    # 将两条用例拆分，分别用不同的浏览器执行
    cases = [
        "test_thread_case.MyTest.test_baidu",
        "test_thread_case.MyTest.test_bing"
    ]

    for c in cases:
        run_case(c)
        time.sleep(1)
