
![](seldom_logo.gif)

WebUI automation testing framework based on Selenium and unittest.

> 基于 selenium 和 unittest 的 Web UI自动化测试框架。

## 特点

* 提供更加简单API编写自动化测试。
* 提供脚手架，快速生成自动化测试项目。
* 全局启动和关闭浏览器，减少浏览器的启动次数。
* 支持用例参数化。
* 支持用例失败/错误重跑。
* 支持生成HTML测试报告生成，运行失败/错误自动截图。

### 安装

```shell
> pip install seldom
```

If you want to keep up with the latest version, you can install with github repository url:

```shell
> pip install -U git+https://github.com/SeldomQA/seldom.git@master
```

### Quick Start

1、查看帮助：

```shell
> seldom -h
usage: seldom [-h] [-v] [--project PROJECT] [-r R] [-install INSTALL]

WebUI automation testing framework based on Selenium.

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      show version
  --project PROJECT  Create an Seldom automation test project.
  -r R               run test case
  -install INSTALL   Install the browser driver, For example, 'chrome',
                     'firefox'.
```

2、创建项目：

```shell
>seldom --project mypro
```

目录结构如下：
```
mypro/
├── test_dir/
│   ├── test_sample.py
├── reports/
└── run.py
```

* `test_dir/`目录实现用例编写。
* `reports/` 目录存放生成的测试报告。
* `run.py` 文件运行测试用例。

3、运行项目：

```shell
> seldom -r run.py
Python 3.7.1

            _      _
           | |    | |
 ___   ___ | |  __| |  ___   _ __ ___
/ __| / _ \| | / _` | / _ \ | '_ ` _ \
\__ \|  __/| || (_| || (_) || | | | | |
|___/ \___||_| \__,_| \___/ |_| |_| |_|
-----------------------------------------
                             @itest.info

generated html file: file:///D:\mypro\reports\2019_11_12_22_28_53_result.html
.1
```

4、查看报告

你可以到 `mypro\reports\` 目录查看测试报告。

![](./test_report.png)

## API Documents

### simple demo

请查看 `demo/test_sample.py` 文件

```python
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main("test_sample.py")

```

__说明：__

* 创建测试类必须继承 `seldom.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* seldom的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。

### main() 方法

```python
import seldom

# ...

if __name__ == '__main__':

    seldom.main(path="./",
              browser="chrome",
              title="百度测试用例",
              description="测试环境：chrome",
              debug=False,
              rerun=0,
              save_last_run=False,
              driver_path=None,
    )
```

说明：

* path ： 指定测试目录或文件。
* browser: 指定测试浏览器，默认`Chrome`。
* title ： 指定测试报告标题。
* description ： 指定测试报告描述。
* debug ： debug模式，设置为True不生成测试HTML测试，默认为`False`。
* rerun : 设置失败重新运行次数，默认为 `0`。
* save_last_run : 设置只保存最后一次的结果，默认为`False`。
* driver_path : 设置浏览器驱动的`绝对`路径。要和 `browser` 设置一致。

### Run the test

```python
import seldom

seldom.main(path="./")  # 当前目录下的所有测试文件
seldom.main(path="./test_dir/")  # 指定目录下的所有测试文件
seldom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
seldom.main(path="test_sample.py")  # 指定当前目录下的测试文件
```

说明：

* 如果指定的目录，测试文件必须以`test` 开头。
* 如果要运行子目录下的文件，必须在子目录下加 `__init__.py` 文件。

### 支持的浏览器及驱动

如果你想指定测试用例在不同的浏览器中运行，非常简单，只需要在`seldom.main()`方法中通过`browser` 参数设置。

```python
import seldom

if __name__ == '__main__':
    seldom.main(browser="chrome") # chrome浏览器,默认值
    seldom.main(browser="firefox") # firefox浏览器
    seldom.main(browser="ie")  # IE浏览器
    seldom.main(browser="opera") # opera浏览器
    seldom.main(browser="edge") # edge浏览器
    seldom.main(browser="chrome_headless") # chrome浏览器headless模式
    seldom.main(browser="firefox_headless") # Firefox浏览器headless模式

```

seldom 支持chrome和frefox浏览器的驱动下载：

```shell
> seldom -install chrome
> seldom -install firefox
```

下载的驱动文件默认保存在`lib` 目录下面。

当然，你也可以手动下载不同浏览器驱动：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

### 元素定位

```html
<form id="form" class="fm" action="/s" name="f">
    <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" name="wd">
```

定位方式：

```python
self.type(id_="kw", text="seldom")
self.type(name="wd", text="seldom")
self.type(class_name="s_ipt", text="seldom")
self.type(tag="input", text="seldom")
self.type(link_text="hao123", text="seldom")
self.type(partial_link_text="hao", text="seldom")
self.type(xpath="//input[@id='kw']", text="seldom")
self.type(css="#kw", text="seldom")

```

帮助：

* [CSS选择器](https://www.w3school.com.cn/cssref/css_selectors.asp)
* [xpath语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

### 断言方法

```python
self.assertTitle("title")   # 断言标题是否等于"title"
self.assertInTitle("title") # 断言标题是否包含"title"
self.assertURL("url")  # 断言URL是否等于
self.assertInURL("url")  # 断言URL是否包含 
self.assertText("text")  # 断言页面是否存在“text”
self.assertAlertText("text") # 断言警告是否存在"text" 提示信息
```

### 跳过用例

```python
import seldom


class YouTest(seldom.TestCase):

    @seldom.skip("跳过这条用例的执行")
    def test_case(self):
        """a simple test case """
        #...

```

### 参数化测试用例

seldom 支持参数化测试用例，集成了[parameterized](https://github.com/wolever/parameterized)。

简单用法：

```python

import seldom
from seldom import data

# ...

class BaiduTest(seldom.TestCase):

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, name, keyword):
        """
         used parameterized test
        :param name: case name
        :param keyword: search keyword
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=keyword)
        self.click(css="#su")
        self.assertTitle(keyword+"_百度搜索")
```

同时seldom 也支持不同文件的读取，[帮助文档](/docs/parameterized.md)， 包括：
* csv文件
* excel文件
* json/yaml文件，需要第三方支持。

### page objects 设计模式

seldom 支持Page objects设计模式，可以配合[poium](https://github.com/wolever/parameterized) 使用。

```python
import seldom
from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "seldom"
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main("test_po_demo.py")

```

poium提供了更多好用的功能，使Page层的创建更加简单。

## 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_cn](https://github.com/GoverSky/HTMLTestRunner_cn)

* [parameterized](https://github.com/wolever/parameterized)

* [pyderman](https://github.com/shadowmoose/pyderman)

* [utx](https://github.com/jianbing/utx)

## 交流
QQ群：948994709
