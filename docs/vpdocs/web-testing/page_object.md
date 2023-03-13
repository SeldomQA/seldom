# Page Object

seldom API 的设计理念是将元素操作和元素定位放到起，本身不太适合实现`Page object`设计模式。

[poium](https://github.com/SeldomQA/poium) 是`Page objects`设计模式最佳实践。

* pip 安装

```shell
> pip install poium
```

将 seldom 与 poium 结合使用。

```python
import seldom
from poium import Page, Element


class BaiduPage(Page):
    """baidu page"""
    search_input = Element(id_="kw")
    search_button = Element(id_="su")


class BaiduTest(seldom.TestCase):
    """Baidu search test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver, print_log=True)
        page.open("https://www.baidu.com")
        page.search_input.send_keys("seldom")
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main(browser="chrome")
```
