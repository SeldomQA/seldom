# HTTP测试

## 优势

seldom 非常适合个人接口自动化项目，它有以下优势。

* 可以写更少的代码
* 提供详细的运行日志
* 提供专门为接口设计的断言
* 强大的数据驱动
* 自动生成HTML/XML测试报告
* 支持生成随机数据
* 支持`har`/`swagger`文件转case
* 支持数据库操作

这些是seldom支持的功能，我们只需要集成HTTP接口库，并提供强大的断言即可。`seldom 2.0` 加入了HTTP接口自动化测试支持。

Seldom 完全兼容 [Requests](https://docs.python-requests.org/en/master/) API 如下:

| seldom         | requests           |
|----------------|--------------------|
| self.get()     | requests.get()     |
| self.post()    | requests.post()    |
| self.put()     | requests.put()     |
| self.delete()  | requests.delete()  |
| self.patch()   | requests.patch()   |
| self.Session() | requests.session() |

## Seldom VS Request+unittest

* unittest + requests 接口自动化示例：

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

* seldom 接口自动化测试示例：

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

* 运行日志

打开debug模式`seldom.run(debug=True)` 运行上面的用例。

```shell

> python test_req.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info

test_get_method (test_req.TestAPI) ... 2023-02-14 23:37:07 request.py | INFO |
-------------- Request -----------------[🚀]
2023-02-14 23:37:07 request.py | INFO | [method]: GET      [url]: http://httpbin.org/get
2023-02-14 23:37:07 request.py | DEBUG | [params]:
 {
  "key1": "value1",
  "key2": "value2"
}
2023-02-14 23:37:08 request.py | INFO | -------------- Response ----------------[🛬️]
2023-02-14 23:37:08 request.py | INFO | successful with status 200
2023-02-14 23:37:08 request.py | DEBUG | [type]: json      [time]: 0.785683
2023-02-14 23:37:08 request.py | DEBUG | [response]:
 {
  "args": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.28.1",
    "X-Amzn-Trace-Id": "Root=1-63ebaaa4-325e25be64b104e770c25f8f"
  },
  "origin": "173.248.248.88",
  "url": "http://httpbin.org/get?key1=value1&key2=value2"
}
2023-02-14 23:37:08 case.py | INFO | 👀 assertStatusCode -> 200.
ok

----------------------------------------------------------------------
Ran 1 test in 0.795s

OK
2023-02-14 23:37:08 runner.py | SUCCESS | A run the test in debug mode without generating HTML report!
```

通过日志/报告都可以看到详细的HTTP接口调用信息。
