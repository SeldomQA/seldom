import seldom
from seldom import file_data


class SampleTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.selenium.dev")
        self.assertTitle("Selenium")
        self.assertInUrl("selenium.dev")


class DDTTest(seldom.TestCase):

    @file_data(file="../data.json", key="bing")
    def test_data_driver(self, _, keyword):
        """ data driver case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=keyword, enter=True)
        self.assertInTitle(keyword)


if __name__ == '__main__':
    seldom.main(debug=True)
