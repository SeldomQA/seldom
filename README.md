# seldom

WebUI automation testing framework based on Selenium and unittest.

> 基于 selenium 和 unittest 的 Web UI自动化测试框架。

## 特点

* 默认使用CSS定位，同时支持多种定位方法（id\name\class\link_text\xpath\css）。
* 基于Selenium二次封装，使用更简单。
* 提供脚手架，快速生成自动化测试项目。
* 自动生成/reports/目录，以及HTML测试报告生成。
* 自带断言方法，断言title、URL 和 text。
* 支持用例参数化。
* 只用用例失败重跑。
* 支持用例失败/错误截图。

### 安装

```shell
> pip install -U git+https://github.com/defnngj/seldom.git@master
```

依赖库：
```
selenium>=3.12.0
parameterized==0.7.0
poium==0.5.1
```

### Quick Start

1、查看帮助：

```shell
> pyse -h
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
>pyse --startproject mypro

2019-11-17 20:27:12,466 - INFO - Start to create new test project: mypro
2019-11-17 20:27:12,467 - INFO - CWD: D:\

2019-11-17 20:27:12,468 - INFO - created folder: mypro
2019-11-17 20:27:12,469 - INFO - created folder: mypro\page
2019-11-17 20:27:12,469 - INFO - created folder: mypro\test_dir
2019-11-17 20:27:12,470 - INFO - created folder: mypro\reports
2019-11-17 20:27:12,471 - INFO - created file: mypro\page\sample_page.py
2019-11-17 20:27:12,471 - INFO - created file: mypro\test_dir\test_sample.py
2019-11-17 20:27:12,472 - INFO - created file: mypro\run.py
```

3、目录结构：
```
mypro/
├── page/
│   ├── sample_page.py
├── test_dir/
│   ├── test_sample.py
├── report/
└── run.py
```

* `page/`目录封装元素定位，使用 [poium](https://github.com/defnngj/poium) 实现元素定位。

```python
# sample_page.py
from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page element"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")
```

* `test_dir/`目录实现用例编写。

```python
#test_sample.py
import pyse
from page.sample_page import BaiduPage


class YouTest(pyse.TestCase):

    def test_case(self):
        """a simple test case """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "pyse"
        page.search_button.click()
        self.assertTitle("pyse")

```
* `report/` 目录存放生成的测试报告。

* `run.py` 文件运行测试用例

```python
import pyse


if __name__ == '__main__':
    # run test
    # pyse.main("./test_dir/")
    pyse.main("./test_dir/test_sample.py")

```
3、运行项目：

```shell
> pyse -r run.py
Python 3.7.1                                                                    

 ______  __   __  _______  _______                                              
|   _  ||  | |  ||  _____||   ____|                                             
|  |_| ||  |_|  || |_____ |  |____                                              
|   ___||_     _||_____  ||   ____|                                             
|  |      |   |   _____| ||  |____                                              
|__|      |___|  |_______||_______|                                                                                     
generated html file: file:///D:\mypro\reports\2019_11_12_22_28_53_result.html   
.1                                                                              
```

4、查看报告

你可以到 `mypro\reports\` 目录查看测试报告。

![](./test_report.png)

## API Documents

### simple demo

请查看 `demo/test_po_demo.py` 文件

```python
import pyse
from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")


class BaiduTest(pyse.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "pyse"
        page.search_button.click()
        self.assertTitle("pyse_百度搜索")
```

__说明：__

* 创建测试类必须继承 `pyse.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* 通过`poium`封装元素定位，在测试用例当中使用。
* 在使用`BaiduPage`的时必须将`self.driver` 传给他。
* pyse的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。


### main() 方法

```python
import pyse

# ...

if __name__ == '__main__':
    
    pyse.main(path="./",
              browser="chrome",
              title="百度测试用例", 
              description="测试环境：Firefox", 
              debug=True,
              rerun=0
    )
```

说明：

* path ： 指定测试目录。
* browser: 指定测试浏览器，默认Chrome。
* title ： 指定测试项目标题。
* description ： 指定测试描述。
* debug ： debug模式，设置为True不生成测试HTML测试。
* rerun : 设置失败重新运行次数，默认为 0。

### Run the test

```python
import pyse

pyse.main(path="./")  # 当前目录下的所有测试文件
pyse.main(path="./test_dir/")  # 指定目录下的所有测试文件
pyse.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
pyse.main(path="test_sample.py")  # 指定当前目录下的测试文件
```

说明：

* 如果指定的目录，测试文件必须以`test` 开头。
* 如果要运行子目录下的文件，必须在子目录下加 `__init__.py` 文件。

### 支持的浏览器及驱动

如果你想指定测试用例在不同的浏览器中运行，非常简单，只需要在`pyse.main()`方法中通过`browser` 参数设置。

```python
import pyse

if __name__ == '__main__':
    pyse.main(browser="chrome") # chrome浏览器,默认值
    pyse.main(browser="firefox") # firefox浏览器
    pyse.main(browser="ie")  # IE浏览器
    pyse.main(browser="opera") # opera浏览器
    pyse.main(browser="edge") # edge浏览器
    pyse.main(browser="chrome_headless") # chrome浏览器headless模式

```

不同浏览器驱动下载地址：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

==========================================================

### 元素定位

请参考 [poium](https://github.com/defnngj/poium/wiki) wiki

```html
<form id="form" class="fm" action="/s" name="f">
    <span class="bg s_ipt_wr quickdelete-wrap">
        <input id="kw" class="s_ipt" name="wd">
```

定位方式（推荐使用 CSS）：

```python
from poium import Page, PageElement

class xxPage(Page):
    elem_id = PageElement(id_='id')
    elem_name = PageElement(name='name')
    elem_class = PageElement(class_name='class')
    elem_tag = PageElement(tag='input')
    elem_link_text = PageElement(link_text='this_is_link')
    elem_partial_link_text = PageElement(partial_link_text='is_link')
    elem_xpath = PageElement(xpath='//*[@id="kk"]')
    elem_css = PageElement(css='#id')

```

### 参数化测试用例

pyse 支持参数化测试用例，集成了[parameterized](https://github.com/wolever/parameterized)。

```python

import pyse
from pyse import ddt

# ...

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
        :param keyword: search keyword
        """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "pyse"
        page.search_button.click()
        self.assertTitle("pyse_百度搜索")
```

## 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_Chart](https://github.com/githublitao/HTMLTestRunner_Chart)

* [parameterized](https://github.com/wolever/parameterized)
