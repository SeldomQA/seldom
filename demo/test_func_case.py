# coding=utf-8
import pyse,nose
from nose.tools import with_setup
from time import sleep


def my_setup_function():
    print "test case start:"


def my_teardown_function():
    print "test case end."


@with_setup(my_setup_function, my_teardown_function)
def test_baidu():
    ''' baidu search key : pyse '''
    driver = pyse.Pyse("chrome")
    driver.open("https://www.baidu.com")
    driver.type("id=>kw", "pyse")
    driver.click("id=>su")
    sleep(1)
    title = driver.get_title()
    assert title == u"pyse_百度搜索"
    driver.quit()


@with_setup(my_setup_function, my_teardown_function)
def test_youdao():
    ''' youdao search key : pyse '''
    driver = pyse.Pyse()   # default firefox browser
    driver.open("http://www.youdao.com")
    driver.type("name=>q","pyse")
    driver.click("id=>qb")
    sleep(1)
    title = driver.get_title()
    print title
    assert title=="pyse - 有道搜索"
    driver.quit()

if __name__ == '__main__':
    test_pro = pyse.TestRunner()
    test_pro.run()

'''
============运行测试用例说明========
TestRunner() 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定路径，例如：
TestRunner(r"D:/test_project/test_case")

执行run()方法运行测试用例.

'''