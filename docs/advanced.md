## 高级用法

### 使用随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

seldom提供了随机获取测试数据的方法。

```python
import seldom
from seldom import testdata


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        word = testdata.get_word()
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=word)
        self.click(css="#su")
        self.assertTitle(word + "_百度搜索")


if __name__ == '__main__':
    seldom.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

__更多的方法__

* first_name()
* last_name()
* username()
* get_birthday()
* get_date()
* get_digits()
* get_email()
* get_float()
* get_future_datetime()
* get_int()
* get_int32()
* get_int64()
* get_md5()
* get_now_time()
* get_past_datetime()
* get_uuid()
* get_word()
* get_words()
* get_phone()


### 数据驱动最佳实践

如果自动化某个功能时，测试数据不一样而操作步骤是一样的，那么就可以使用参数化来节省测试代码。

seldom集成了参数化功能。

__参数化测试用例__

```python

import seldom
from seldom import data


class BaiduTest(seldom.TestCase):

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, _, keyword):
        """
        used parameterized test
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=keyword)
        self.click(css="#su")
        self.assertTitle(keyword+"_百度搜索")
```

通过`@data()` 装饰器来参数化测试用例。

__参数化测试类__

也可以针对测试类进行参数化, 通过`data_class` 方法：

```python
import seldom
from seldom import data_class

@data_class(
    ("keyword", "assert_tile"),
    [("seldom", "seldom_百度搜索"),
     ("python", "python_百度搜索")
])
class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=self.keyword)
        self.click(css="#su")
        self.assertTitle(self.assert_tile)

```

__csv文件参数化__

seldom支持将`csv`文件的参数化。

表格内容如下（data.csv）：

|  username   | password  |
|  ----  | ----  |
| admin  | admin123 |
| guest  | guest123 |

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("./data.csv", line=2)
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

`csv_to_list()` 方法csv文件内容转化为list。

* file: 指定csv文件的路径。
* line: 指定从第几行开始读取，默认第1行。

__excel文件参数化__

seldom支持将`excel`文件的参数化。

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("./data.xlsx", sheet="Sheet1", line=2)
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

`excel_to_list()` 方法excel文件数据转化为list。

* file : 指定excel文件的路径。
* sheet: 指定excel的标签页，默认名称为 Sheet1。
* line :  指定从第几行开始读取，默认第1行。

__JSON文件参数化__

seldom支持将`JSON`文件的参数化。

json 文件：
```json
{
 "login":  [
    ["admin", "admin123"],
    ["guest", "guest123"]
 ]
}
```

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("./data.json", key="login")
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

* file : 指定JSON文件的路径。
* key: 指定字典的key，默认不指定解析整个JSON文件。

__YAML文件参数化__

seldom支持`YAML`文件的参数化。

data.yaml 文件：

```yaml
login:
  - - admin
    - admin123
  - - guest
    - guest123
```

```python
import seldom
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("./data.yaml", key="login")
    def test_login(self, username, password):
        """a simple test case """
        print(username)
        print(password)
        # ...

```

* file : 指定YAML文件的路径。
* key: 指定字典的key，默认不指定解析整个YAML文件。


__支持第三方ddt库__

seldom支持第三方参数化库：[ddt](https://github.com/datadriventests/ddt)。

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

更多的用法请查看ddt文档：https://ddt.readthedocs.io/en/latest/example.html


### Page objects设计模式

seldom API的设计理念是将元素操作和元素定位放到起，本身不太适合实现`Page objects`设计模式。

[poium](https://github.com/SeldomQA/poium) 是`Page objects`设计模式最佳实践，如果想使用poium，需要单独安装。

```shell
> pip install poium==1.0.0
```

将seldom与poium结合使用。

```python
import seldom
from poium import Page, Element


class BaiduPage(Page):
    """baidu page"""
    search_input = Element(id_="kw")
    search_button = Element(id_="su")


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "seldom"
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main()
```

### 自动发邮件

如果你想将测试完成的报告发送到指定邮箱，那么可以调用发邮件的方法实现。


```python
import seldom
from seldom import SMTP

# ...

if __name__ == '__main__':
    seldom.main()
    smtp = SMTP(user="send@126.com", password="abc123", host="smtp.126.com")
    smtp.sender(to="receive@mail.com", subject='Email title')
```

* `subject`邮件标题 默认：`Seldom Test Report`。
* `to`添加多个收件人 逗号`,`分隔。

如果你自定义了报告的名称，那么需要指定报告名称。

```python
import seldom
from seldom import SMTP

# ……

if __name__ == '__main__':
    report_path = "/you/path/to/report.html"
    seldom.main(report=report_path)
    smtp = SMTP(user="you@126.com", password="abc123", host="smtp.126.com")
    smtp.sender(to="receive@mail.com", subject='Email title', attachments=report_path)
```

> `debug`模式不会生成测试报告， 自动化发邮件不支持`debug` 模式，自然也无法将报告发送到指定邮箱了。



### 用例的依赖

在编写用例的时候不推荐你编写依赖的用例，但是，有些时候我们并不能完全消除这些依赖。seldom增加了用例依赖的方法。

__depend__

`depend` 装饰器用来设置依赖的用例。

```python
import seldom
from seldom import depend


class TestDepend(seldom.TestCase):

    def test_001(self):
        # ...

    @depend("test_001")
    def test_002(self):
        # ...

    @depend("test_002")
    def test_003(self):
        # ...

if __name__ == '__main__':
    seldom.main(debug=True)
```

`test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。


__if_depend__

`id_depend` 装饰器不会依赖用例的执行状态，可以自己定义是否要跳过依赖的用例。

```python
import seldom
from seldom import if_depend

class TestIfDepend(seldom.TestCase):
    Test001 = True

    def test_001(self):
        self.open("https://www.baidu.com")
        TestIfDepend.Test001 = False  # 修改Test001为 False

    @if_depend("Test001")
    def test_002(self):
        self.open("http://news.baidu.com/")


if __name__ == '__main__':
    seldom.main(debug=True)
```

1. 首先，定义变量 `Test001`，默认值为`True`。
2. 在`test_001`用例中，可以根据一些条件来选择是否修改`Test001`的值，如果改为`False`， 那么依赖的用例将被跳过。
3. 在`test_002`用例中，通过`id_depend`装饰器来判断`Test001`的值，如果为为`False`， 那么装饰的用例跳过，否则执行。

