from pyse import Pyse, TestRunner
from time import sleep
import unittest

class BaiduTest(unittest.TestCase):

    def test_baidu(self):
        ''' baidu search key : pyse '''
        driver = Pyse("chrome")
        driver.open("https://www.baidu.com/")
        driver.clear("id=>kw")
        driver.type("id=>kw", "pyse")
        driver.click("css=>#su")
        driver.assertTitle("pyse")
        driver.assertText("xpath=>//div/h3/a", "基于selenium的pyse自动化测试框架 - 虫师 - 博客园")
        driver.quit()


if __name__ == '__main__':
    runner = TestRunner()
    runner.run()
