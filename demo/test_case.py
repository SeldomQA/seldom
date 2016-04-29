# coding=utf-8
from pyse import Pyse, TestRunner
from time import sleep


def test_baidu():
    ''' baidu search key : pyse '''
    driver = Pyse("chrome")
    driver.open("https://www.baidu.com")
    driver.type("id=>kw", "pyse")
    driver.click("css=>#su")
    sleep(1)
    assert "pyse" in driver.get_title()
    driver.quit()

if __name__ == '__main__':
    TestRunner().run()
