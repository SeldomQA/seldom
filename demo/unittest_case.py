# coding=utf-8
from pyse import Pyse, TestRunner, myunit
from time import sleep

'''
============运行测试用例说明========
TestRunner() 默认匹配当前目录下"*_case.py"的文件并执行。当然也可以指定路径，例如：
TestRunner(r"D:/test_project/test_case")

执行run()方法运行测试用例，默认的生成的报告标题为：Pyse Test Report ，可以自定义报告标题。例如：
run(title_text = u'xx项目测试报告', description_text = u'环境：window 7  Chrome')

'''

class BaiduTest(myunit.MyTest):
    ''' baidu test '''

    def test_case(self):
        ''' test search key : pyse '''
        self.driver = Pyse("chrome")
        driver = self.driver
        driver.open("http://www.baidu.com")
        driver.type("#kw","pyse")
        driver.click("#su")
        sleep(1)
        title = driver.get_title()
        self.assertEqual(title,"pyse_百度搜索")


if __name__ == '__main__':
    test_pro = TestRunner()
    test_pro.run()

