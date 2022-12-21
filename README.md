[GitHub](https://github.com/SeldomQA/seldom) | [Gitee](https://gitee.com/fnngj/seldom) |

![](seldom_logo.jpg)

[![PyPI version](https://badge.fury.io/py/seldom.svg)](https://badge.fury.io/py/seldom) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/seldom)
![visitors](https://visitor-badge.glitch.me/badge?page_id=SeldomQA.seldom)

Seldom is an automation testing framework based on unittest.

> seldom 是基于unittest 的自动化测试框架。

### Features

- [x] web/app/api全功能测试框架
- [x] 提供脚手架快速创建自动化项目
- [x] 集成`XTestRunner`测试报告，现代美观
- [x] 提供丰富的断言
- [x] 提供强大的`数据驱动`
- [x] 平台化支持

### Install
> 2.10.0 为了解决[107](https://github.com/SeldomQA/seldom/issues/107) 问题，我们经过反复的讨论和优化，甚至对相关库XTestRunner做了修改；以为完美解决了这个问题，没想到还是引起了一些严重的错误。为此，我们感到非常沮丧，退回到2.9.0的实现方案。请升级到2.10.1以上版本。

```shell
pip install seldom==3.1.0
```

If you want to keep up with the latest version, you can install with github repository url:

```shell
> pip install -U git+https://github.com/SeldomQA/seldom.git@master
```

### 🤖 Quick Start

1、查看帮助：

```shell
seldom --help
Usage: seldom [OPTIONS]

  seldom CLI.

Options:
  --version                       Show version.
  -P, --project TEXT              Create an Seldom automation test project.
  -cc, --clear-cache BOOLEAN      Clear all caches of seldom.
  -p, --path TEXT                 Run test case file path.
  -c, --collect / -nc, --no-collect
                                  Collect project test cases. Need the
                                  `--path`.
  -l, --level [data|method]       Parse the level of use cases. Need the
                                  --path.
  -j, --case-json TEXT            Test case files. Need the `--path`.
  -e, --env TEXT                  Set the Seldom run environment `Seldom.env`.
  -b, --browser [chrome|firefox|ie|edge|safari]
                                  The browser that runs the Web UI automation
                                  tests. Need the `--path`.
  -u, --base-url TEXT             The base-url that runs the HTTP automation
                                  tests. Need the `--path`.
  -d, --debug / -nd, --no-debug   Debug mode. Need the `--path`.
  -rr, --rerun INTEGER            The number of times a use case failed to run
                                  again. Need the `--path`.
  -r, --report TEXT               Set the test report for output. Need the
                                  `--path`.
  -m, --mod TEXT                  Run tests modules, classes or even
                                  individual test methods from the command
                                  line.
  -i, --install [chrome|firefox|ie|edge]
                                  Install the browser driver.
  -ll, --log-level [TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR]
                                  Set the log level.
  -h2c, --har2case TEXT           HAR file converts an interface test case.
  --help                          Show this message and exit.
```

2、创建项目：

```shell
> seldom -P mypro
```

目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── __init__.py
│   ├── test_web_sample.py
│   ├── test_api_sample.py
├── test_data/
│   ├── data.json
├── reports/
└── confrun.py
```

* `test_dir/` 测试用例目录。
* `test_data/` 测试数据文件目录。
* `reports/` 测试报告目录。
* `confrun.py` 运行配置文件。

3、运行项目：

* ❌️ 在`pyCharm`中右键执行。

* ✔️ 通过命令行工具执行。

```shell
> seldom -p test_dir # 运行 test_dir 测试目录


              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info
...

2022-04-30 18:37:29 log.py | INFO | -------------- Request -----------------[🚀]
2022-04-30 18:37:29 log.py | INFO | [method]: DELETE      [url]: http://httpbin.org/delete

2022-04-30 18:37:30 log.py | INFO | -------------- Response ----------------[🛬️]
2022-04-30 18:37:30 log.py | INFO | successful with status 200

2022-04-30 18:37:30 log.py | DEBUG | [type]: json      [time]: 0.725183

2022-04-30 18:37:30 log.py | DEBUG | [response]:
 {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '0', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-626d1168-457309ad306428ca5bcbb961'}, 'json': None, 'origin': '173.248.248.88', 'url': 'http://httpbin.org/delete'}

...

2022-04-30 18:37:36 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'seldom'.
2022-04-30 18:37:39 log.py | INFO | 👀 assertIn title: seldom - 搜索.
.52022-04-30 18:37:39 log.py | INFO | 📖 https://cn.bing.com
2022-04-30 18:37:41 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'poium'.
2022-04-30 18:37:42 log.py | INFO | 👀 assertIn title: poium - 搜索.
.62022-04-30 18:37:42 log.py | INFO | 📖 https://cn.bing.com
2022-04-30 18:37:43 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'XTestRunner'.
2022-04-30 18:37:44 log.py | INFO | 👀 assertIn title: XTestRunner - 搜索.
.72022-04-30 18:37:44 log.py | INFO | 📖 http://www.itest.info
2022-04-30 18:37:52 log.py | INFO | 👀 assertIn url: http://www.itest.info/.
.82022-04-30 18:37:52 log.py | SUCCESS | generated html file: file:///D:\mypro\reports\2022_04_30_18_37_29_result.html
2022-04-30 18:37:52 log.py | SUCCESS | generated log file: file:///D:\mypro\reports\seldom_log.log
```

4、查看报告

你可以到 `mypro\reports\` 目录查看测试报告。

![test report](./test_report.png)

## 🔬 Demo

> seldom继承unittest单元测试框架，完全遵循unittest编写用例规范。

[demo](/demo) 提供了丰富实例，帮你快速了解seldom的用法。

### Web UI 测试

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
    seldom.main(browser="chrome")
```

__说明：__
* `seldom.main()` 通过 `browser` 指定运行的浏览器。 

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

__说明：__

* `seldom.main()` 通过 `base_url` 指定接口项目基本URL地址。 

### App 测试

seldom 3.0 支持App测试

```python
import seldom


class TestBBS(seldom.TestCase):

    def test_bbs_search(self):
        self.sleep(5)
        self.click(id_="com.meizu.flyme.flymebbs:id/nw")
        self.type(id_="com.meizu.flyme.flymebbs:id/nw", text="flyme")
        self.click(id_="com.meizu.flyme.flymebbs:id/o1")
        self.sleep(2)
        elems = self.get_elements(id_="com.meizu.flyme.flymebbs:id/a29")
        for elem in elems:
            self.assertIn("flyme", elem.text.lower())


if __name__ == '__main__':
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    seldom.main(app_info=desired_caps, app_server="http://127.0.0.1:4723")
```
__说明：__

* `seldom.main()` 通过 `app_info` 指定App信息； `app_server` 指定appium server 地址。 

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


### 项目实例

基于seldom的web UI自动化项目：

https://github.com/SeldomQA/seldom-web-testing

基于seldom的接口自动化项目:

https://github.com/defnngj/seldom-api-testing

### 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_cn](https://github.com/GoverSky/HTMLTestRunner_cn)

* [parameterized](https://github.com/wolever/parameterized)

* [utx](https://github.com/jianbing/utx)

### 交流

QQ群：948994709


## 🔥 company

他们都在用(排名不分先后)

![](./company/samexsys.gif)

![](./company/klook.png)
