import seldom
from seldom import Steps


class BingTest(seldom.TestCase):
    """Baidu search test case"""

    def test_case_two(self):
        """method chaining """
        Steps(url="https://cn.bing.com").open().find("#sb_form_q").type("seldom").submit()
        self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    seldom.main(debug=True)
