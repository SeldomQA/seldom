from selenium import webdriver
from selenium.webdriver.common.by import By


class MySe:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def by_id(self, elem: str):
        return self.driver.find_element(By.ID, elem)

    def by_name(self, elem: str):
        return self.driver.find_element(By.NAME, elem)
