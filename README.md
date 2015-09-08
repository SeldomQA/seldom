# pyse
WebUI automation testing framework based on Selenium

介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。
  
特点：
* 所有方法只提供xpath定位，webdriver提供了8种定位方法（id\name\class name\tag name\link text\partial link text\xpath\css selector）但xpath一定程度可以替代id\name\class name\tag name 等方法，本框架所提供的click_text()方法可以替代link text方法，所以只用xpath
定位对不影响框架本身对元素的定位能力，又保证了定位方法的一致性。
* 本框架只是对selenium（webdriver）原方法的简单封装，精简为30个方法，经过我的实践，这些方法完全够胜任于我们的自动化工作。
* 集成了HTMLTestRunner 测试报告，并对测试报告做了增加，使每一个用例都能产生截图。

安装及前提条件：
* Python2.7+ :https://www.python.org/
* selenium  :https://pypi.python.org/pypi/selenium
* 安装pyse ,将其克隆到本地，将pyse目录放到..\Python27\Lib\site-packages\目录下即可


例子：
   请查看demo目录

=====================================================
    # coding=utf-8
    from pyse import Pyse, TestRunner, myunit
    from time import sleep

    class BaiduTest(myunit.MyTest):
      ''' baidu test '''

    def test_case(self):
        ''' test key : pyse '''
        self.driver = Pyse("chrome")
        driver = self.driver
        driver.open("http://www.baidu.com")
        driver.type("//*[@id='kw']","pyse")
        driver.click("//*[@id='su']")
        sleep(1)
        title = driver.get_title()
        self.assertEqual("pyse_百度搜索",title)


    if __name__ == '__main__':
      test_pro = TestRunner()
      test_pro.run()
==========================================================
* TestRunner()类默认匹配"*_case.py"文件，如：baidu_case.py。当然也可以指定测试用例的目录，如：TestRunner("D:/test_pro/test_case")
* run() 可定义测试报告的标题和表述，如：run(u"xx项目测试报告",u"运行环境：windows 7,chrome")




