#coding=utf-8
from pyse import Pyse,TestRunner
from time import sleep
import unittest

class baiduTest(unittest.TestCase):

    def setUp(self):
        self.driver = Pyse("chrome")
        self.driver.wait(10)
        self.base_url = "http://www.baidu.com"

    def test_case(self):
        self.driver.open(self.base_url)
        self.driver.click_text("设置")
        self.driver.click_text("搜索设置")
        sleep(2)
        self.driver.click("//a[@class='prefpanelgo']")
        sleep(1)
        self.driver.accept_alert()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	TestRunner("C:\\Python27\\Lib\\site-packages\\pyse\\demo").run()
