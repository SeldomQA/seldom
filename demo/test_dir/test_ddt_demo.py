import os
import seldom
from seldom import data, file_data

JSON_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "json_data.json")


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


class W3CTest(seldom.TestCase):
    """form input test case"""

    @file_data(file=JSON_DATA,  key="name")
    def test_name(self, firstname, lastname):
        """
         used file_data test
        """
        self.open("https://www.w3school.com.cn/tiy/t.asp?f=html_form_text")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname)
        self.type(name="lastname", text=lastname)
        self.sleep(2)


if __name__ == '__main__':
    seldom.main(debug=True)
