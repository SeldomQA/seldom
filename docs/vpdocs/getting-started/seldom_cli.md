# seldom CLI

`seldom 2.10.7` 对命令行工具做了增强，可以使用命令行的方式运行用例。

## seldom 帮助

* `seldom --help` 查看帮助使用

```shell
> seldom --help
Usage: seldom [OPTIONS]

  seldom CLI.

Options:
  --version                       Show version.
  -P, --project TEXT              Create an Seldom automation test project.
  -cc, --clear-cache BOOLEAN      Clear all caches of seldom.
  -p, --path TEXT                 Run test case file path.
  -c, --collect BOOLEAN           Collect project test cases. Need the
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
  -d, --debug BOOLEAN             Debug mode. Need the `--path`.
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

如果无法使用`seldom` 命令。

1. 请确保你已经安装了seldom

```shell
> pip install seldom
```

2. 如果仍然无法使用`seldom`命令，请用`where`检查安装位置。

```shell
> where seldom
C:\Python38\Scripts\seldom.exe
```

## seldom 使用

### 创建项目

-  `-P/--project`

```shell
> seldom -P mypro
2022-09-03 11:22:25 cli.py | INFO | Start to create new test project: mypro
2022-09-03 11:22:25 cli.py | INFO | CWD: D:\github\seldom

2022-09-03 11:22:25 cli.py | INFO | created folder: mypro
2022-09-03 11:22:25 cli.py | INFO | created folder: mypro\test_dir
2022-09-03 11:22:25 cli.py | INFO | created folder: mypro\reports
2022-09-03 11:22:25 cli.py | INFO | created folder: mypro\test_data
2022-09-03 11:22:25 cli.py | INFO | created file: mypro\test_data\data.json
2022-09-03 11:22:25 cli.py | INFO | created file: mypro\test_dir\test_web_sample.py
2022-09-03 11:22:25 cli.py | INFO | created file: mypro\test_dir\test_api_sample.py
2022-09-03 11:22:25 cli.py | INFO | created file: mypro\run.py
```

### 安装浏览器驱动

* `-i/--install`

```shell
> seldom -i chrome

2022-09-03 11:25:55 cli.py | INFO | Chrome Driver[==>] C:\Users\fnngj\.wdm\drivers\chromedriver\win32\104.0.5112\chromedriver.exe
```

支持`[chrome|firefox|ie|edge]`等浏览器驱动安装。

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
> seldom -m test_first_demo            # 文件名，不要.py后缀
> seldom -m test_first_demo.BingTest   # 文件名.类名
> seldom -m test_first_demo.BingTest.test_case  # 文件名.类名.方法名
```

### 调试模式

* ` -d, --debug/ -nd, --no-debug`

```shell
> seldom -p test_first_demo.py -d   # 开启debug模式
> seldom -p test_first_demo.py -nd   # 关闭debug模式
```

### 运行浏览器

* `-b/--browser`

```shell
> seldom -p test_first_demo.py -b firefox  # firefox浏览器
```

> 支持`[chrome|firefox|ie|edge]` 浏览器。

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
  - `-c, --collect / -nc, --no-collect`: 是否收集用例, 默认`false`。
  - `-l/--level`: 是否收集用例级别: `data/method`。
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
> seldom --clear-cache true
```

* 说明：默认清空seldom所有缓存，即`cache.clear()`