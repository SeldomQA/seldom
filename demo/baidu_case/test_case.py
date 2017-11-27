# coding=utf-8
from pyse import Pyse, TestRunner
from time import sleep
import unittest
from parameterized import parameterized


class BaiduTest(unittest.TestCase):
    ''' Baidu serach test case '''

    def setUp(self):
        self.driver = Pyse("chrome")
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand([
        (1, 'pyse'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self,name,search_key):
        ''' baidu search key : pyse '''
        self.driver.open(self.base_url)
        self.driver.clear("id=>kw")
        self.driver.type("id=>kw", search_key)
        self.driver.click("css=>#su")
        self.driver.assertTitle(search_key)


if __name__ == '__main__':
    runner = TestRunner('./','百度测试用例','测试环境：Chrome')
    runner.run()
