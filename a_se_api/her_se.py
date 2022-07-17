from selenium import webdriver
from selenium.webdriver.common.by import By

dr = None


def start_chrome():
    global dr
    dr = webdriver.Chrome()


def go_to(url):
    global dr
    dr.get(url)


def close():
    global dr
    dr.close()


def id(elem):
    global dr
    return dr.find_element(By.ID, elem)

def name(elem):
    global dr
    return dr.find_element(By.NAME, elem)


def wirte(elem, text):
    elem.send_keys(text)


def click(elem):
    elem.click()

