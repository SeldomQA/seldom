import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

#
# class TestSample(unittest.TestCase):
#
#     def test_case(self):
#         dr = webdriver.Chrome()
#         try:
#             dr.get("https://cn.bing.com/")
#             dr.find_element(By.ID, "sb_form_q").send_keys("selenium")
#             dr.find_element(By.ID, "sb_form_q").submit()
#             time.sleep(2)
#         except BaseException as msg:
#             print("报错信息： %s" %msg)
#         finally:
#             dr.quit()


# class TestSample(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.dr = webdriver.Chrome()
#
#     def test_case(self):
#         dr = self.dr
#         dr.get("https://cn.bing.com/")
#         dr.find_element(By.ID, "sb_form_q").send_keys("selenium")
#         dr.find_element(By.ID, "sb_form_q11").submit()
#         time.sleep(2)
#
#     def tearDown(self) -> None:
#         self.dr.quit()


# def bing_search(dr, keyword):
#     """搜索封装"""
#     dr.find_element(By.ID, "sb_form_q").send_keys(keyword)
#     dr.find_element(By.ID, "sb_form_q11").submit()
#     time.sleep(2)
#
#
# class TestSample(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.dr = webdriver.Chrome()
#
#     def test_case(self):
#         dr = self.dr
#         dr.get("https://cn.bing.com/")
#         bing_search(dr, "selenium")
#
#     def tearDown(self) -> None:
#         self.dr.quit()
import requests


def get_admin_token():
    """封装登录"""
    url = "http://quick.testpub.cn/api/v1/login/"
    r = requests.post(url, data={"username": "admin", "password": "admin123"})
    return r.json()["data"]["Token"]


class TestSample(unittest.TestCase):

    def test_case1(self):
        login = get_admin_token()
        self.assertNotEqual(login, "")

    def test_case2(self):
        url = "http://quick.testpub.cn/api/v1/project/"
        user_token = get_admin_token()  # 调用登录
        headers = {"token": user_token}
        r = requests.post(url, headers=headers)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

