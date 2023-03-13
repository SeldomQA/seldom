# 快速开始

### 基本规范

`seldom`继承`unittest`单元测试框架，所以他的编写规范与[unittest](https://docs.python.org/3/library/unittest.html)基本保持一致。

```shell
# test_sample.py
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    seldom.main()
```

基本规范：

1. 创建测试类`YouTest`并继承`seldom.TestCase`类。
2. 创建测试方法`test_case`, 必须以`test`开头。
3. `seldom.mian()`是框架运行的入口方法，接下来详细介绍。


### `main()` 方法

`main()`方法是seldom运行测试的入口, 它提供了一些最基本也是最重要的配置。

```python
import seldom

# ...

if __name__ == '__main__':

    seldom.main(path="./",
                browser="chrome",
                base_url=None,
                app_info=None,
                app_server=None,
                report=None,
                title="百度测试用例",
                tester="虫师",
                description="测试环境:chrome",
                debug=False,
                rerun=0,
                language="en",
                timeout=10,
                whitelist=[],
                blacklist=[],
                open=True
    )
```

__参数说明__


* path : 指定测试目录或文件， 与`case`参数互斥。
* case : 指定测试用例， 与`path`参数互斥。
* browser : 指定浏览器（"chrome"、"firefox" 等）， Web测试。
* base_url : 设置全局的基本URL， HTTP测试。
* app_info : app 启动信息，参考`desired_capabilities`配置， app测试。
* app_server : appium server 启动地址（默认 http://127.0.0.1:4723）， app测试。
* report : 自定义测试报告的名称，默认格式为`2020_04_04_11_55_20_result.html`。
* title : 指定测试报告标题。
* tester : 指定测试人员, 默认`Anonymous`。
* description : 指定测试报告描述。
* debug : debug模式，设置为True不生成测试HTML测试，默认为`False`。
* rerun : 设置失败重新运行次数，默认为 `0`。
* language : 设置HTML报告中英文，默认`en`, 中文`zh-CN`。
* timeout : 设置超时时间，默认`10`秒。
* whitelist :  用例标签（label）设置白名单。
* blacklist :  用例标签（label）设置黑名单。
* open :  是否使用浏览器自动打开测试报告，默认`True`。


### `confrun.py` 配置文件
> seldom 3.1.0 提供过了 `confrun.py` 用于配置运行环境。

在这个文件中可以定义运行相关的钩子函数。

```py
"""
seldom confrun.py hooks function
"""

def start_run():
    """
    Test the hook function before running
    """
    ...


def end_run():
    """
    Test the hook function after running
    """
    ...


def browser():
    """
    Web UI test:
    browser: gc(google chrome)/ff(firefox)/edge/ie/safari
    """
    return "gc"


def base_url():
    """
    http test
    api base url
    """
    return "http://httpbin.org"


def app_info():
    """
    app UI test
    appium app config
    """
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    return desired_caps


def app_server():
    """
    app UI test
    appium server/desktop address
    """
    return "http://127.0.0.1:4723"

def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html"
    return "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "seldom test report"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "jenkins"]


def language():
    """
    setting report language
    return "en"
    return "zh-CN"
    """
    return "en"


def whitelist():
    """test label white list"""
    return []


def blacklist():
    """test label black list"""
    return []
```

以上配置根据需求自动化项目类型配置，相互可能冲突的钩子函数：

* Web UI测试: `browser()`
* http 接口测试: `base_url()`
* app UI测试: `app_info()`, `app_server()`

### 运行测试

seldom 的运行有三种方式：

* `main()` 方法：在`.py` 文件中使用`seldom.main()` 方法。
* `seldom` 命令：通过`sedom` 命令指定要运行的目录&文件&类&方法。
* ~~`pycharm`右键执行：这种方式无法读取到配置，有严重缺陷。~~

> 强烈建议使用前两种！！

__1. `main()`方法运行测试__

创建 `test_sample.py` 文件，在测试文件中使用`main()`方法，如下：

```py
# test_sample.py
import seldom
from seldom import data


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1+1, 2)

    @data([
        ("case1", "seldom"),
        ("case2", "XTestRunner"),
    ])
    def test_ddt(self, name, search):
        """ ddt case """
        print(f"name: {name}, search_key: {search}")


if __name__ == '__main__':
    # 指定运行其他目录&文件
    seldom.main(path="./")  # 指定当前文件所在目录下面的用例。
    seldom.main(path="./test_dir/")  # 指定当前目录下面的test_dir/ 目录下面的用例。
    seldom.main(path="./test_dir/test_sample.py")  # 指定测试文件中的用例。
    seldom.main(path="D:/seldom_sample/test_dir/test_sample.py")  # 指定文件的绝对路径。
    
    # 运行当前文件中的用例
    seldom.main()  # 默认运行当前文件中所有用例
    seldom.main(case="test_sample")  # 指定当前文件
    seldom.main(case="test_sample.TestCase")  # 指定测试类
    seldom.main(case="test_sample.TestCase.test_case")  # 指定测试用例

    # 使用参数化的用例
    seldom.main(case="test_sample.TestCase.test_ddt")  # 错误用法
    seldom.main(case="test_sample.TestCase.test_ddt_0")  # 正确用法，0表示第一条数据用例
```

`seldom.main()` 提供哪些参数，请参考前面的文档。

* 运行测试文件

```shell
> python test_sample.py      # 通过python命令运行
```

__2. seldom命令执行__

* 目录结构

```
mypro/
├── test_dir/
│   ├── __init__.py
│   ├── test_sample.py
└── confrun.py  # 运行配置文件
```

`seldom -p`命令指定目录和文件。

`seldom -m`命令可以提供更细粒度的运行。

```shell
> cd mypro/  # 进入项目根目录
> seldom -p test_dir  # 运行目录
> seldom -p test_dir/test_sample.py  # 运行文件
> seldom -m test_dir.test_sample       # 运行文件
> seldom -m test_dir.test_sample.SampleTest # 运行 SampleTest 测试类
> seldom -m test_dir.test_sample.SampleTest.test_case # 运行 test_case 测试方法
```

运行相关的配置，可以在`confrun.py` 文件中配置。


__3. 在pyCharm中运行测试__

> 强烈不建议这种方式，除非你的测试用例没有任何依赖。

步骤一：配置测试用例通过 unittest 运行。

![](/image/pycharm.png)

步骤二：在文件中选择测试类或用例执行。

![](/image/pycharm_run_case.png) 

> 警告：运行用例打开的浏览器，需要手动关闭， seldom不做用例关闭操作。


### 失败重跑

Seldom支持`错误`&`失败`重跑。

```python
# test_sample.py
import seldom


class YouTest(seldom.TestCase):

  
    def test_error(self):
        """error case"""
        self.assertEqual(a, 2)

    def test_fail(self):
        """fail case """
        self.assertEqual(1+1, 3)


if __name__ == '__main__':
    seldom.main(rerun=3)
```

参数说明：

* rerun: 指定重跑的次数，默认为 `0`。

运行日志：

```shell
> python test_sample.py


              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info




XTestRunner Running tests...

----------------------------------------------------------------------
ERetesting... test_error (test_sample.YouTest)..1
ERetesting... test_error (test_sample.YouTest)..2
ERetesting... test_error (test_sample.YouTest)..3
EFRetesting... test_fail (test_sample.YouTest)..1
FRetesting... test_fail (test_sample.YouTest)..2
FRetesting... test_fail (test_sample.YouTest)..3
Generating HTML reports...
F2022-07-12 00:22:52 log.py | SUCCESS | generated html file: file:///D:\github\seldom\reports\2022_07_12_00_22_51_result.html
2022-07-12 00:22:52 log.py | SUCCESS | generated log file: file:///D:\github\seldom\reports\seldom_log.log
```

### 测试报告

seldom 默认生成HTML测试报告，在运行测试文件下自动创建`reports`目录。

* 运行测试用例前

```shell
mypro/
└── test_sample.py
```

* 运行测试用例后

```shell
mypro/
├── reports/
│   ├── 2020_01_01_11_20_33_result.html
│   ├── seldom_log.log
└── test_sample.py
```

通过浏览器打开 `2020_01_01_11_20_33_result.html` 测试报告，查看测试结果。

![](/image/report.png)


__debug模式__

如果不想每次运行都生成HTML报告，可以打开`debug`模式。

```py
import seldom

seldom.main(debug=True)
```

__定义测试报告__


```py
import seldom

seldom.main(report="./report.html",
            title="百度测试用例",
            tester="虫师",
            description="测试环境：windows 10/ chrome")
```

* report: 配置报告名称和路径。
* title: 自定义报告的标题。
* tester: 指定自动化测试工程师名字。
* description: 添加报告信息，支持列表, 例如：["OS: windows","Browser: chrome"]。

__XML测试报告__

如果需要生成XML格式的报告，只需要修改报告的后缀名为`.xml`即可。

```py
import seldom

seldom.main(report="report.xml")
```

