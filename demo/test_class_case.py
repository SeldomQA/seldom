# coding=utf-8
import pyse,nose
from time import sleep


class TestLogin:
    '''test login '''
    
    def setup(self):
        self.driver = pyse.Pyse("chrome")
        self.base_url = "http://www.126.com"
        self.driver.wait(30)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        ''' test mail login : admin ,123456 '''
        driver = self.driver
        driver.open(self.base_url)
        driver.switch_to_frame("#loginDiv > iframe")
        driver.type("input[name='email']","admin")
        driver.type("input[name='password']","123456")
        driver.click("#dologin")
        sleep(3)
        user_name = driver.get_text("#spnUid")
        assert user_name=="admin@126.com"


if __name__ == '__main__':
    test_pro = pyse.TestRunner()
    test_pro.run()

'''
============运行测试用例说明========
TestRunner() 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定路径，例如：
TestRunner(r"D:/test_project/test_case")

执行run()方法运行测试用例.

'''