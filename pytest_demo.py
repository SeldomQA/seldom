import pytest
from seldom import testdata


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3+5", testdata.get_int()), # seldom 生成随机数据
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

import seldom
from appium import webdriver


class TestApp(seldom.TestCase):

    def start(self):
        # APP定义运行环境
        desired_caps = {
            'deviceName': 'Android Emulator',
            'automationName': 'appium',
            'platformName': 'Android',
            'platformVersion': '7.0',
            'appPackage': 'com.android.calculator2',
            'appActivity': '.Calculator',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_calculator(self):
        """测试计算器"""
        self.driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
        self.driver.find_element_by_id("com.android.calculator2:id/op_add").click()
        self.driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
        self.driver.find_element_by_id("com.android.calculator2:id/eq").click()


if __name__ == '__main__':
    seldom.main()
