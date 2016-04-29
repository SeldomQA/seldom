# coding=utf-8
from pyse import Pyse,TestRunner
from time import sleep


class TestLogin:
    '''test login '''

    def setup(self):
        self.driver = Pyse("chrome")
        self.base_url = "http://www.126.com"

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        ''' test mail login : admin ,123456 '''
        driver = self.driver
        driver.open(self.base_url)
        driver.switch_to_frame("xpath=>//*[@id='loginDiv']/iframe")
        driver.type("name=>email", "admin")
        driver.type("name=>password", "123456")
        driver.click("id=>dologin")
        sleep(3)
        user_name = driver.get_text("id=>spnUid")
        assert user_name == "admin@126.com"


if __name__ == '__main__':
    test_pro = TestRunner()
    test_pro.run()

'''
============运行测试用例说明========
TestRunner() 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定路径，例如：
TestRunner(r"D:/test_project/test_case")

执行run()方法运行测试用例.

'''