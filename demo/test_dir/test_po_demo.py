"""
page object model
"""
import pyse


class BaiduPage:
    """baidu page"""
    search_input = "#kw"
    search_button = "#su"


class BaiduTest(pyse.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        self.open("https://www.baidu.com/")
        self.type(BaiduPage.search_input, "pyse")
        self.click(BaiduPage.search_button)
        self.sleep(2)
        self.assertTitle("pyse_百度搜索")


if __name__ == '__main__':
    pyse.main(debug=True)
