import seldom
from seldom import Steps


class WebTestChaining(seldom.TestCase):
    """test chaining API"""

    def test_baidu(self):
        """test baidu search"""
        Steps().open("https://www.baidu.com").find("#kw").type("seldom").find("#su").click().sleep(2)
        self.assertInTitle("seldom")

    def test_bing(self):
        """test bing search"""
        Steps().open("https://www.bing.com").find("#sb_form_q").type("seldomqa").find("#sb_form_q").submit().sleep(2)
        self.assertInTitle("seldomqa")


if __name__ == '__main__':
    seldom.main(browser="edge")
