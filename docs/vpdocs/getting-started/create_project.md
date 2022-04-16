# 创建项目

seldom已经安装完成，那么现在已经迫不及待的想体验seldom的使用。

### 创建用例

创建一个python文件`test_sample.py`。

```py
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

seldom提供的有命令，可以快速的帮助我们创建。

### 自动生成项目

seldom 通过`seldom`命令提供了脚手架，可以快速的帮我们创建Web UI自动化项目。

1、查看帮助：

```shell
> seldom -h
usage: seldom [-h] [-v] [-project PROJECT] [-r R] [-m M] [-install INSTALL]

WebUI automation testing framework based on Selenium.

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show version
  -project PROJECT  Create an Seldom automation test project.
  -h2c H2C          HAR file converts an interface test case.
  -r R              run test case
  -m M              run tests modules, classes or even individual test methods
                    from the command line
  -install INSTALL  Install the browser driver, For example, 'chrome',
                    'firefox'.
```

2、创建项目：

```shell
> seldom -project mypro
```

目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── test_web_sample.py
│   ├── test_api_sample.py
├── test_data/
│   ├── data.json
├── reports/
└── run.py
```

* `test_dir/` 测试用例目录。
* `test_data/` 测试数据文件目录。
* `reports/` 测试报告目录。
* `run.py` 运行测试用例主文件。
