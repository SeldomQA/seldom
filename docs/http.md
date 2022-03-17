## HTTP接口测试

## 前言

HTTP接口测试很简单，不管工具、框架、还是平台，只要很的好的几个点就是好工具。

1. 测试数据问题：比如删除接口，重复执行还能保持结果一致，必定要做数据初始化。
2. 接口依赖问题：B接口依赖A的返回值，C接口依赖B接口的返回值。
3. 加密问题：不同的接口加密规则不一样。有些用到时间戳、md5、base64、AES，如何提供种能力。
4. 断言问题：有些接口返回的结构体很复杂，如何灵活的做到断言。

对于以上问题，工具和平台要么不支持，要么很麻烦，然而框架是最灵活的。 

> unittest/pytest + requests/https 直接上手写代码就好了，既简单又灵活。

那么同样是写代码，A框架需要10行，B框架只需要5行，然而又不失灵活性，那我当然是选择更少的了，毕竟，人生苦短嘛。

seldom适合个人接口自动化项目，它有以下优势。

* 可以写更少的代码
* 自动生成HTML/XML测试报告
* 支持参数化，减少重复的代码
* 支持生成随机数据
* 支持har文件转case
* 支持数据库操作

这些是seldom支持的功能，我们只需要集成HTTP接口库，并提供强大的断言即可。`seldom 2.0` 加入了HTTP接口自动化测试支持。

