# 创建项目

seldom已经安装完成，那么现在已经迫不及待的想体验seldom的使用。


### 自动生成项目

seldom 通过`seldom`命令提供了脚手架，可以快速的帮我们创建自动化测试项目。

1. 查看帮助：

```shell
> seldom --help
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

2. 创建项目：

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
* `confrun.py` 运行测试用例配置文件。

3. 克隆项目

如果无法使用`seldom`命令，可以通过git克隆相关项目进行学习。


* seldom-web-testing

```shell
> git clone https://github.com/SeldomQA/seldom-web-testing
```

* seldom-api-testing

```shell
> git clone https://github.com/defnngj/seldom-api-testing
```


### 创建测试用例

根据上面的创建的项目，可以在`test_dir`目录下继续创建测试用例：`test_sample.py`。

```py
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        ...


if __name__ == '__main__':
    seldom.main()
```

根据自己的需求编写`Web UI` or`HTTP接口`自动化测试。
