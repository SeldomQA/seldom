# 创建项目

seldom已经安装完成，那么现在已经迫不及待的想体验seldom的使用。

### 自动生成项目

seldom 通过`seldom`命令提供了脚手架，可以快速的帮我们创建自动化测试项目。

1. 查看帮助：

```shell
> seldom --help
Usage: seldom [OPTIONS]

  seldom CLI.

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v                 Show version.                                           │
│ --project-api         -api      TEXT     Create a project of API type. [default: None]           │
│ --project-app         -app      TEXT     Create a project of App type [default: None]            │
│ --project-web         -web      TEXT     Create a project of Web type [default: None]            │
│ --clear-cache         -cc                Clear all caches of seldom.                             │
│ --log-level           -ll       TEXT     Set the log level [TRACE |DEBUG | INFO | SUCCESS |      │
│                                          WARNING | ERROR].                                       │
│                                          [default: None]                                         │
│ --mod                 -m        TEXT     Run tests modules, classes or even individual test      │
│                                          methods from the command line.                          │
│                                          [default: None]                                         │
│ --path                -p        TEXT     Run test case file path. [default: None]                │
│ --env                 -e        TEXT     Set the Seldom run environment `Seldom.env`.            │
│                                          [default: None]                                         │
│ --browser             -b        TEXT     The browser that runs the Web UI automation tests       │
│                                          [chrome | edge | firefox | chromium]. Need the --path.  │
│                                          [default: None]                                         │
│ --base-url            -u        TEXT     The base-url that runs the HTTP automation tests. Need  │
│                                          the --path.                                             │
│                                          [default: None]                                         │
│ --debug               -d                 Debug mode. Need the --path/--mod.                      │
│ --rerun               -rr       INTEGER  The number of times a use case failed to run again.     │
│                                          Need the --path.                                        │
│                                          [default: 0]                                            │
│ --report              -r        TEXT     Set the test report for output. Need the --path.        │
│                                          [default: None]                                         │
│ --collect             -c                 Collect project test cases. Need the --path.            │
│ --level               -l        TEXT     Parse the level of use cases [data | case]. Need the    │
│                                          --path.                                                 │
│                                          [default: data]                                         │
│ --case-json           -j        TEXT     Test case files. Need the --path. [default: None]       │
│ --har2case            -h2c      TEXT     HAR file converts an seldom test case. [default: None]  │
│ --swagger2case        -s2c      TEXT     Swagger file converts an seldom test case.              │
│                                          [default: None]                                         │
│ --api-excel                     TEXT     Run the api test cases in the excel file.               │
│                                          [default: None]                                         │
│ --install-completion                     Install completion for the current shell.               │
│ --show-completion                        Show completion for the current shell, to copy it or    │
│                                          customize the installation.                             │
│ --help                                   Show this message and exit.                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```

2. 创建项目：

```shell
> seldom -api mypro  # API automation test project.
> seldom -app mypro  # or App automation test project.
> seldom -web mypro  # or Web automation test project.
```

目录结构如下：

```shell
mypro/
├── test_dir/
│   ├── __init__.py
│   ├── test_sample.py
├── test_data/
│   ├── data.json
├── reports/
├── confrun.py
└── run.py
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

根据自己的需求编写`Web UI`、`App UI`或`HTTP接口`自动化测试。
