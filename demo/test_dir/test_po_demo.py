"""
page object model
"""
import pyse
from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")


class BaiduTest(pyse.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "pyse"
        page.search_button.click()
        self.assertTitle("pyse_百度搜索")


if __name__ == '__main__':
    pyse.main("test_po_demo.py", debug=True)
