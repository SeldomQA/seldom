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
def run_case(case, browser):
    """
    根据传入的case执行用例
    """
    if browser == "chrome":
        aa = {
            "browser": "chrome",  # 指定浏览器 chrome
            "executable_path": "/Users/zhiheng.hu/klpro/webdriver/chromedriver",  # 指定浏览器驱动
        }
        seldom.main(case=case, browser=aa, debug=True)

    if browser == "edge":
        bb = {
            "browser": "edge",  # 指定浏览器 edge
            "executable_path": "/Users/zhiheng.hu/klpro/webdriver/msedgedriver",  # 指定浏览器驱动
        }
        seldom.main(case=case, browser=bb, debug=True)


if __name__ == "__main__":
    # 定义三个目录，分别丢给2个线程，当然取决于 @threads(s) 的数量。
    cases = {
        "test_thread_case.MyTest.test_baidu": "chrome",
        "test_thread_case.MyTest.test_bing": "edge"
    }

    for case, browser in cases.items():
        print("case", case, browser)
        run_case(case, browser)
