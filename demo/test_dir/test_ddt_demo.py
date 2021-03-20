import os
import seldom
from seldom import data, file_data

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
JSON_DATA = os.path.join(DATA_PATH, "json_data.json")
YAML_DATA = os.path.join(DATA_PATH, "yaml_data.yaml")
CSV_DATA = os.path.join(DATA_PATH, "csv_data.csv")
EXCEL_DATA = os.path.join(DATA_PATH, "excel_data.xlsx")


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


class FileDataTest(seldom.TestCase):
    """form input test case"""

    @file_data(file=JSON_DATA,  key="name")
    def test_json(self, firstname, lastname):
        """
        used file_data test
        """
        self.open("https://www.w3school.com.cn/tiy/t.asp?f=html_form_text")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname)
        self.type(name="lastname", text=lastname)
        self.sleep(1)

    @file_data(file=YAML_DATA,  key="name")
    def test_yaml(self, firstname, lastname):
        """
        used file_data test
        """
        self.open("https://www.w3school.com.cn/tiy/t.asp?f=html_form_text")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname)
        self.type(name="lastname", text=lastname)
        self.sleep(1)

    @file_data(file=CSV_DATA,  line=2)
    def test_csv(self, firstname, lastname):
        """
        used file_data test
        """
        self.open("https://www.w3school.com.cn/tiy/t.asp?f=html_form_text")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname)
        self.type(name="lastname", text=lastname)
        self.sleep(1)

    @file_data(file=EXCEL_DATA, sheet="Sheet1", line=2)
    def test_excel(self, firstname, lastname):
        """
        used file_data test
        """
        self.open("https://www.w3school.com.cn/tiy/t.asp?f=html_form_text")
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname)
        self.type(name="lastname", text=lastname)
        self.sleep(1)


if __name__ == '__main__':
    seldom.main(debug=True)
