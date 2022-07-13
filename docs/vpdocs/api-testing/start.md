# 开始使用

### 前言

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
    seldom.main(debug=True)
```

主要简化点在，接口的返回数据的处理。当然，seldom真正的优势在断言、日志和报告。


### 运行测试

打开debug模式`seldom.run(debug=True)` 运行上面的用例。

```shell

> python .\test_req.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.x.x
-----------------------------------------
                             @itest.info

.\test_req.py
test_case (test_req.TestRequest) ... 
2022-04-30 18:20:47 log.py | INFO | -------------- Request -----------------[🚀]
2022-04-30 18:20:47 log.py | INFO | [method]: POST      [url]: http://httpbin.org/post

2022-04-30 18:20:47 log.py | DEBUG | [headers]:
 {'User-Agent': 'python-requests/2.25.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': 'application/json', 'Connection': 'keep-alive', 'Host': 'httpbin.org', 'Content-Length': '36', 'Origin': 'http://httpbin.org', 'Content-Type': 'application/json', 'Cookie': 'lang=zh'}

2022-04-30 18:20:47 log.py | DEBUG | [cookies]:
 {'lang': 'zh'}

2022-04-30 18:20:47 log.py | DEBUG | [json]:
 {'key1': 'value1', 'key2': 'value2'}

2022-04-30 18:20:47 log.py | INFO | -------------- Response ----------------[🛬️]
2022-04-30 18:20:47 log.py | INFO | successful with status 200

2022-04-30 18:20:47 log.py | DEBUG | [type]: json      [time]: 0.582786

2022-04-30 18:20:47 log.py | DEBUG | [response]:
 {'args': {}, 'data': '{"key1": "value1", "key2": "value2"}', 'files': {}, 'form': {}, 'headers': {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '36', 'Content-Type': 'application/json', 'Cookie': 'lang=zh', 'Host': 'httpbin.org', 'Origin': 'http://httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-626d0d7e-69a616b20139cd6869cc5e90'}, 'json': {'key1': 'value1', 'key2': 'value2'}, 'origin': '173.248.248.88', 'url': 'http://httpbin.org/post'}

ok

----------------------------------------------------------------------
Ran 1 test in 0.594s

OK
2022-04-30 18:20:47 log.py | SUCCESS | A run the test in debug mode without generating HTML report!
```

通过日志/报告都可以清楚的看到。

* 请求的方法
* 请求url
* 响应的类型
* 响应的数据
