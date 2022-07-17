import seldom
from seldom import data


class BaiduTest(seldom.TestCase):
    """Baidu search test case"""

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, name, search_key):
        """
         used parameterized test
        :param name: case name
        :param search_key: search keyword
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=search_key)
        self.click(css="#su")
        self.assertInTitle(search_key)


if __name__ == '__main__':
    seldom.main(browser="gc", debug=True)
