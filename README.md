# pyse
WebUI automation testing framework based on Selenium and Nose.

介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。
  
特点：
* 支持多种定位方法（id\name\class\link_text\xpath\css）。
* 本框架只是对selenium（webdriver）原生方法进行了简单的封装，精简为大约30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 基于nose单元测试框架，所以测试文件与测试方法遵循nose的命名规范。
* 自动生成HTML测试报告生成。

安装说明：
* Python2.7+ :https://www.python.org/
* 执行 >python setup.py install ,自动安装所有依赖：selenium、nose、nose-html-reporting。


例子：
   请查看demo目录

=====================================================
    # coding=utf-8
    from pyse import Pyse, TestRunner
    from time import sleep

    def test_baidu():
      ''' baidu search key : pyse '''
      driver = Pyse("chrome")
      driver.open("https://www.baidu.com")
      driver.type("id=>kw","pyse")
      driver.click("css=>#su")
      sleep(1)
      assert "pyse" in driver.get_title()
      driver.quit()

    if __name__ == '__main__':
      test_pro = TestRunner()
      test_pro.run()

==========================================================
运行测试用例说明：
* TestRunner() 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定测试目录，例如：
TestRunner("D:/you/project/test_case/")  # 注意用斜线"/"表示路径。
* 执行run()方法运行测试用例

支持的浏览器及驱动：
==========================================================
  Firefox:
  
    driver = Pyse("firefox")  
  或：
  
    driver = Pyse("ff")
  
  Chrome:
  
    driver = Pyse("chrome")  
  
  IE:
  
    driver = Pyse("internet explorer")
  或：
  
    driver = Pyse("ie")
  
  Opera:
  
    driver = Pyse("opera")
  
  PhantomJS:
  
    driver = Pyse("phantomjs")


Chromedriver:https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer:http://selenium-release.storage.googleapis.com/index.html

operadriver:https://github.com/operasoftware/operachromiumdriver/releases

phantomjs:http://phantomjs.org

==========================================================

元素定位：
==========================================================
  pyse支持多种定位方式，id、name、class、link text、xpath和css。把定位方法与定位内容一体，写起更加简洁。

    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
==========================================================
    
  id定位:

    driver.type("id=>kw", "pyse")
==========================================================
    
  class定位:

    driver.type("class=>s_ipt", "pyse")
==========================================================
    
  name定位:

    driver.type("name=>wd", "pyse")
==========================================================

  link text定位：
    点击百度首页上的"新闻"链接。

    driver.click_text(u"link_text=>新闻")
==========================================================

  xpath定位：

    driver.type("xpath=>//*[@class='s_ipt']","pyse")
    driver.type("xpath=>//*[@id='kw']","pyse")
==========================================================
     
  css定位：

    driver.type("css=>.s_ipt","pyse")
    driver.type("css=>#su","pyse")
==========================================================
    
  css选择器参考手册：
  http://www.w3school.com.cn/cssref/css_selectors.asp
  nose基本用法：
  http://pythontesting.net/framework/nose/nose-introduction/
