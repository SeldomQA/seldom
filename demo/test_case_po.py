from pyse import Pyse, TestCase, TestRunner

'''
used Page Object Model.
'''

class BasePage:

    def __init__(self, driver, base_url="https://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url

    def _open(self, url):
        url = self.base_url + url
        self.driver.open(url)
    
    def open(self):
        self._open(self.url)


class BaiduPage(BasePage):
    
    url = "/"

    def search_input(self, searck_key):
        self.driver.type("id=>kw", searck_key)

    def search_button(self):
        self.driver.click("id=>su")


class BaiduTest(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("firefox")

    def test_case(self):
        ''' baidu search key : pyse '''
        bd = BaiduPage(self.driver)
        bd.open()
        bd.search_input("pyse")
        bd.search_button()
        self.assertTitle("pyse_百度搜索")


if __name__ == '__main__':
    runner = TestRunner('./','百度测试用例','测试环境：Firefox')
    runner.run()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。
'''

