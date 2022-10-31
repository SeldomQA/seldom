import seldom


class BaiduTest(seldom.TestCase):
    """
    * start_class/end_class
    * start/end
    """

    @classmethod
    def start_class(cls):
        """start class"""
        print("test class start")
        cls.max_window()

    @classmethod
    def end_class(cls):
        """end class"""
        ...

    def start(self):
        """start"""
        print("test case start")
        self.index_page = "https://www.baidu.com/"
        self.news_page = "https://news.baidu.com/"

    def end(self):
        """end"""
        ...

    def test_open_index(self):
        """open baidu index page"""
        self.open(self.index_page)

    def test_open_news(self):
        """"open baidu news page"""
        self.open(self.news_page)


if __name__ == '__main__':
    seldom.main(debug=True)
