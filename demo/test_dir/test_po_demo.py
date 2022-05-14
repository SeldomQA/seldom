"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poium=1.1.1
```
"""
import seldom
from seldom import Seldom
from poium import Page, Element


class BaiduPage(Page):
    """baidu page"""
    search_input = Element(id_="kw", describe="搜索输入框")
    search_button = Element(id_="su", describe="搜索按钮")


class BaiduTest(seldom.TestCase):
    """Baidu search test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(Seldom.driver, print_log=True)
        page.open("https://www.baidu.com")
        page.search_input.send_keys("seldom")
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main(browser='chrome', debug=True)
