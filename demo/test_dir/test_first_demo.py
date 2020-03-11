import seldom
from seldom import data


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """A simple test"""
        self.open("https://www.baidu.com/")
        self.move_to_element(link_text="设置")
        self.click(link_text="搜索设置")
        self.select(css="#nr", value='20')
        self.click(class_name="prefpanelgo")
        self.sleep(2)
        self.assertAlertText("已经记录下您的使用偏好")
        self.accept_alert()

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
        :return:
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=search_key)
        self.click(css="#su")
        self.assertInTitle(search_key)


if __name__ == '__main__':
    seldom.main(debug=True)

