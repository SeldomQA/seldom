import seldom
from seldom import data, file_data


class BingTest(seldom.TestCase):
    """Bing search test case"""

    @data([
        ("First case description", "seldom"),
        ("Second case description", "selenium"),
        ("Third case description", "unittest"),
    ])
    def test_bing_tuple(self, desc, search_key):
        """
         used tuple test data
        :param desc: case desc
        :param search_key: search keyword
        """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=search_key, enter=True)
        self.assertInTitle(search_key)

    @data([
        ["First case description", "seldom"],
        ["Second case description", "selenium"],
        ["Third case description", "unittest"],
    ])
    def test_bing_list(self, desc, search_key):
        """
         used list test data
        :param desc: case desc
        :param search_key: search keyword
        """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=search_key, enter=True)
        self.assertInTitle(search_key)

    @data([
        {"scene": "First case description", "search_key": "seldom"},
        {"scene": "Second case description", "search_key": "selenium"},
        {"scene": "Third case description", "search_key": "unittest"},
    ])
    def test_bing_dict(self, scene, search_key):
        """
         used dict test data
        :param scene: case desc
        :param search_key: search keyword
        """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=search_key, enter=True)
        self.assertInTitle(search_key)


class FileDataTest(seldom.TestCase):
    """form input test case"""

    def start(self):
        self.test_url = "https://www.w3school.com.cn/tiy/t.asp?f=eg_html_form_submit"

    @file_data("json_data.json", key="name")
    def test_json_list(self, firstname, lastname):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname, clear=True)
        self.type(name="lastname", text=lastname, clear=True)
        self.sleep(1)

    @file_data("json_data.json", key="login")
    def test_json_dict(self, _, username, password):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=username, clear=True)
        self.type(name="lastname", text=password, clear=True)
        self.sleep(1)

    @file_data("yaml_data.yaml", key="name")
    def test_yaml_list(self, firstname, lastname):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname, clear=True)
        self.type(name="lastname", text=lastname, clear=True)
        self.sleep(1)

    @file_data("yaml_data.yaml", key="login")
    def test_yaml_dict(self, username, password):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=username, clear=True)
        self.type(name="lastname", text=password, clear=True)
        self.sleep(1)

    @file_data("csv_data.csv", line=2)
    def test_csv(self, firstname, lastname):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname, clear=True)
        self.type(name="lastname", text=lastname, clear=True)
        self.sleep(1)

    @file_data(file="excel_data.xlsx", sheet="Sheet1", line=2)
    def test_excel(self, firstname, lastname):
        """
        used file_data test
        """
        self.open(self.test_url)
        self.switch_to_frame(id_="iframeResult")
        self.type(name="firstname", text=firstname, clear=True)
        self.type(name="lastname", text=lastname, clear=True)
        self.sleep(1)


if __name__ == '__main__':
    seldom.main(browser="gc", debug=False)
