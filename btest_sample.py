# test_sample.py
import seldom
from seldom import data, Seldom
from poium import Page, Element


# class BaiduPage(Page):
#     search = Element(id_="kw")


class TestCase(seldom.TestCase):

    def test_case(self):
        """
        sample case
        """
        self.open("https://www.baidu.com")
        self.assertNotElement(id_="abcd")
        # self.type(id_="kw", text="seldom")
        # self.click(id_="su")
        # browser = self.new_browser()
        # browser.get("https://www.baidu.com")
        # self.sleep(5)
        # page = BaiduPage(Seldom.driver)
        # page.open("https://www.baidu.com")
        # page.search.send_keys("seldom")
        # page.search.submit()

    # @data([
    #     ("case1", "seldom"),
    #     ("case2", "XTestRunner"),
    # ])
    # def test_ddt(self, name, search):
    #     """
    #     参数化用例
    #     """
    #     print(f"name: {name}, search_key: {search}")
    #

if __name__ == '__main__':
    # seldom.main(case="btest_sample")  # 指定当前文件
    # seldom.main(case="btest_sample.TestCase")  # 指定测试类

    # from seldom.running.config import Log

    # print("def", Log.colorLog)
    seldom.main(browser="gc", case="btest_sample.TestCase.test_case", debug=False)  # 指定测试用例

    # 使用参数化的用例
    # seldom.main(case="btest_sample.TestCase.test_ddt")  # 错误用法
    # seldom.main(case="btest_sample.TestCase.test_ddt_0_case1")  # 正确用例






