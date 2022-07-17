# from seldom.utils import get_file_path
#
# path = get_file_path(name="data.json")
# print(path)


# from selenium import webdriver
#
# dr = webdriver.Chrome()
# dr.get("https://www.baidu.com")
# elem = dr.find_element_by_id("kw")
# dr.execute_script('arguments[0].style.border="2px solid #FF0000";', elem)

# dr.execute_script("arguments[0].setAttribute('style',arguments[1]);", elem, "border:2px solid red;")
# from selenium import webdriver
#
# class demoClass:
#
#     def __new__(cls, name):
#         cls.browser = name
#         if cls.browser == "gc":
#             return webdriver.Chrome()
#         return None
#
#
# test1 = demoClass("gc")
# test1.get("https://www.baidu.com")
# test1.quit()
#


import seldom
from seldom import Seldom, data

from seldom.logging import log
from seldom import ChromeConfig
from seldom import label
from seldom import EdgeConfig


# class BaiduTest(seldom.TestCase):
#     """Baidu serach test case""".format()

    # def start(self):
    #     """
    #     可以在start中引用多个页面
    #     """
    #     self.baidu_page = BaiduPage(Seldom.driver)
    #     self.baidu_search_page = BaiduSearchPage(Seldom.driver)

    # @data([
    #     {"scene": '这是用例描述', 'keyword': 'seldom'},
    #     {"scene": '来个公式：2+3', 'keyword': 'selenium'},
    #     {"scene": 'こんにちは', 'keyword': 'unittest'},
    # ])
    # @data([
    #     ('这是用例描述11', 'seldom'),
    #     ('来个公式：2+3', 'selenium'),
    #     ('こんにちは', 'unittest'),
    # ])
    # def test_baidu2(self, scene, keyword):
    #     """
    #     used parameterized test
    #     """
    #     ...

    # def test_error(self):
    #     log.error("error case")
    #     print("普通打印 error")
    #     a
    #
    # def test_fail(self):
    #     log.warning("fail case")
    #     print("普通打印 fail")
    #     self.assertEqual(2, 3)

    # def test_case(self):
    #     """
    #     A simple test
    #     """
    #     self.baidu_page.open("https://www.baidu.com")
    #     self.baidu_page.search_input.send_keys("seldomQA")
    #     self.screenshots()
    #     self.baidu_page.search_button.click()
    #     self.sleep(2)
    #     self.screenshots()
    #     ret = self.baidu_search_page.search_result.text
    #     print(ret)

# import seldom
# from seldom import SMTP
# from seldom.logging import log
# from seldom import skip
#
#
# class BaiduTest(seldom.TestCase):
#
#     def test_case(self):
#         """a simple test case """
#         self.open("https://www.baidu.com")
#         self.type(id_="kw222", text="seldom")
#         # elems = self.get_elements(tag="el-tag")
#         # print(len(elems))
#         # self.type(id_="kw", text="seldom")
#         # self.click(id_="su")
#         # self.assertInTitle("seldom2")
#
#     def test_case2(self):
#         self.open("http://www.baidu.com")
#         self.assertEqual(1+1, 2)
#
#     def test_case3(self):
#         self.open("http://www.baidu.com")
#         self.assertEqual(1 + 1, 3)
#
#     @skip()
#     def test_case4(self):
#         self.open("http://www.baidu.com")
#         self.assertEqual(1 + 1, 3)

    # def test_bing(self):
    #     """a simple test case """
    #     self.open("https://www.bing.com")
    #     self.type(id_="sb_form_q22", text="seldom", enter=True)
    #     self.assertInTitle("seldom")


class BingTest(seldom.TestCase):

    def open_new_browser(self):
        """selenium api"""
        self.get("http://www.bing.com")
        self.type(id="sb_form_q", text="XTestRunner")
        self.click(id="sb_form_q")
        self.sleep(2)
        self.assertTitle("bing")

    # def test_case(self):
    #     """a simple test case """
    #     self.open("https://m.baidu.com")
    #     # open new browser
    #     self.open_new_browser()
    #
    #     self.type(id_="index-kw", text="seldom")
    #     self.click(id_="index-bn")
    #     self.assertTitle("seldom - 百度")


if __name__ == '__main__':
    # EdgeConfig.command_executor = "D:\webdriver\msedgedriver.exe"
    seldom.main(debug=True, browser="gc")
