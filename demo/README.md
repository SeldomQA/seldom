## seldom demo

通过 demo 帮助你快速了解seldom的使用。

### 准备工作

* 目录树：

```shell
./demo
├── README.md
├── __init__.py
├── confrun.py  # 运行配置钩子函数
├── reports     # 测试报告
├── test_data   # 测试数据
└── test_dir    # 测试用例
    ├── __init__.py
    ├── api_case  # http接口用例
    ├── app_case  # app UI 自动化用例
    └── web_case  # web UI 自动化用例
```

* 请安装 seldom 最新版本。

```shell
> pip install -U seldom
```

* 确保 seldom 命令可用。

```shell
> seldom --version                 
seldom, version 3.1.1
```

### 使用方法

seldom 从 3.1 开始支持 `confrun.py` 配置运行钩子函数，并推荐你使用这种方式。

| 函数         | 类型      | 说明                                                        |
|-------------|---------|-----------------------------------------------------------|
| start_run() | fixture | 运行测试之前执行                                                  |
| end_run()   | fixture | 运行测试之后执行                                                  |
| browser()   | web     | 设置浏览器类型：gc(google chrome)/ff(firefox)/edge/ie/safari      |
| base_url()  | api     | 设置http接口基本url: 例如 http://httpbin.org                      |
| app_info()  | app     | 基于appium，启动app信息                                          |
| app_server()  | app     | 基于appium，设置appium 服务地址+端口                             |
| debug()  | general     | 是否开启debug模式：True/False                                    |
| rerun()  | general     | 用例失败/错误重跑，默认：0                                            |
| report()  | general     | 指定报告生成地址，例如： `/User/tech/xxx.html`、  `/User/tech/xxx.xml` |
| timeout()  | general     | 全局运行超时时间，默认：10                                            |
| title()  | general     | 测试报告标题：html报告                                             |
| tester()  | general     | 测试人员名字：html报告                                            |
| description()  | general     | 测试报告描述：html报告                                       |
| language()  | general     | 测试报告语言：html报告，类型： `en`、`zh-CN`                     |
| whitelist()  | general     | 运行用例白名单                                                |
| blacklist()  | general     | 运行用例黑名单                                                |


__特殊配置__

特殊配置是针对不同的测试类型设置的配置。

* web UI 自动化配置

```python
# confrun.py

def browser():
    """
    Web UI test:
    browser: gc(google chrome)/ff(firefox)/edge/ie/safari
    """
    return "gc"
```

运行测试：

```shell
> seldom --path test_dir/web_case/
> seldom --path test_dir/web_case/test_playwright_demo.py
```

* http 接口测试

```python
# confrun.py

def base_url():
    """
    http test
    api base url
    """
    return "http://httpbin.org"
```

运行测试：

```shell
> seldom --path test_dir/web_case/
```

* app UI 自动化测试

```python
# confrun.py

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
```

运行测试：

```shell
> seldom --path test_dir/app_case/
```

__通用配置__

通用配置是不管运行什么类型的测试都适用的配置。

```python
# confrun.py

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

