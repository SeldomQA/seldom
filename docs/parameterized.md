### seldom 数据驱动最佳实践

如果自动化某个功能，测试数据不一样而操作步骤是一样的，那么就可以使用参数化来节省测试代码。

seldom集成了参数化功能。

__参数化测试用例：__

```python

import seldom
from seldom import data


class BaiduTest(seldom.TestCase):

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, name, keyword):
        """
         used parameterized test
        :param name: case name
        :param keyword: search keyword
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=keyword)
        self.click(css="#su")
        self.assertTitle(keyword+"_百度搜索")
```

通过`@data()` 装饰器来参数化测试用例。

__参数化测试类：__

也可以针对测试类进行参数化, 通过`data_class` 方法：

```python
import seldom
from seldom import ddt_class


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

#### 使用第三方ddt

有时测试数据会比较多，需要将数据存到测试文件，推荐使用[ddt](https://github.com/datadriventests/ddt)。

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
    seldom.main(path="test_sample.py",
                rerun=0,
                save_last_run=False,
                )
```

更多的用法请查看ddt文档：https://ddt.readthedocs.io/en/latest/example.html
