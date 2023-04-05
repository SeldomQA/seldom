# 数据驱动

数据驱动是测试框架非常重要的功能之一，它可以有效的节约大量重复的测试代码。seldom针对该功能做强大的支持。


### @class_data() 方法

`class_data()` 装饰测试类，测试类下面的任何方法可以共用 `class_data()` 中定义的变量。
 
* 用法一

```python
import seldom
from seldom import data_class


@data_class([
    {"username": "user_1", "password": "abc123"},
    {"username": "user_2", "password": "abc456"},
])
class DDTTest(seldom.TestCase):

    def test_data_func(self):
        """ data driver case """
        print("username->", self.username)
        print("password->", self.password)


if __name__ == '__main__':
    seldom.main(debug=True)
```

* 用法二

```python
import seldom
from seldom import data_class


@data_class(("username", "password"), [
    ("user_1", "abc123"),
    ("user_1", "abc456"),
])
class DDTTest(seldom.TestCase):

    def test_data_func(self):
        """ data driver case """
        print("username->", self.username)
        print("password->", self.password)


if __name__ == '__main__':
    seldom.main(debug=True)
```

### @data()方法

当测试数据量比较少的情况下，可以通过`@data()`管理测试数据。


**参数化测试用例**

```python

import seldom
from seldom import data


class DataDriverTest(seldom.TestCase):

    @data([
        ("First case", "seldom"),
        ("Second case", "selenium"),
        ("Third case", "unittest"),
    ])
    def test_tuple_data(self, name, keyword):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {keyword}")
    
    @data([
        ["First case", "seldom"],
        ["Second case", "selenium"],
        ["Third case", "unittest"],
    ])
    def test_list_data(self, name, keyword):
        """
        Used list test data
        """
        print(f"test data: {keyword}")
    
    @data([
        {"scene": 'First case', 'keyword': 'seldom'},
        {"scene": 'Second case', 'keyword': 'selenium'},
        {"scene": 'Third case', 'keyword': 'unittest'},
    ])
    def test_dict_data(self, scene, keyword):
        """
        used dict test data
        """
        print(f"case desc: {scene}")
        print(f"test data: {keyword}")

```

通过`@data()` 装饰器来参数化测试用例。

**动态生成测试数据**

除了使用固定的数据外，也可以动态生成一些测试数据用于自动化测试。

```python
import seldom
from seldom import data
from seldom import testdata


def test_data() -> list:
    """
    自动生成测试数据
    return [{},{}]
    """
    login_data = []
    for i in range(5):
        login_data.append({
            "scene": f"login{i}",
            "username": testdata.get_email(),
            "password": testdata.get_int(100000, 999999)
        })
    return login_data


class MyTest(seldom.TestCase):

    @data(test_data())
    def test_login(self, _, username, password):
        """test login"""
        print(f"test username: {username}")
        print(f"test password: {password}")
```

### @file_data() 方法

当测试数据量比较大的情况下，可以通过`@file_data()`管理测试数据。


__CSV 文件参数化__

seldom 支持将`csv`文件的参数化。

表格内容如下（data.csv）：

| username | password |
| -------- | -------- |
| admin    | admin123 |
| guest    | guest123 |

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("data.csv", line=2, end_line=10)
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

- file: 指定 csv 文件的路径。
- line: 指定从第几行开始读取，默认第 1 行。
- end_line: 指定读取到第几行的数据，默认None, 最后一行。


**excel 文件参数化**

seldom 支持将`excel`文件的参数化。

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("data.xlsx", sheet="Sheet1", line=2, end_line=10)
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

- file : 指定 excel 文件的路径。
- sheet: 指定 excel 的标签页，默认名称为 Sheet1。
- line : 指定从第几行开始读取，默认第 1 行。
- end_line: 指定读取到第几行的数据，默认None, 最后一行。

**JSON 文件参数化**

seldom 支持将`JSON`文件的参数化。

json 文件：

```json
{
  "login1": [
    ["admin", "admin123"],
    ["guest", "guest123"]
  ],
  "login2": [
    {
      "username": "Tom",
      "password": "tom123"
    },
    {
      "username": "Jerry",
      "password": "jerry123"
    }
  ]
}
```

> 注：`login1` 和 `login2` 的调用方法一样。 区别是前者更简洁，后者更易读。

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("data.json", key="login1")
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

- file : 指定 JSON 文件的路径。
- key: 指定字典的 key，默认不指定解析整个 JSON 文件。

**YAML 文件参数化**

seldom 支持`YAML`文件的参数化。

data.yaml 文件：

```yaml
login1:
  - - admin
    - admin123
  - - guest
    - guest123
login2:
  - username: Tom
    password: tom123
  - username: Jerry
    password: jerry123
```

同`JSON`用法一样，`YAML`书写更加简洁。

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("data.yaml", key="login1")
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

- file : 指定 YAML 文件的路径。
- key: 指定字典的 key，默认不指定解析整个 YAML 文件。

__解释： `@file_data()`是如何查找测试数据文件的？__