Seldom 兼容 [Requests](https://docs.python-requests.org/en/master/) API 如下:

|  seldom   | requests  |
|  ----  | ----  |
| self.get()  | requests.get() |
| self.post()  | requests.post() |
| self.put()  | requests.put() |
| self.delete()  | requests.delete() |

### Seldom VS Request+unittest

先来看看unittest + requests是如何来做接口自动化的：

```python
import unittest
import requests


class TestAPI(unittest.TestCase):

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get("http://httpbin.org/get", params=payload)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
```

这其实已经非常简洁了。同样的用例，用seldom实现。

```python
# test_req.py
import seldom


class TestAPI(seldom.TestCase):

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("http://httpbin.org/get", params=payload)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main()
```

主要简化点在，接口的返回数据的处理。当然，seldom真正的优势在断言、日志和报告。

### har to case

对于不熟悉 Requests 库的人来说，通过Seldom来写接口测试用例还是会有一点难度。于是，seldom提供了`har` 文件转 `case` 的命令。

首先，打开fiddler 工具进行抓包，选中某一个请求。

然后，选择菜单栏：`file` -> `Export Sessions` -> `Selected Sessions...`

![](./image/fiddler.png)

选择导出的文件格式。

![](./image/fiddler2.png)

点击`next` 保存为`demo.har` 文件。

最后，通过`seldom -h2c` 转为`demo.py` 脚本文件。

```shell
> seldom -h2c .\demo.har
.\demo.py
2021-06-14 18:05:50 [INFO] Start to generate testcase.
2021-06-14 18:05:50 [INFO] created file: D:\.\demo.py
```

`demo.py` 文件。

```python
import seldom


class TestRequest(seldom.TestCase):

    def start(self):
        self.url = "http://httpbin.org/post"

    def test_case(self):
        headers = {"User-Agent": "python-requests/2.25.0", "Accept-Encoding": "gzip, deflate", "Accept": "application/json", "Connection": "keep-alive", "Host": "httpbin.org", "Content-Length": "36", "Origin": "http://httpbin.org", "Content-Type": "application/json", "Cookie": "lang=zh"}
        cookies = {"lang": "zh"}
        self.post(self.url, json={"key1": "value1", "key2": "value2"}, headers=headers, cookies=cookies)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main()

```

### 运行测试

打开debug模式`seldom.run(debug=True)` 运行上面的用例。

```shell
> python .\test_req.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.5.1
-----------------------------------------
                             @itest.info

.\test_req_2.py
test_case (test_req_2.TestRequest) ... 
2022-02-19 00:52:13 [INFO] -------------- Request -----------------[🚀]
2022-02-19 00:52:13 [DEBUG] [method]: POST      [url]: http://httpbin.org/post

2022-02-19 00:52:13 [DEBUG] [headers]:
 {'User-Agent': 'python-requests/2.25.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Host': 'httpbin.org', 'Content-Length': '36', 'Origin': 'http://httpbin.org', 'Content-Type': 'application/json', 'Cookie': 'lang=zh'}

2022-02-19 00:52:13 [DEBUG] [cookies]:
 {'lang': 'zh'}

2022-02-19 00:52:13 [DEBUG] [json]:
 {'key1': 'value1', 'key2': 'value2'}

2022-02-19 00:52:13 [INFO] -------------- Response ----------------[🛬️]
2022-02-19 00:52:13 [DEBUG] [type]: json

2022-02-19 00:52:13 [DEBUG] [response]:
 {'args': {}, 'data': '{"key1": "value1", "key2": "value2"}', 'files': {}, 'form': {}, 'headers': {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '36', 'Content-Type': 'application/json', 'Cookie': 'lang=zh', 'Host': 'httpbin.org', 'Origin': 'http://httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-620fcebc-78fd3200528941ab13f942f9'}, 'json': {'key1': 'value1', 'key2': 'value2'}, 'origin': '173.248.248.93', 'url': 'http://httpbin.org/post'}

ok

----------------------------------------------------------------------
Ran 1 test in 0.789s

OK
2022-02-19 00:52:13 [PRINT] A run the test in debug mode without generating HTML report!
```

通过日志/报告都可以清楚的看到。

* 请求的方法
* 请求url
* 响应的类型
* 响应的数据

### 更强大的断言

断言接口返回的数据是我们在做接口自动化很重要的工作。

__assertJSON__


接口返回结果如下：

```json
{
  "args": {
    "hobby": [
      "basketball",
      "swim"
    ],
    "name": "tom"
  }
}
```

我的目标是断言`name` 和 `hobby` 部分的内容。seldom可以针对`JSON`文件进行断言。

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_assert_json(self):
        payload = {'name': 'tom', 'hobby': ['basketball', 'swim']}
        self.get("http://httpbin.org/get", params=payload)
        assert_json = {'args': {'hobby': ['swim', 'basketball'], 'name': 'tom'}}
        self.assertJSON(assert_json)
```

运行日志

```shell

2022-02-19 00:59:28 [INFO] -------------- Request -----------------[🚀]
2022-02-19 00:59:28 [DEBUG] [method]: GET      [url]: http://httpbin.org/get

2022-02-19 00:59:28 [DEBUG] [params]:
 {'name': 'tom', 'hobby': ['basketball', 'swim']}

2022-02-19 00:59:28 [INFO] -------------- Response ----------------[🛬️]
2022-02-19 00:59:28 [DEBUG] [type]: json

2022-02-19 00:59:28 [DEBUG] [response]:
 {'args': {'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-620fd06f-23a6d1231cb1b7aa7e34a211'}, 'origin': '173.248.248.93', 'url': 'http://httpbin.org/get?name=tom&hobby=basketball&hobby=swim'}

💡 Assert data has not key: headers
💡 Assert data has not key: origin
💡 Assert data has not key: url
ok

----------------------------------------------------------------------
Ran 1 test in 0.626s

OK
2022-02-19 00:59:28 [PRINT] A run the test in debug mode without generating HTML report!
```

seldom还会提示你还有哪些字段没有断言。


__assertPath__

`assertPath` 是基于 `jmespath` 实现的断言，功能非常强大。

jmespath:https://jmespath.org/specification.html

接口返回数据如下：

```json
{
  "args": {
    "hobby": 
      ["basketball", "swim"], 
    "name": "tom"
  }
}
```

seldom中可以通过path进行断言：

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_assert_path(self):
        payload = {'name': 'tom', 'hobby': ['basketball', 'swim']}
        self.get("http://httpbin.org/get", params=payload)
        self.assertPath("name", "tom")
        self.assertPath("args.hobby[0]", "basketball")

```


__assertSchema__

有时并不关心数据本身是什么，而是需要断言数据的类型。 `assertSchema` 是基于 `jsonschema` 实现的断言方法。

jsonschema: https://json-schema.org/learn/

接口返回数据如下：

```json
{
  "args": {
    "hobby": 
      ["basketball", "swim"], 
    "name": "tom", 
    "age": "18"
  }
}
```

seldom中可以通过利用`jsonschema` 进行断言：

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_assert_schema(self):
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("/get", params=payload)
        schema = {
            "type": "object",
            "properties": {
                "args": {
                    "type": "object",
                    "properties": {
                        "age": {"type": "string"},
                        "name": {"type": "string"},
                        "hobby": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                        }
                    }
                }
            },
        }
        self.assertSchema(schema)
