## seldom 定位元素

seldom 提供了8中定位方式，说seldom保持一致。

* id_
* name
* class_name
* tag
* link_text
* partial_link_text
* css
* xpath

### 使用方式

```py
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom_百度搜索")


```

点击`click()`和输入`type()`的时候直接使用。

__帮助信息：__

* [CSS选择器](https://www.w3school.com.cn/cssref/css_selectors.asp)
* [xpath语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

### 定位一组元素

有时候我们通过一种定位写法不能找到单个元素，需要在一种定位方式中使用下标，在seldom中可以通过`index`指定下标。

* selenium中的写法

```py
driver.find_elements_by_tag_name("input")[7].send_keys("selenium")
```

* seldom中的写法

```py
self.type(tag="input", index=7, text="seldom")
```

在seldom中不指定`index`默认下标为`0`。

