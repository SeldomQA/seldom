
![](seldom_logo.png)

WebUI automation testing framework based on Selenium and unittest.

> 基于 selenium 和 unittest 的 Web UI自动化测试框架。

## 特点

* 提供更加简单API编写自动化测试。
* 提供脚手架，快速生成自动化测试项目。
* 全局启动和关闭浏览器，减少浏览器的启动次数。
* 支持用例参数化。
* 支持用例失败/错误重跑。
* 定制化HTML测试报告，用例失败/错误自动截图。

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

```shell
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

![test report](./test_report.png)

## Documents

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
    seldom.main()

```

__说明：__

* 创建测试类必须继承 `seldom.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* seldom的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。


### Run the test

```python
import seldom

seldom.main()  # 默认运行当前测试文件
seldom.main(path="./")  # 当前目录下的所有测试文件
seldom.main(path="./test_dir/")  # 指定目录下的所有测试文件
seldom.main(path="./test_dir/test_sample.py")  # 指定目录下的测试文件
```

说明：

* 如果指定的目录，测试文件必须以`test` 开头。
* 如果要运行子目录下的文件，必须在子目录下加 `__init__.py` 文件。

### seldom 文档

请阅读下面的文档，帮助你快速学会Seldom。

* [seldom安装](./docs/install.md)

* [seldom创建项目](./docs/create_project.md)

* [浏览器&驱动](./docs/driver.md)

* [运行测试](./docs/run_test.md)

* [main()方法](./docs/main.md)

* [生成测试报告](./docs/reports.md)

* [seldom 元素定位](./docs/find_element.md)

* [seldom API](./docs/seldom_api.md)

* [seldom 断言](./docs/assert.md)

* [用例失败重跑&自动截图](./docs/rerun_screenshot.md)

* [数据驱动最佳实践](./docs/parameterized.md)

* [实现Page Objects设计模式](./docs/poium.md)

* [生成测试数据](./docs/testdata.md)

* [跳过测试用例](./docs/skip.md)

* [发邮件功能](./docs/send_mail.md)

* [setUp/setUpClass方法](./docs/setupclass.md)


## 感谢

感谢从以下项目中得到思路和帮助。

* [HTMLTestRunner_cn](https://github.com/GoverSky/HTMLTestRunner_cn)

* [parameterized](https://github.com/wolever/parameterized)

* [pyderman](https://github.com/shadowmoose/pyderman)

* [utx](https://github.com/jianbing/utx)

## 交流

QQ群：948994709
