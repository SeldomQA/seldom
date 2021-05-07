## HTTP接口测试

seldom做接口测试有很多优势。

* 支持HTML/XML测试报告
* 支持参数化
* 支持生成随机数据

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


### 运行测试

打开debug模式`seldom.run(debug=True)` 运行上面的用例。

```shell
> python .\test_req.py
2021-04-29 18:19:39 [INFO] A run the test in debug mode without generating HTML report!
2021-04-29 18:19:39 [INFO]
              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/
-----------------------------------------
                             @itest.info

test_get_method (test_req.TestAPI) ...
----------- Request 🚀 ---------------
url: http://httpbin.org/get         method: GET
----------- Response 🛬️ -------------
type: json
{'args': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-608a883c-7b355ba81fcd0d287566405a'}, 'origin': '183.178.27.36', 'url': 'http://httpbin.org/get?key1=value1&key2=value2'}
ok

----------------------------------------------------------------------
Ran 1 test in 0.619s

OK
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
test_get_method (test_req.TestAPI) ...
----------- Request 🚀 ---------------
url: http://httpbin.org/get         method: GET
----------- Response 🛬️ -------------
type: json
{'args': {'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-608a896d-48fac4f6139912ba01d2626f'}, 'origin': '183.178.27.36', 'url': 'http://httpbin.org/get?name=tom&hobby=basketball&hobby=swim'}
💡 Assert data has not key: headers
💡 Assert data has not key: origin
💡 Assert data has not key: url
ok

----------------------------------------------------------------------
Ran 1 test in 1.305s

OK
```

seldom还会提示你还有哪些字段没有断言。


__assertPath__

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

更过数据文件(csv/excel/yaml)，[参考](https://github.com/SeldomQA/seldom/blob/master/docs/advanced.md)

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

