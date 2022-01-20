import seldom


class BaiduTest(seldom.TestCase):
    """
    * start_class/end_class
    * start/end
    """

    @classmethod
    def start_class(cls):
        print("test class start")
        cls.max_window()

    @classmethod
    def end_class(cls):
        print("test class end")

    def start(self):
        print("test case start")
        self.index_page = "https://www.baidu.com/"
        self.news_page = "https://news.baidu.com/"

    def end(self):
        print("test case end")

    def test_case1(self):
        self.open(self.index_page)

    def test_case2(self):
        self.open(self.news_page)


if __name__ == '__main__':
    seldom.main(debug=True)
