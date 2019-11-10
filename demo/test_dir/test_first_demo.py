import pyse
from pyse import ddt


class BaiduTest(pyse.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        self.open("https://www.baidu.com/")
        self.move_to_element("link_text=>设置")
        self.click("link_text=>搜索设置")
        self.select("#nr", '20')
        self.click("class=>prefpanelgo")
        self.sleep(2)
        self.assertAlert("已经记录下您的使用偏好")
        self.accept_alert()

    @ddt.data([
        (1, 'pyse'),
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
        self.type("id=>kw", search_key)
        self.click("css=>#su")
        self.assertTitle(search_key)


if __name__ == '__main__':
    pyse.main(debug=True)

