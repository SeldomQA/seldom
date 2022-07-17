import seldom


class BingTest(seldom.TestCase):

    def test_bing_search(self):
        """selenium api"""
        self.open("http://www.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    seldom.main(browser="gc", debug=True)
