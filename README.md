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
> seldom -h
usage: seldom [-h] [-V] [--startproject STARTPROJECT] [-r R]

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
>seldom --startproject mypro
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
* `test_dir/`目录实现用例编写。
* `report/` 目录存放生成的测试报告。
* `run.py` 文件运行测试用例

3、运行项目：

```shell
> seldom -r run.py
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
```

__说明：__

* 创建测试类必须继承 `seldom.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* 通过`poium`封装元素定位，在测试用例当中使用。
* 在使用`BaiduPage`的时必须将`self.driver` 传给他。
* seldom的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。


### main() 方法

```python
import seldom

# ...

if __name__ == '__main__':
    
    seldom.main(path="./",
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

seldom 支持参数化测试用例，集成了[parameterized](https://github.com/wolever/parameterized)。

```python

import seldom
from seldom import ddt

# ...

class BaiduTest(seldom.TestCase):

    @ddt.data([
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
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "seldom"
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")
```

## 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_Chart](https://github.com/githublitao/HTMLTestRunner_Chart)

* [parameterized](https://github.com/wolever/parameterized)