```

是否再次感受到了seldom提供的断言非常灵活，强大。


### 接口数据依赖

在场景测试中，我们需要利用上一个接口的数据，调用下一个接口。

* 简单的接口依赖

```python
import seldom

class TestRespData(seldom.TestCase):

    def test_data_dependency(self):
        """
        Test for interface data dependencies
        """
        headers = {"X-Account-Fullname": "bugmaster"}
        self.get("/get", headers=headers)
        self.assertStatusCode(200)

        username = self.response["headers"]["X-Account-Fullname"]
        self.post("/post", data={'username': username})
        self.assertStatusCode(200)
```

seldom提供了`self.response`用于记录上个接口返回的结果，直接拿来用即可。

* 封装接口依赖

创建公共模块

```python
# common.py
from seldom import HttpRequest


class Common(HttpRequest):

    def get_login_user(self):
        """
        调用接口获得用户名
        """
        headers = {"X-Account-Fullname": "bugmaster"}
        self.get("http://httpbin.org/get", headers=headers)
        user = self.response["headers"]["X-Account-Fullname"]
        return user

```

> 创建类直接继承 `HttpRequest` 类调用使用Http请求方法`get/post/put/delete` .

引用公共模块

```python
import seldom
from common import Common


class TestRequest(seldom.TestCase):

    def start(self):
        self.c = Common()

    def test_case(self):
        # 调用 get_login_user() 获取
        user = self.c.get_login_user()
        print(user)
        self.post("http://httpbin.org/post", data={'username': user})
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

```


### 数据驱动

seldom本来就提供的有强大的数据驱动，拿来做接口测试非常方便。

__@data__

```python
import seldom
from seldom import data


class TestDDT(seldom.TestCase):

    @data([
        ("key1", 'value1'),
        ("key2", 'value2'),
        ("key3", 'value3')
    ])
    def test_data(self, key, value):
        """
        Data-Driver Tests
        """
        payload = {key: value}
        self.post("/post", data=payload)
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"][key], value)

```

__@file_data__

创建`data.json`数据文件

```json
{
 "login":  [
    ["admin", "admin123"],
    ["guest", "guest123"]
 ]
}
```

通过`file_data`实现数据驱动。

```python
import seldom
from seldom import file_data


class TestDDT(seldom.TestCase):

    @file_data("data.json", key="login")
    def test_data(self, username, password):
        """
        Data-Driver Tests
        """
        payload = {username: password}
        self.post("http://httpbin.org/post", data=payload)
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"][username], password)

```

更多数据文件(csv/excel/yaml)，[参考](https://github.com/SeldomQA/seldom/blob/master/docs/advanced.md)

### Session使用

在实际测试过程中，大部分接口需要登录，`Session` 是一种非常简单记录登录状态的方式。

```python
import seldom


class TestCase(seldom.TestCase):

    def start(self):
        self.s = self.Session()
        self.s.get('/cookies/set/sessioncookie/123456789')

    def test_get_cookie1(self):
        self.s.get('/cookies')

    def test_get_cookie2(self):
        self.s.get('/cookies')


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
```

用法非常简单，你只需要在每个接口之前调用一次`登录`， `self.s`对象就记录下了登录状态，通过`self.s` 再去调用其他接口就不需要登录。

### 随机生成测试数据

seldom提供随机生成测试数据方法，可以生成一些常用的数据。

```python
import seldom
from seldom import testdata


class TestAPI(seldom.TestCase):

    def test_data(self):
        phone = testdata.get_phone()
        payload = {'phone': phone}
        self.get("http://httpbin.org/get", params=payload)
        self.assertPath("args.phone", phone)

```

更过类型的测试数据，[参考](https://github.com/SeldomQA/seldom/blob/master/docs/advanced.md)

