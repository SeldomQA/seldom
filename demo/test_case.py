from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized


class BaiduTest(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        ''' Setting browser driver, Using chrome by default.'''
        cls.driver = Pyse("chrome")

    '''
    A simple test
    '''
    def test_case(self):
        ''' baidu search key : pyse '''
        self.driver.open("https://www.baidu.com/")
        self.driver.move_to_element("link_text=>设置")
        self.driver.click("link_text=>搜索设置")
        self.driver.select("#nr", '20')
        self.driver.click("class=>prefpanelgo")
        alert_text = self.driver.get_alert_text()
        self.assertAlert("已经记录下您的使用偏好")
        self.driver.accept_alert()

    """
    used parameterized test
    """
    @parameterized.expand([
        (1, 'pyse'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self,name,search_key):
        ''' baidu search key : pyse '''
        self.driver.open("https://www.baidu.com")
        self.driver.clear("id=>kw")
        self.driver.type("id=>kw", search_key)
        self.driver.click("css=>#su")
        self.assertTitle(search_key)


if __name__ == '__main__':
    runner = TestRunner('./', '百度测试用例', '测试环境：Firefox')
    runner.debug()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。

debug() # debug模式不生成测试报告
run()   # run模式生成测试报告
'''

