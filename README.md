# pyse
WebUI automation testing framework based on Selenium and unittest.

### 介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium所提供的方法操作更简洁。

### 特点：
* 默认使用CSS定位，同时支持多种定位方法（id\name\class\link_text\xpath\css）。
* 本框架只是对selenium（webdriver）原生方法进行了简单的封装，精简为大约30个方法，这些方法基本能够胜任于我们的web自动化测试。
* 以测试类为单位，自动打开和关闭浏览器，减少浏览器的打开/关闭次数，节省时间。
* 自动生成/report/目录，以及HTML测试报告生成。
* 自带断言方法，断言title、URL 和 text。

### 安装：

```
> pip install -U git+https://github.com/defnngj/pyse.git@master
```

### pyse命令：

1、查看帮助：

```shell
pyse -h
usage: pyse [-h] [-V] [--startproject STARTPROJECT] [-r R]

WebUI automation testing framework based on Selenium.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  --startproject STARTPROJECT
                        Specify new project name.
  -r R                  run test case
```

2、创建项目：

```shell
pyse --startproject mypro
2019-11-07 00:24:57,783 - INFO - Start to create new test project: mypro

2019-11-07 00:24:57,784 - INFO - CWD: D:\

2019-11-07 00:24:57,785 - INFO - created folder: mypro
2019-11-07 00:24:57,786 - INFO - created folder: mypro\test_dir
2019-11-07 00:24:57,787 - INFO - created folder: mypro\reports
2019-11-07 00:24:57,788 - INFO - created file: mypro\test_dir\test_sample.py
2019-11-07 00:24:57,789 - INFO - created file: mypro\run.py
```

3、运行项目：

```shell
> cd mypro\
> pyse -r run.py
```
你可以到 `mypro\reports\` 目录查看测试报告。

### 编写测试：

请查看 `test_sample.py` 文件

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
    pyse.main(debug=True)
```

代码说明：
* 测试用例文件命名必须以 `test` 开头。
* 元素定位方式默认使用 CSS 语法 `#kw`, 也可以显示的使用 `css=>#kw`。
* pyse的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。
* 通过`main()`方法运行测试用例。

**main()方法参数**
```shell
pyse.main(path="./",
          browser="chrome",
          title="百度测试用例", 
          description="测试环境：Firefox", 
          debug=True
)
```

说明：
* path ： 指定测试目录。
* browser: 指定测试浏览器，默认Chrome。
* title ： 指定测试项目标题。
* description ： 指定测试环境描述。
* debug ： debug模式，设置为True不生成测试HTML测试。

### 支持的浏览器及驱动：

如果你想指定测试用例在不同的浏览器中运行，非常简单，只需要在`pyse.main()`方法中通过`browser`设置。

```python

if __name__ == '__main__':
    pyse.main(browser="firefox")

```

支持的浏览器包括："chrome"、"firefox"、"ie"、"opera"、"edge"、"chrome_headless" 等。

不同浏览器驱动下载地址：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

### 元素定位:

pyse支持多种定位方式，id、name、class、link text、xpath和css。把定位方法与定位内容一体，写起更加简洁。
```html
    <form id="form" class="fm" action="/s" name="f">
      <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">
```

定位方式（推荐使用 CSS）：

```python
# 默认支持CSS语法
self.type(".s_ipt","pyse")     #css
self.type("#su","pyse")        #css

# id
self.type("id=>kw", "pyse")  #id

# class name
self.type("class=>s_ipt", "pyse")  #class定位

# name
self.type("name=>wd", "pyse")  #name

# xpath
self.type("xpath=>//*[@class='s_ipt']","pyse")  #xpath
self.type("xpath=>//*[@id='kw']","pyse")        #xpath

# link text
self.click_text("link_text=>新闻") #link text (点击百度首页上的"新闻"链接)

```

css选择器参考手册：
http://www.w3school.com.cn/cssref/css_selectors.asp

### 参数化测试用例
pyse 支持参数化测试用例，集成了[parameterized](https://github.com/wolever/parameterized)。

```python

import pyse
from pyse import ddt


class BaiduTest(pyse.TestCase):

    @ddt.data([
        (1, 'pyse'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, name, keyword):
        """
         used parameterized test
        :param name: case name
        :param search_key: search keyword
        """
        self.open("https://www.baidu.com")
        self.clear("id=>kw")
        self.type("id=>kw", keyword)
        self.click("css=>#su")
        self.assertTitle(keyword)

```

### 测试报告

![](./test_report.png)
