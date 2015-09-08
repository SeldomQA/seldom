# pyse
WebUI automation testing framework based on Selenium

介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。
  
特点：
* 所有方法只提供css定位，webdriver提供了8种定位方法（id\name\class name\tag name\link text\partial link text\xpath\css selector）但其实，我们使用xpath或css完全可以替代id\name\class name\tag name 等方法，本框架所提供的click_text()方法可以替代link text方法，在最版本中用css替换掉了xpath，原因是css语法更简洁。统一元素定位方法使代码看起来更具有一致性，当看到一个元素时不用再犹豫选择哪种定位方法，直接使用css就好了。
* 本框架只是对selenium（webdriver）原方法的简单封装，精简为30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 集成了HTMLTestRunner 测试报告，并对测试报告做了增强，使每一个用例都能自动产生截图。

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
        ''' test search key : pyse '''
        self.driver = Pyse("chrome")
        driver = self.driver
        driver.open("http://www.baidu.com")
        driver.type("#kw","pyse")
        driver.click("#su")
        sleep(1)
        title = driver.get_title()
        self.assertEqual("pyse_百度搜索",title)


    if __name__ == '__main__':
      test_pro = TestRunner()
      test_pro.run()
==========================================================
运行测试用例说明：
* TestRunner() 默认匹配当前目录下"*_case.py"的文件并执行。当然也可以指定路径，例如：
TestRunner(r"D:/test_project/test_case")
* 执行run()方法运行测试用例，默认的生成的报告标题为：Pyse Test Report ，可以自定位报告标题。例如：
run(title_text = u'xx项目测试报告', description_text = u'环境：window 7  Chrome')
或：
run(u'xx项目测试报告', u'环境：window 7  Chrome')



元素定位：
==========================================================
  关于元素的定位，经过权衡，抛弃了之前采用的xpath，而选择css，主要是因为css的语法写起来更简洁。

    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
==========================================================
    
  id定位:

    driver.type("#kw", "pyse")
==========================================================
    
  class定位:

    driver.type(".s_ipt", u"pyse")
==========================================================
    
  name定位:

    driver.type("[name=wd]", "pyse")
    driver.type("[name='wd']", "pyse")
==========================================================

  tag name定位:

    driver.type("input", "pyse")
    driver.type("span>input", "pyse")
    driver.type("from>span>input", "pyse")
==========================================================

  link text定位：
    click_text()方法可以做到这一点，例如，点击百度首页上的"新闻"链接。

    driver.click_text("新闻")
==========================================================
    
  css更封复杂的更定写法：

    driver.type("span.bg s_ipt_wr>input.s_ipt","pyse")
    driver.type("span.bg s_btn_wr>input#su","pyse")
==========================================================
    
  css选择器参考手册：
  http://www.w3school.com.cn/cssref/css_selectors.asp
