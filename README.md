[GitHub](https://github.com/SeldomQA/seldom) | [Gitee](https://gitee.com/fnngj/seldom) |

![](seldom_logo.jpg)

[![PyPI version](https://badge.fury.io/py/seldom.svg)](https://badge.fury.io/py/seldom) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/seldom)
![visitors](https://visitor-badge.glitch.me/badge?page_id=SeldomQA.seldom)

WebUI/HTTP automation testing framework based on unittest.

> 基于unittest 的 Web UI/HTTP自动化测试框架。

### 特点

* 集成`selenium`/`requests`，支持Web UI/HTTP测试。
* 集成`XTestRunner`, 支持HTML/XML格式的测试报告。
* 提供脚手架，快速生成自动化测试项目。
* 提供强大的测试数据参数化。
* 提供丰富的断言。
* 支持给用例标签，及黑白名单。
* 支持生成随机测试数据。
* 支持设置用例依赖。


### Install

```shell
> pip install seldom
```

If you want to keep up with the latest version, you can install with github repository url:

```shell
> pip install -U git+https://github.com/SeldomQA/seldom.git@master
```

### 🤖 Quick Start

1、查看帮助：

```shell
> seldom -h
usage: seldom [-h] [-v] [-project PROJECT] [-h2c H2C] [-r R] [-m M]
              [-install INSTALL]

WebUI/HTTP automation testing framework based on unittest.

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show version
  -project PROJECT  Create an Seldom automation test project.
  -h2c H2C          HAR file converts an interface test case.
  -r R              run test case
  -m M              run tests modules, classes or even individual test methods
                    from the command line
  -install INSTALL  Install the browser driver, For example, 'chrome', 'firefox',
                    'ie', 'edge', 'opera'.
```

2、创建项目：

```shell
> seldom -project mypro
```

目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── test_sample.py
├── test_data/
│   ├── data.json
├── reports/
└── run.py
```

* `test_dir/` 测试用例目录。
* `test_data/` 测试数据文件目录。
* `reports/` 测试报告目录。
* `run.py` 运行测试用例主文件。

3、运行项目：

> ❌️ 在`pyCharm`中右键执行。
>
> ✔️ 通过命令行工具执行。

```shell
> python run.py


              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.7.0
-----------------------------------------
                             @itest.info

2022-03-26 17:36:13.346 | INFO     | seldom.logging.log:info:45 - 📖 https://www.baidu.com
2022-03-26 17:36:18.187 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: id=kw  -> input 'seldom'.
2022-03-26 17:36:19.025 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: css selector=#su  -> click.
2022-03-26 17:36:20.234 | INFO     | seldom.logging.log:info:45 - 👀 assertIn title: seldom_百度搜索.
.12022-03-26 17:36:20.236 | INFO     | seldom.logging.log:info:45 - 📖 https://www.baidu.com
2022-03-26 17:36:21.370 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: id=kw  -> input 'poium'.
2022-03-26 17:36:22.185 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: css selector=#su  -> click.
2022-03-26 17:36:23.297 | INFO     | seldom.logging.log:info:45 - 👀 assertIn title: poium_百度搜索.
.22022-03-26 17:36:23.299 | INFO     | seldom.logging.log:info:45 - 📖 https://www.baidu.com
2022-03-26 17:36:24.745 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: id=kw  -> input 'HTMLTestRunner'.
2022-03-26 17:36:25.599 | INFO     | seldom.logging.log:info:45 - ✅ Find 1 element: css selector=#su  -> click.
2022-03-26 17:36:28.059 | INFO     | seldom.logging.log:info:45 - 👀 assertIn title: HTMLTestRunner_百度搜索.
.32022-03-26 17:36:28.060 | INFO     | seldom.logging.log:info:45 - 📖 http://www.itest.info
2022-03-26 17:36:38.541 | INFO     | seldom.logging.log:info:45 - 👀 assertIn url: http://www.itest.info/.
.42022-03-26 17:36:38.553 | SUCCESS  | seldom.logging.log:printf:75 - generated html file: file:///D:\mypro\reports\2022_03_26_17_36_12_result.html
2022-03-26 17:36:38.555 | SUCCESS  | seldom.logging.log:printf:75 - generated log file: file:///D:\mypro\reports\2022_03_26_17_36_12_log.log
.1.2.3.4
```

4、查看报告

你可以到 `mypro\reports\` 目录查看测试报告。

![test report](./test_report.png)

## 🔬 Demo

### Web 测试

[demo](/demo) 提供了丰富实例，帮你快速了解seldom的用法。

简单的实例 `demo/test_dir/test_first_demo.py` 

```python
import seldom
from seldom import Steps


class BaiduTest(seldom.TestCase):

    def test_case_one(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom_百度搜索")

    def test_case_two(self):
        """method chaining """
        Steps(url="https://www.baidu.com").open().find("#kw").type("seldom").find("#su").click()
        self.assertTitle("seldom_百度搜索")

if __name__ == '__main__':
    seldom.main()

```

__说明：__

* 创建测试类必须继承 `seldom.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* seldom的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。
* `Steps`类提供了一套方法链的API，编写简单的用例更连贯。

### HTTP 测试

seldom 2.0 支持HTTP测试

```python
import seldom


class TestRequest(seldom.TestCase):

    def test_put_method(self):
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete('/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org")
```

### Run the test

```python
import seldom

seldom.main()  # 默认运行当前测试文件
seldom.main(path="./")  # 当前目录下的所有测试文件
seldom.main(path="./test_dir/")  # 指定目录下的所有测试文件
seldom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
```


## 📖 Document

[中文文档](https://seldomqa.github.io/)

[English document(readthedocs)](https://seldomqa.readthedocs.io/en/latest/index.html)

### 项目实例

基于seldom的web UI自动化项目：

https://github.com/SeldomQA/seldom-web-testing

基于seldom的接口自动化项目:

https://github.com/defnngj/seldom-api-testing

### 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_cn](https://github.com/GoverSky/HTMLTestRunner_cn)

* [parameterized](https://github.com/wolever/parameterized)

* [pyderman](https://github.com/shadowmoose/pyderman)

* [utx](https://github.com/jianbing/utx)

### 交流

QQ群：948994709


## 🔥 company

他们都在用(排名不分先后)

![](./company/samexsys.gif)

![](./company/klook.png)
