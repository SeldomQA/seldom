# pyse
WebUI automation testing framework based on Selenium and unittest.

#### 介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。

#### 特点：
* 支持多种定位方法（id\name\class\link_text\xpath\css）。
* 本框架只是对selenium（webdriver）原生方法进行了简单的封装，精简为大约30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 基于unittest单元测试框架，所以测试文件与测试方法遵循unittest开发。
* 自动生成HTML测试报告生成。

#### 安装说明：
* Python3.5+ : https://www.python.org/
* Selenium3.6.0+ : https://pypi.python.org/pypi/selenium
* 进入pyse/目录，执行:

```
python setup.py install。
```

#### 例子：

请查看demo/目录

```python
from pyse import Pyse, TestRunner
from time import sleep
import unittest

class BaiduTest(unittest.TestCase):

    def test_baidu(self):
        ''' baidu search key : pyse '''
        driver = Pyse("chrome")
        driver.open("https://www.baidu.com")
        driver.clear("id=>kw")
        driver.type("id=>kw", "pyse")
        driver.click("css=>#su")
        sleep(1)
        self.assertTrue("pyse",driver.get_title())
        driver.quit()

if __name__ == '__main__':
    runner = TestRunner()
    runner.run()
```

运行测试用例说明：
* TestRunner() 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定测试目录，例如：
TestRunner("path/you/project/test_case/")  # 注意用斜线"/"表示路径。
* 执行run()方法运行测试用例

#### 支持的浏览器及驱动：

```python

driver = Pyse("firefox")   #Firefox
driver = Pyse("ff")        #Firefox
driver = Pyse("chrome")    # Chrome
driver = Pyse("internet explorer")  #IE
driver = Pyse("ie")        #IE
driver = Pyse("opera")  #Opera
driver = Pyse("chrome_headless")  #Chrome headless模式
driver = Pyse("edge")  #Edge
```

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

phantomjs(PhantomJS):http://phantomjs.org

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

#### 元素定位:

pyse支持多种定位方式，id、name、class、link text、xpath和css。把定位方法与定位内容一体，写起更加简洁。
```html
    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
```

定位方式：

```python
driver.type("id=>kw", "pyse")  #id

driver.type("class=>s_ipt", "pyse")  #class定位

driver.type("name=>wd", "pyse")  #name

driver.click_text("link_text=>新闻") #link text (点击百度首页上的"新闻"链接。)

driver.type("xpath=>//*[@class='s_ipt']","pyse")  #xpath
driver.type("xpath=>//*[@id='kw']","pyse")        #xpath

driver.type("css=>.s_ipt","pyse")     #css
driver.type("css=>#su","pyse")        #css

```

==========================================================

  css选择器参考手册：
  http://www.w3school.com.cn/cssref/css_selectors.asp
  nose基本用法：
  http://pythontesting.net/framework/nose/nose-introduction/
