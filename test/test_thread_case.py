import seldom
from seldom.utils import threads


class MyTest(seldom.TestCase):

    def test_baidu(self):
        self.open("https://www.baidu.com")
        self.sleep(3)

    def test_bing(self):
        self.open("https://www.bing.com")
        self.sleep(4)


@threads(2)  # !!!核心!!!! 设置线程数
def run_case(case: str, browser: str):
    """
    根据传入的case执行用例
    """
    seldom.main(case=case, browser=browser, debug=True)


if __name__ == "__main__":
    # 将两条用例拆分，分别用不同的浏览器执行
    cases = {
        "test_thread_case.MyTest.test_baidu": "chrome",
        "test_thread_case.MyTest.test_bing": "edge"
    }

    for key, value in cases.items():
        run_case(key, value)
