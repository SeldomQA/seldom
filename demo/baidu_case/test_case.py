# coding=utf-8
from pyse import Pyse, TestRunner
from time import sleep
import unittest


class BaiduTest(unittest.TestCase):
    ''' Baidu serach test case '''

    def setUp(self):
        self.driver = Pyse("chrome")

    def tearDown(self):
        self.driver.quit()
    
    def baidu_search(self,search_key):
        self.driver.open("https://www.baidu.com")
        self.driver.clear("id=>kw")
        self.driver.type("id=>kw", search_key)
        self.driver.click("css=>#su")
        sleep(1)

    def test_baidu1(self):
        ''' baidu search key : pyse '''
        search_key = "pyse"
        self.baidu_search(search_key)
        self.assertTrue(search_key,self.driver.get_title())

    def test_baidu2(self):
        ''' baidu search key : selenium '''
        search_key = "selenium"
        self.baidu_search(search_key)
        self.assertTrue(search_key,self.driver.get_title())


if __name__ == '__main__':
    runner = TestRunner('./','百度测试用例','测试环境：Chrome')
    runner.run()
