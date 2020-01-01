## seldom 创建项目

seldom已经安装完成，那么现在已经迫不及待的想体验seldom的使用。

### 创建测试文件

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
    seldom.main("test_sample.py")
```

seldom提供的有命令，可以快速的帮助我们创建。

### 快速生成自动化项目

seldom 通过`seldom`命令提供了脚手架，可以快速的帮我们创建Web UI自动化项目。

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
> seldom --project mypro
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
