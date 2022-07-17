import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class HeSe:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url: str):
        self.driver.get(url)
        return self

    def close(self):
        self.driver.close()
        return self

    def get_element(self, **kwargs):
        by, value = next(iter(kwargs.items()))
        if by == "id":
            return self.driver.find_element(By.ID, value)
        if by == "name":
            return self.driver.find_element(By.NAME, value)
        else:
            pass

    def sleep(self, sec):
        time.sleep(sec)
        return self

    def type(self, text: str, **kwargs):
        elem = self.get_element(**kwargs)
        elem.send_keys(text)
        return self

    def click(self, **kwargs):
        elem = self.get_element(**kwargs)
        elem.click()
        return self
