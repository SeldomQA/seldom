### 实现Page objects设计模式

seldom API的设计理念已经将元素操作和元素定位做了整合，本身不太适合实现Page objects设计模式。

[poium](https://github.com/SeldomQA/poium)是Page objects设计模式最佳实践，如果想使用poium，需要单独安装。

```shell
> pip install poium
```

将seldom与poium结合使用。

```python
import seldom
from seldom import Seldom
from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(Seldom.driver)
        page.get("https://www.baidu.com")
        page.search_input = "seldom"
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main("test_po_demo.py")

```
