import seldom
from seldom import Steps


class BaiduTest(seldom.TestCase):
    """Baidu search test case"""

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertTitle("seldom_百度搜索")

    def test_case_two(self):
        """method chaining """
        Steps(url="https://www.baidu.com").open().find("#kw").type("seldom").find("#su").click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main(debug=True)

