# pyse
WebUI automation testing framework based on Selenium and unittest.

#### 介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。

#### 特点：
* 默认使用CSS定位，同时支持多种定位方法（id\name\class\link_text\xpath\css）。
* 本框架只是对selenium（webdriver）原生方法进行了简单的封装，精简为大约30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 以测试类为单位，自动打开和关闭浏览器，减少浏览器的打开/关闭次数，节省时间。
* 自动生成/report/目录，以及HTML测试报告生成。
* 自带断言方法，断言title、URL 和 text。

#### 安装说明：
* Python 3.5+ : https://www.python.org/
* Selenium 3.12.0 : https://pypi.python.org/pypi/selenium
* 进入pyse/目录，执行:

```
> python setup.py install
```

#### 例子：

请查看demo/test_case.py目录

```python
import pyse

class BaiduTest(pyse.TestCase):

    def test_baidu(self):
        ''' baidu search key : pyse '''
        self.open("https://www.baidu.com/")
        self.type("#kw", "pyse")
        self.click("#su")
        self.assertTitle("pyse_百度搜索")

if __name__ == '__main__':
    runner = pyse.TestRunner()
    runner.run()
```

运行测试用例说明：
* 测试用例文件命名必须以“__test__”开头。
* 默认情况下使用 __Chrome__ 浏览器运行测试用例。
* 元素定位方式默认使用 CSS 语法 `#kw`, 也可以显示的使用 `css=>#kw`。
* pyse的TestCase类中默认封装了`assertTitle`、`assertUrl` 和 `assertText`等断言。
* `TestRunner()` 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定测试目录，例如：
TestRunner("path/you/project/test_case/")  # 注意用斜线"/"表示路径。
* 执行`run()`方法运行测试用例并生成测试报告，在调试测试用例过程中可以使用 `debug()` 方法将不会生成HTML测试报告。


#### 支持的浏览器及驱动：

指定运行的浏览器：

```python
import pyse

class YouTest(pyse.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
    
    def test_case(self):
        #……

```

支持的浏览器:

```python
cls.driver = Pyse("firefox")   #Firefox
cls.driver = Pyse("chrome")    # Chrome
cls.driver = Pyse("ie")        #IE
cls.driver = Pyse("opera")     #Opera
cls.driver = Pyse("edge")      #Edge
cls.driver = Pyse("chrome_headless")  #Chrome headless模式
```

浏览器驱动下载地址：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

#### 元素定位:

pyse支持多种定位方式，id、name、class、link text、xpath和css。把定位方法与定位内容一体，写起更加简洁。
```html
    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
```

定位方式（推荐使用 CSS）：

```python
# 默认支持CSS语法
driver.type(".s_ipt","pyse")     #css
driver.type("#su","pyse")        #css

driver.type("id=>kw", "pyse")  #id

driver.type("class=>s_ipt", "pyse")  #class定位

driver.type("name=>wd", "pyse")  #name

driver.type("xpath=>//*[@class='s_ipt']","pyse")  #xpath
driver.type("xpath=>//*[@id='kw']","pyse")        #xpath

driver.click_text("link_text=>新闻") #link text (点击百度首页上的"新闻"链接)

```

==========================================================

  css选择器参考手册：
  http://www.w3school.com.cn/cssref/css_selectors.asp

#### 测试报告

![](./test_report.png)
