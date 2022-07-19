from selenium import webdriver
from selenium.webdriver.common.by import By


class YouSe:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def get_element(self, **kwargs):
        by, value = next(iter(kwargs.items()))
        if by == "id":
            return self.driver.find_element(By.ID, value)
        if by == "name":
            return self.driver.find_element(By.NAME, value)
        else:
            pass

    def type(self, text: str, **kwargs):
        elem = self.get_element(**kwargs)
        elem.send_keys(text)

    def click(self, **kwargs):
        elem = self.get_element(**kwargs)
        elem.click()
