# 更多功能

### har to case

对于不熟悉 Requests 库的人来说，通过Seldom来写接口测试用例还是会有一点难度。于是，seldom提供了`har` 文件转 `case` 的命令。

首先，打开fiddler 工具进行抓包，选中某一个请求。

然后，选择菜单栏：`file` -> `Export Sessions` -> `Selected Sessions...`

![](/image/fiddler.png)

选择导出的文件格式。

![](/image/fiddler2.png)

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

## 请求转 cURL

seldom 支持将请求转成`cCURL`命令， 你可以方便的通过`cURL`命令执行，或者导入到其他接口工具，例如，postman 支持`cURL`命令导入。

```python
# test_http.py
import seldom


class TestRequest(seldom.TestCase):
    """
    http api test demo
    doc: https://requests.readthedocs.io/en/master/
    """

    def test_get_curl(self):
        """
        test get curl
        """
        self.get('http://httpbin.org/get', params={'key': 'value'})
        curl = self.curl()
        print(curl)
        self.post('http://httpbin.org/post', data={'key': 'value'})
        curl = self.curl()
        print(curl)

        # or
        r = self.delete('http://httpbin.org/delete', params={'key': 'value'})
        curl = self.curl(r.request)
        print(curl)
        r = self.put('http://httpbin.org/put', json={'key': 'value'}, headers={"token": "123"})
        curl = self.curl(r.request)
        print(curl)


if __name__ == '__main__':
    seldom.main(debug=True)
```

* 日志结果

```shell
> python test_http.py

...
curl -X GET  'Content-Type: application/json'  -H 'token: 123' -d '{"key": "value"}' http://httpbin.org/get

curl -X POST  'Content-Type: application/x-www-form-urlencoded' -H  -d key=value http://httpbin.org/post

curl -X DELETE  'http://httpbin.org/delete?key=value'

curl -X PUT  -H 'Content-Type: application/json' -H 'token: 123' -d '{"key": "value"}' http://httpbin.org/put
```

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

1. 创建公共模块

```python
# common.py
from seldom.request import check_response 
from seldom.request import HttpRequest


class Common(HttpRequest):
    
    @check_response("获取登录用户名", 200, "headers.Account", {"headers.Host": "httpbin.org"}, debug=True)
    def get_login_user(self):
        """
        调用接口获得用户名
        """
        headers = {"Account": "bugmaster"}
        r = self.get("http://httpbin.org/get", headers=headers)
        return r


if __name__ == '__main__':
    c = Common()
    c.get_login_user()
```

* 运行日志

```shell
2022-04-24 22:21:38 [DEBUG] Execute get_login_user - args: (<__main__.Common object at 0x000001A6B028F970>,)
2022-04-24 22:21:38 [DEBUG] Execute get_login_user - kwargs: {}
2022-04-24 22:21:38.831 | DEBUG    | seldom.logging.log:debug:34 - Execute get_login_user - args: (<__main__.Common object at 0x000001A6B028F970>,)
2022-04-24 22:21:38.832 | DEBUG    | seldom.logging.log:debug:34 - Execute get_login_user - kwargs: {}
2022-04-24 22:21:39 [DEBUG] Execute get_login_user - response:
 {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Account': 'bugmaster', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-62655cf3-18c082b413a51b840fa9a449'}, 'origin': '173.248.248.88', 'url': 'http://httpbin.org/get'}
2022-04-24 22:21:39 [INFO] Execute get_login_user - 用户登录 success!
2022-04-24 22:21:39.402 | DEBUG    | seldom.logging.log:debug:34 - Execute get_login_user - response:
 {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Account': 'bugmaster', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-62655cf3-18c082b413a51b840fa9a449'}, 'origin': '173.248.248.88', 'url': 'http://httpbin.org/get'}
2022-04-24 22:21:39.402 | INFO     | seldom.logging.log:info:45 - Execute get_login_user - 用户登录 success!
```

* check_response

`@check_response` 专门用于处理封装的方法。__参数说明：__

* `describe` : 封装方法描述。
* `status_code`: 判断接口返回的 HTTP 状态码，默认`200`。
* `ret`: 提取接口返回的字段，参考`jmespath` 提取规则。
* `check`: 检查接口返回的字段。参考`jmespath` 提取规则。
* `debug`: 开启`debug`，打印更多信息。


2. 引用公共模块

```python
import seldom
from common import Common


class TestRequest(seldom.TestCase):

    def start(self):
        self.c = Common()

    def test_case(self):
        # 调用 get_login_user() 获取
        user = self.c.get_login_user()
        self.post("http://httpbin.org/post", data={'username': user})
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)

```

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


### 提取接口返回数据

当接口返回的数据比较复杂时，我们需要有更方便方式去提取数据，seldom提供 `jmespath`、`jsonpath` 来简化数据提取。

* 接口返回数据

```json
{
  "args": {
    "hobby": [
      "basketball",
      "swim"
    ],
    "name": "tom"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.25.0",
    "X-Amzn-Trace-Id": "Root=1-62851614-1ca9fdb276238c60406c118f"
  },
  "origin": "113.87.15.99",
  "url": "http://httpbin.org/get?name=tom&hobby=basketball&hobby=swim"
}
```

