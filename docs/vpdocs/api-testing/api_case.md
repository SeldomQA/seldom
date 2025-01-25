# 支持Excel测试用例

> seldom > 3.8.0

在编写接口测试用例的时候，有时候测试用例非常简单，比如单接口的测试，不需要登录token，不存在用例数据依赖，也不需要参数加密，此时，使用`Excel`
文件编写用例更为高效。

seldom支持了这种用例的编写。

### 编写Excel用例

[查看例子](https://github.com/SeldomQA/seldom/tree/master/api_case)

首先，创建一个Excel文件，格式如下。

| name            | api   | method | headers | param_type | params | assert | exclude |
|-----------------|-------|--------|---------|------------|--------|--------|---------|
| 简单GET接口         | /get  | GET    | {}      | data       | {}     | {}     | []      |
| 简单POST接口-json参数 | /post | POST   | {}      | json       | {}     | {}     | []      |
| ...             |       |        |         |            |        |        |         |

__参数说明__

| 字段           | 说明                                                    | 列子                                                   | 
|--------------|-------------------------------------------------------|------------------------------------------------------|
| `name`       | 用例的名称，会在测试报告中展示。                                      |                                                      | 
| `api`        | 接口的地址，可以写完整的URL地址, 也可以只定义路径，`base_url` 在 `confrun.py` | 例如：`http://www.httpbin.org/get` or `/get`            |
| `method`     | 接口的请求方法，必须大写，不允许为空                                    | 支持：`GET`、`POST`、`PUT`、`DELETE`                       |
| `headers`    | 请求头，不允许为空，默认为 `{}`，字段必须双引号`"`。                        | 例如：`{"user-agent": "my-app/0.0.1"}`                  |
| `param_type` | 接口参数类型，必须小写，不允许为空。                                    | 例如：`data`、 `json`                                    |
| `params`     | 接口参数，不允许为空，默认为 `{}`，字段必须双引号`"`。                       | 例如：`{"id": 1, "name": "jack"}`                       |
| `assert`     | 断言接口返回，允许为空 或 `{}`，                                   | 例如：`{"status": 200, "success": True, "data": [...]}` |
| `exclude`    | 断言过滤字段，一些特殊的字段会导致断言失败，需要过滤掉。                          | 例如：`["X-Amzn-Trace-Id", "timestamp"]`                |

__confrun.py配置__

```python

def base_url():
    """
    http test
    api base url
    """
    return "http://www.httpbin.org"


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
    return "d://mypro/result.html" or "d://mypro/result.xml"
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
    return "seldom 执行 excel 接口用例"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "api"]


def language():
    """
    setting report language
    return "en" or "zh-CN"
    """
    return "zh-CN"


def failfast():
    """
    fail fast
    :return:
    """
    return False
```

### 运行测试用例

* 目录结构

```shell
mypro/
├── api_case.xlsx
└── confrun.py
```

* 运行测试

```shell
> cd mypro
> seldom --api-excel api_case.xlsx
```

* 运行日志

```shell

 seldom --api-excel .\api_case.xlsx
run .\api_case.xlsx file.

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info

2024-07-06 21:00:35 | INFO     | runner.py | TestLoader: ...\Lib\site-packages\seldom\file_runner\api_excel.py
2024-07-06 21:00:35 | INFO     | parameterization.py | find data file: .\api_case.xlsx

XTestRunner Running tests...

----------------------------------------------------------------------
2024-07-06 21:00:35 | INFO     | api_excel.py | execute api case: [简单GET接口]
2024-07-06 21:00:35 | INFO     | request.py | -------------- Request -----------------[🚀]
2024-07-06 21:00:35 | INFO     | request.py | [method]: GET      [url]: http://www.httpbin.org/get
2024-07-06 21:00:35 | DEBUG    | request.py | [headers]:
{
  "user-agent": "my-app/0.0.1"
}
2024-07-06 21:00:35 | DEBUG    | request.py | [params]:
{
  "key": "value"
}
2024-07-06 21:00:35 | INFO     | request.py | -------------- Response ----------------[🛬️]
2024-07-06 21:00:35 | INFO     | request.py | successful with status 200
2024-07-06 21:00:35 | DEBUG    | request.py | [type]: json      [time]: 0.481752
2024-07-06 21:00:35 | DEBUG    | request.py | [response]:
 {
  "args": {
    "key": "value"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.httpbin.org",
    "User-Agent": "my-app/0.0.1",
    "X-Amzn-Trace-Id": "Root=1-66893ff2-60ed7c5378ca01452917ea0c"
  },
  "origin": "14.155.89.115",
  "url": "http://www.httpbin.org/get?key=value"
}
2024-07-06 21:00:35 | INFO     | case.py | 👀 assertJSON -> {'args': {'key': 'value'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'www.httpbin.org', 'User-Agent': 'my-app/0.0.1', 'X-Amzn-Trace-Id': 'Root=1-668906ef-2e2d8c4c3f36a228264da1ab'}, 'origin': '14.155.89.115', 'url': 'http://www.httpbin.org/get?key=value'}.

...

```

* 生成测试报告

![](/image/api_excel_report.png)