```shell
mypro/
├── test_dir/
│   ├── module/
│   │   ├── case/
│   │   │   ├── test_sample.py (使用@file_data)
├── test_data/
│   ├── module_data/
│   │   ├── data.csv (测试数据文件所以位置)
...
```

在 `test_sample.py` 中使用`@file_data("data.csv")`默认只能向上查找两级目录，即到`module`目录下遍历查找`data.csv`文件。显然这中情况下是无法找到`data.csv` 文件的。

如果用例层级比较深，只需要指定文件目录的`“相对路径”`即可，使用方式：`@file_data("test_data/module_data/data.csv")`，不要加`./`的前缀。


**支持配置测试环境**

在自动化测试过程中，我们往往需要一套代码在不同的环境下运行，seldom支持根据环境使用不同的数据文件。

* 数据文件目录结构（一）
```shell
.
└── test_data
    ├── develop
    │   └── test_data.json
    ├── product
    │   └── test_data.json
    └── test
        └── test_data.json
```

* 数据文件目录结构（二）
```shell
.
├── develop
│   └── test_data
│       └── test_data.json
├── product
│   └── test_data
│       └── test_data.json
└── test
    └── test_data
        └── test_data.json
```

* 配置测试环境
```python
import seldom
from seldom import file_data
from seldom import Seldom


class MyTest(seldom.TestCase):

    # 数据文件目录结构（一）
    @file_data("test_data.json")
    def test_case(self, req, resp):
        f"""a simple test case"""
        ...

    # 数据文件目录结构（二）
    @file_data("test_data/test_data.json")
    def test_case(self, req, resp):
        f"""a simple test case"""
        ...


if __name__ == '__main__':
    Seldom.env = "product"  # test/develop/product 设置当前环境
    seldom.main(debug=True)
```

`Seldom.env` 默认为`None`，当设置了环境，`@file_data()` 会带上环境的目录名，例如:

* `test_data.json` 查找的文件为 `product/test_data.json`
* `test_data/test_data.json` 查找的文件为 `product/test_data/test_data.json`

> `Seldom.env` 可以随意命名，但最好遵循一定的规范:`test/develop/product`。你还可以利用`Seldom.env`变量本地创建更多的配置。

### @api_data()方法

越来越多的公司落地 数据工厂，通过造数平台/数据工厂 来创建管理测试数据；`@api_data()` 装饰器支持通过URL获取驱动数据。

* 接口数据

`http://127.0.0.1:8080/v1/public/data_service/get_case_data?data_id=1`

```json
{
  "success":true,
  "error": {
    "code":"",
    "message":""
  },
  "result":[
    {
      "scene": "测试1",
      "email": "li123@126.com",
      "password": "abc123"
    },
    {
      "scene": "测试2",
      "email": "li456@126.com",
      "password": "abc456"
    }
  ]
}
```

* 调用接口数据

```python
import seldom
from seldom import api_data


class TestApi(seldom.TestCase):

    @api_data(url="http://127.0.0.1:8080/v1/public/data_service/get_case_data",
              params={"data_id": 1},
              headers={"X-Account-Email": "li.li@gmail.com"},
              ret="result")
    def test_case(self, scene, email, password):
        """
        test get request
        """
        print("name:", scene)
        print("email:", email)
        print("password:", password)


if __name__ == '__main__':
    seldom.main(debug=True)
```

__`api_data()`参数说明__

* url: 返回数据的接口url地址；默认仅支持`GET` 接口。
* params: 请求参数。
* header: 请求头。
* ret: 提取接口返回的数据，默认仅支持 list 类型。

### 使用函数构造数据

如果数据驱动使用的数据比较简单其有规律，可以通过自定义函数生成，并且把函数传给 `@data()` 装饰器即可。

```python
import seldom
from seldom import data


def register():
    """生成注册账号信息"""
    users = []
    for i in range(10):
        users.append({
            "username": f"user{i}",
            "password": f"abc123{i}",
            "password2": f"abc123{i}"}
        )

    return users


class DDTTest(seldom.TestCase):

    @data(register())
    def test_data_func(self, username, password, password2):
        """ data driver case """
        print("username->", username)
        print("password->", password)
        print("password2->", password2)


if __name__ == '__main__':
    seldom.main(debug=True)
```

### 支持第三方 ddt 库

seldom 仍然允许你使用第三方参数化库，例如：[ddt](https://github.com/datadriventests/ddt)。

安装：

```shell
> pip install ddt
```

创建测试文件`test_data.json`：

```json
{
  "test_data_1": {
    "word": "seldom"
  },
  "test_data_2": {
    "word": "unittest"
  },
  "test_data_3": {
    "word": "selenium"
  }
}
```

在 seldom 使用`ddt`。

```python
import seldom
from ddt import ddt, file_data


@ddt
class YouTest(seldom.TestCase):

    @file_data("test_data.json")
    def test_case(self, word):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=word)
        self.click(css="#su")
        self.assertTitle(word + "_百度搜索")


if __name__ == '__main__':
    seldom.main()
```

更多的用法请查看 ddt 文档：https://ddt.readthedocs.io/en/latest/example.html


