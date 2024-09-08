import seldom
from seldom import Steps


class BingTest(seldom.TestCase):
    """Bing search test case"""

    def test_case(self):
        """a simple test case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        self.assertInTitle("seldom")

    def test_case_two(self):
        """method chaining """
        Steps(url="https://cn.bing.com").open().find("#sb_form_q").type("seldom").submit().sleep(2)
        self.assertInTitle("seldom")


if __name__ == '__main__':
    seldom.main(browser="gc")
