import seldom


class WebTestOne(seldom.TestCase):
    """case lunch browser"""

    def start(self):
        self.browser("edge")

    def end(self):
        self.quit()

    def test_baidu(self):
        self.open("http://www.baidu.com")
        self.Keys(css="#chat-textarea").input("seldom").enter()
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")

    def test_bing(self):
        self.open("http://cn.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")


class WebTestTwo(seldom.TestCase):
    """class lunch browser"""

    @classmethod
    def start_class(cls):
        cls.browser(cls, "edge")

    @classmethod
    def end_class(cls):
        cls.quit(cls)

    def test_baidu(self):
        self.open("http://www.baidu.com")
        self.Keys(css="#chat-textarea").input("seldom").enter()
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")

    def test_bing(self):
        self.open("http://cn.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")


if __name__ == '__main__':
    seldom.main()
