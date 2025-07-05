# seldom CLI

`seldom 2.10.7` 对命令行工具做了增强，可以使用命令行的方式运行用例。

## seldom 帮助

* `seldom --help` 查看帮助使用

```shell
> seldom --help
Usage: seldom [OPTIONS]                                                                                                    
                                                                                                                            
 seldom CLI.                                                                                                                                                                                                                                      
                                                                                                                            
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v                 Show version.                                                                   │
│ --project-api         -api      TEXT     Create a project of API type. [default: None]                                   │
│ --project-app         -app      TEXT     Create a project of App type [default: None]                                    │
│ --project-web         -web      TEXT     Create a project of Web type [default: None]                                    │
│ --clear-cache         -cc                Clear all caches of seldom.                                                     │
│ --log-level           -ll       TEXT     Set the log level [TRACE |DEBUG | INFO | SUCCESS | WARNING | ERROR].            │
│                                          [default: None]                                                                 │
│ --mod                 -m        TEXT     Run tests modules, classes or even individual test methods from the command     │
│                                          line.                                                                           │
│                                          [default: None]                                                                 │
│ --path                -p        TEXT     Run test case file path. [default: None]                                        │
│ --env                 -e        TEXT     Set the Seldom run environment `Seldom.env`. [default: None]                    │
│ --browser             -b        TEXT     The browser that runs the Web UI automation tests [chrome | edge | firefox |    │
│                                          chromium]. Need the --path.                                                     │
│                                          [default: None]                                                                 │
│ --base-url            -u        TEXT     The base-url that runs the HTTP automation tests. Need the --path.              │
│                                          [default: None]                                                                 │
│ --debug               -d                 Debug mode. Need the --path/--mod.                                              │
│ --rerun               -rr       INTEGER  The number of times a use case failed to run again. Need the --path.            │
│                                          [default: 0]                                                                    │
│ --report              -r        TEXT     Set the test report for output. Need the --path. [default: None]                │
│ --collect             -c                 Collect project test cases. Need the --path.                                    │
│ --level               -l        TEXT     Parse the level of use cases [data | case]. Need the --path. [default: data]    │
│ --case-json           -j        TEXT     Test case files. Need the --path. [default: None]                               │
│ --har2case            -h2c      TEXT     HAR file converts an seldom test case. [default: None]                          │
│ --swagger2case        -s2c      TEXT     Swagger file converts an seldom test case. [default: None]                      │
│ --api-excel                     TEXT     Run the api test cases in the excel file. [default: None]                       │
│ --install-completion                     Install completion for the current shell.                                       │
│ --show-completion                        Show completion for the current shell, to copy it or customize the              │
│                                          installation.                                                                   │
│ --help                                   Show this message and exit.                                                     │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

如果无法使用`seldom` 命令。

1. 请确保你已经安装了seldom

```shell
> pip install seldom
```

2. 如果仍然无法使用`seldom`命令，请用`where`检查安装位置。

```shell
> where seldom
C:\Python311\Scripts\seldom.exe
```

## seldom 使用

### 创建项目

- `-P/--project`

```shell
> seldom --project-api myapi  # API automation test project.
> seldom --project-app myapp  # or App automation test project.
> seldom --project-web myweb  # or Web automation test project.
```

### 生成接口自动化用例

* `-h2c/--har2case`

```shell
> seldom -h2c demo.har
2022-09-03 11:29:29 core.py | INFO | demo.py
2022-09-03 11:29:29 core.py | INFO | Start to generate testcase.
2022-09-03 11:29:29 core.py | INFO | created file: D:\github\seldom\seldom\har2case\demo.py
```

注：`har` 是fiddler 抓包工具导出的一种格式，即 `HTTPArchive`。

### 运行测试目录&文件

* `-p\--path`

```shell
> seldom -p ./test_dir/                     # 指定运行目录
> seldom -p ./test_dir/test_first_demo.py   # 指定运行文件
```

不支持斜杠`\`表示路径

### 运行文件&类&方法

* `-m\--mod`

```shell
> seldom -m test_dir                             # 目录名
> seldom -m test_dir.test_sample                 # 目录名.文件名，不要.py后缀
> seldom -m test_dir.test_sample.SampleTest      # 目录名.文件名.类名
> seldom -m test_dir.test_sample.SampleTest.test_case  # 目录名.文件名.类名.方法名
```

### 调试模式

* ` -d, --debug`

```shell
> seldom -p test_sample.py -d   # 开启debug模式（默认不指定-d关闭）
```

### 运行浏览器

* `-b/--browser`

```shell
> seldom -p test_sample.py -b firefox  # firefox浏览器
```

> 支持`[chrome|chrimium|firefox|edge]` 浏览器。

### 运行URL

* `-u/--base-url`

```shell
> seldom -p test_http_demo.py -u http://httpbin.org  # base-url
```

### 测试报告

* `-r/--report`

```shell
> seldom -p test_first_demo.py -r result.html  # HTML报告
> seldom -p test_first_demo.py -r result.xml  # XML报告
```

### 失败/错误重跑次数

* `-rr/--rerun`

```shell
> seldom -p test_first_demo.py -rr 2  # rerun重跑次数
```

### 数据驱动运行环境

* `-e/--env`

```shell
> seldom -p test_ddt_demo.py -e production  # 运行环境
```

> 注：参考`数据驱动` 一章 `Seldom.env` 的用法。

### 收集测试用例

```shell
> seldom -p test_dir -c -l method -j case.json
Collect use cases for the test_dir directory.
add env Path: .

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v{x}.{x}.{x}
-----------------------------------------
                             @itest.info

save them to D:\github\seldom\demo\case.json
```

* 说明：
    - `-p/--path`: 指定收集用例的目录：`test_dir`。
    - `-c, --collect`: 指定收集用例, 默认`False`。
    - `-l/--level`: 指定收集用例级别: `data/method`。
    - `-j/--case-json`: 收集用例保存文件: `case.json`。

### 运行收集测试用例

```shell
> seldom -p test_dir -j case.json -r result.html
```

* 说明：
    - `-p/--path`: 指定运行用例的根目录：`test_dir`。
    - `-j/--case-json`: 运行收集用例文件: `case.json`。
    - `-r/--report`: 运行收集用例生成报告: `result.html`。

### 清除所有缓存

```shell
> seldom --clear-cache
```

* 说明：默认清空seldom所有缓存，即`cache.clear()`

### 执行 API（excel文件）测试用例

```shell
> seldom  --api-excel api_case.xlsx
```

* 说明：简单的HTTP接口测试可以使用excel编写，seldom支持运行excel文件。excel的具体定义可以参考`HTTP接口测试`章节。