* 常规提取

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_extract_responses(self):
        """
        提取 response 数据
        """
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("http://httpbin.org/get", params=payload)

        # response
        response1 = self.response["args"]["name"]
        response2 = self.response["args"]["hobby"]
        response3 = self.response["args"]["hobby"][0]
        print(f"response1 --> {response1}")
        print(f"response2 --> {response2}")
        print(f"response3 --> {response3}")

        # jmespath
        jmespath1 = self.jmespath("args.name")
        jmespath2 = self.jmespath("args.hobby")
        jmespath3 = self.jmespath("args.hobby[0]")
        jmespath4 = self.jmespath("hobby[0]", response=self.response["args"])
        print(f"\njmespath1 --> {jmespath1}")
        print(f"jmespath2 --> {jmespath2}")
        print(f"jmespath3 --> {jmespath3}")
        print(f"jmespath4 --> {jmespath4}")

        # jsonpath
        jsonpath1 = self.jsonpath("$..name")
        jsonpath2 = self.jsonpath("$..hobby")
        jsonpath3 = self.jsonpath("$..hobby[0]")
        jsonpath4 = self.jsonpath("$..hobby[0]", index=0)
        jsonpath5 = self.jsonpath("$..hobby[0]", index=0, response=self.response["args"])
        print(f"\njsonpath1 --> {jsonpath1}")
        print(f"jsonpath2 --> {jsonpath2}")
        print(f"jsonpath3 --> {jsonpath3}")
        print(f"jsonpath4 --> {jsonpath4}")
        print(f"jsonpath5 --> {jsonpath5}")
...
```

说明：
* `response`: 保存接口返回的数据，可以直接以，字典列表的方式提取。
* `jmespath()`: 根据 JMESPath 语法规则，默认提取接口返回的数据，也可指定`resposne`数据提取。
* `jsonpath()`: 根据 JsonPath 语法规则，默认提取接口返回的数据, `index`指定下标，也可指定`resposne`数据提取。

运行结果：

```shell
2022-05-19 00:57:08 log.py | DEBUG | [response]:
 {'args': {'age': '18', 'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-62852563-2fe77d4b1ce544696af60f10'}, 'origin': '113.87.15.99', 'url': 'http://httpbin.org/get?hobby=basketball&hobby=swim&name=tom&age=18'}

response1 --> tom
response2 --> ['basketball', 'swim']
response3 --> basketball

jmespath1 --> tom
jmespath2 --> ['basketball', 'swim']
jmespath3 --> basketball
jmespath4 --> basketball

jsonpath1 --> ['tom']
jsonpath2 --> [['basketball', 'swim']]
jsonpath3 --> ['basketball']
jsonpath4 --> basketball
jsonpath5 --> basketball
```

* ~~jresponse()~~ 用法

在接口测试中通过`jresponse()` 方法可以直接提取数据。

> 注：该方法从命名、参数都不规范，不推荐使用，后续版本将会移除。

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_jresponse(self):
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("http://httpbin.org/get", params=payload)
        self.jresponse("$..hobby[0]")  # 提取hobby (默认 jsonpath)
        self.jresponse("$..age")   # 提取age (默认 jsonpath)
        self.jresponse("hobby[0]", j="jmes")  # 提取hobby (jmespath)
        self.jresponse("age", j="jmes")  # 提取age (jmespath)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org", debug=True)
```

运行结果

```shell
...
2022-04-10 21:05:17.683 | DEBUG    | seldom.logging.log:debug:34 - [response]:
 {'args': {'age': '18', 'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-6252d60c-551433d744b6869e5d1944d7'}, 'origin': '113.87.12.14', 'url': 'http://httpbin.org/get?hobby=basketball&hobby=swim&name=tom&age=18'}

2022-04-10 21:05:17.686 | DEBUG    | seldom.logging.log:debug:34 - [jresponse]:
 ['basketball']
2022-04-10 21:05:17.689 | DEBUG    | seldom.logging.log:debug:34 - [jresponse]:
 ['18']
```

### genson

通过 `assertSchema()` 断言时需要写JSON Schema，但是这个写起来需要学习成本，seldom集成了[GenSON](https://github.com/wolverdude/GenSON) ,可以帮你自动生成。

* 例子

```python
import seldom
from seldom.utils import genson


class TestAPI(seldom.TestCase):

    def test_assert_schema(self):
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("/get", params=payload)
        print("response \n", self.response)
        
        schema = genson(self.response)
        print("json Schema \n", schema)
        
        self.assertSchema(schema)
```

* 运行日志

```shell
...
response
 {'args': {'age': '18', 'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-626574d0-4c04bb7e76a53e8042c9d856'}, 'origin': '173.248.248.88', 'url': 'http://httpbin.org/get?hobby=basketball&hobby=swim&name=tom&age=18'}

json Schema
 {'$schema': 'http://json-schema.org/schema#', 'type': 'object', 'properties': {'args': {'type': 'object', 'properties': {'age': {'type': 'string'}, 'hobby': {'type': 'array', 'items': {'type': 'string'}}, 'name': {'type': 'string'}}, 'required': ['age', 'hobby', 'name']}, 'headers': {'type': 'object', 'properties': {'Accept': {'type': 'string'}, 'Accept-Encoding': {'type': 'string'}, 'Host': {'type': 'string'}, 'User-Agent': {'type': 'string'}, 'X-Amzn-Trace-Id': {'type': 'string'}}, 'required': ['Accept', 'Accept-Encoding', 'Host', 'User-Agent', 'X-Amzn-Trace-Id']}, 'origin': {'type': 'string'}, 'url': {'type': 'string'}}, 'required': ['args', 'headers', 'origin', 'url']}
```

