# coding=utf-8
from pyse import Pyse, TestRunner
from nose.tools import with_setup
from time import sleep


def my_setup_function():
    print "test case start:"


def my_teardown_function():
    print "test case end."


@with_setup(my_setup_function, my_teardown_function)
def test_baidu():
    ''' baidu search key : pyse '''
    driver = Pyse("chrome")
    driver.open("https://www.baidu.com")
    driver.type("id=>kw", "pyse")
    driver.click("id=>su")
    sleep(1)
    title = driver.get_title()
    assert "pyse" in title
    driver.quit()


@with_setup(my_setup_function, my_teardown_function)
def test_youdao():
    ''' youdao search key : pyse '''
    driver = Pyse()   # default firefox browser
    driver.open("http://www.youdao.com")
    driver.type("name=>q", "pyse")
    driver.click("id=>qb")
    sleep(1)
    title = driver.get_title()
    print title
    assert title == "pyse - 有道搜索"
    driver.quit()

if __name__ == '__main__':
    test_pro = TestRunner()
    test_pro.run()