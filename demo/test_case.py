from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized

'''
A simple test
'''
class BaiduTest(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("firefox")

    def test_case(self):
        ''' baidu search key : pyse '''
        self.driver.open("https://www.baidu.com/")
        self.driver.type("id=>kw", "pyse")
        self.driver.click("css=>#su")
        self.assertTitle("pyse_百度搜索")

'''
used parameterized test
'''

class BaiduTest2(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("firefox")

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
    runner = TestRunner('./','百度测试用例','测试环境：Chrome')
    runner.run()

'''
说明：
'./' ： 指定测试目录。
'百度测试用例' ： 指定测试项目标题。
'测试环境：Chrome' ： 指定测试环境描述。
'''

