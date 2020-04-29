## 如何设置前置步骤

在编写自动化测试用例的过程中，我们需要设置前置步骤。这时候就需要将一些前置动作放到`setUp/setUpClass`中。

### setUp使用

当你想在每条用例开始之前执行的动作，放到`setUp()`方法中。

```python
import seldom


class TestCase(seldom.TestCase):

    def setUp(self):
        self.get("https://www.baidu.com")

    def test_search_seldom(self):
        self.type_enter(id_="kw", text="seldom")
        self.assertTitle("seldom_百度搜索")

    def test_search_poium(self):
        self.type_enter(id_="kw", text="poium")
        self.assertTitle("poium_百度搜索")
#...

```

### setUpClass使用

有些用例需要在测试类开始之前执行一些动作，这个时候就会用到`setUpClass()`类方法。

```python
import seldom


class TestCase(seldom.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get(cls, "https://www.baidu.com")
        cls.type(cls, id_="kw", text="setupclass")
        cls.click(cls, id_="su")
        cls.sleep(2)

    def test_get_search_result(self):
        result = self.get_text(xpath="//div/h3/a", index=0)
        print(result)


if __name__ == '__main__':
    seldom.main(debug=True)


```

`setUpClass()`方法比较特殊，在它下面编写测试步骤，需要注意两点：
* 类方法以 `cls` 前缀。
* 调用的方法第一个参数需要传 `cls` 参数

总之，并不推荐你把用例的操作步骤 `setUpClass()`方法中。
