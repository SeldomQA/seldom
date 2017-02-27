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
        sleep(1)
        self.assertTrue("pyse",driver.get_title())
        driver.quit()


if __name__ == '__main__':
    runner = TestRunner()
    runner.run()
