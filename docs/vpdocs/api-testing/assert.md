# 更强大的断言

断言接口返回的数据是HTTP接口自动化测试非常重要的工作，提供强大的断言方法可以提高用例的编写效率。

### assertJSON

`assertJSON()` 断言接口返回的某部分数据。

* 请求参数

```json
{
  "name": "tom",
  "hobby": [
    "basketball",
    "swim"
  ]
}
```

* 返回结果

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

我的目标是断言`name` 和 `hobby` 部分的内容。

```python
import seldom


class TestAPI(seldom.TestCase):

    def test_assert_json(self):
        # 接口参数
        payload = {"name": "tom", "hobby": ["basketball", "swim"]}
        # 接口调用
        self.get("http://httpbin.org/get", params=payload)

        # 断言数据
        assert_data = {
            "hobby": ["swim", "basketball"],
            "name": "tom"
        }
        self.assertJSON(assert_data, self.response["args"], exclude=["xxx"])
```

* exclude 用于设置跳过的检查字段，例如一些 时间、随机数 等，每次调用都不一样，但并不影响结果的正确性。通过 exclude 来设置屏蔽这些字段的检查。

### assertPath

`assertPath` 是基于 `jmespath` 实现的断言，功能非常强大。

* jmespath: https://jmespath.org/specification.html

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
        self.assertPath("args.name", "tom")
        self.assertPath("args.hobby[0]", "basketball")
        self.assertInPath("args.hobby[0]", "ball")

```

* `args.hobby[0]` 提取接口返回的数据。
* `assertPath()` 判断提取的数据是否等于`basketball`; 
* `assertInPath()` 判断提取的数据是否包含`ball`。

### assertSchema

当你不关心数据本身是什么，而是关心数据的结构和类型时，可以使用 `assertSchema` 断言方法。 `assertSchema` 是基于 `jsonschema` 实现的断言方法。

* jsonschema: https://json-schema.org/learn/

```python
import seldom
from seldom.utils import genson


class TestAPI(seldom.TestCase):

    def test_assert_schema(self):
        # 接口参数
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        # 调用接口
        self.get("/get", params=payload)

        # 生成数据结构和类型
        schema = genson(self.response["args"])
        print("json Schema: \n", schema)

        # 断言数据结构和类型
        assert_data = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "age": {
                    "type": "string"
                },
                "hobby": {
                    "type": "array", "items": {"type": "string"}
                },
                "name": {
                    "type": "string"
                }
            },
            "required":
                ["age", "hobby", "name"]
        }
        self.assertSchema(assert_data, self.response["args"])

```

* `genson`: 可以生成`jsonschema`数据结构和类型（`seldom 2.9` 新增）。
