## 如何设置前置步骤

在编写自动化测试用例的过程中，我们需要设置前置步骤。这时候就需要将一些前置动作放到`start()/start_class()`中，将一些前置动作放到`end()/end_class()`中。

### start/end使用

当你想在每条用例开始之前执行的动作，放到`start()/end()`方法中。

```python
import seldom


class TestCase(seldom.TestCase):

    def start(self):
        print("一条测试用例开始")
        self.get("https://www.baidu.com")
    
    def end(self):
        print("一条测试结果")
        self.assertInTitle("百度搜索")

    def test_search_seldom(self):
        self.type_enter(id_="kw", text="seldom")
        

    def test_search_poium(self):
        self.type_enter(id_="kw", text="poium")

#...

```

### start_class/end_class使用

有些用例需要在测试类开始之前执行一些动作，这个时候就会用到`start_class()/end_class()`类方法。

```python
import seldom


class TestCase(seldom.TestCase):

    def start_class(self):
        print("测试类开始执行")
        self.get("https://www.baidu.com")

    def end_class(self):
        print("测试类结束执行")
        self.assertInTitle("百度搜索")

    def test_search_seldom(self):
        self.type_enter(id_="kw", text="seldom", clear=True)

    def test_search_poium(self):
        self.type_enter(id_="kw", text="poium", clear=True)


```

但是，

__不推荐你把用例的操作步骤 `start_class()/end_class()`方法中!__

__不推荐你把用例的操作步骤 `start_class()/end_class()`方法中!__

__不推荐你把用例的操作步骤 `start_class()/end_class()`方法中!__

因为它不属于某条用例的一部分，一旦里面的操作步骤运行失败，测试报告都不会生成。
