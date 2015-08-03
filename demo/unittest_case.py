# coding=utf-8
from pyse import Pyse, TestRunner, myunit
from time import sleep


class BaiduTest(myunit.MyTest):
    ''' baidu test
    '''

    def test_case(self):
        ''' test key : pyse '''
        self.driver = Pyse("chrome")
        driver = self.driver
        driver.open("http://www.baidu.com")
        driver.type("//*[@id='kw']","pyse")
        driver.click("//*[@id='su']")
        sleep(1)


if __name__ == '__main__':
    test_pro = TestRunner(r"C:\Python27\Lib\site-packages\pyse\demo")
    test_pro.run()
