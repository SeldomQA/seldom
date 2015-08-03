#coding=utf-8
from pyse import Pyse
from time import sleep

driver = Pyse("chrome")

driver.open("https://www.baidu.com")
driver.type("//*[@id='kw']", u"pyse自动化测试")
driver.click("//*[@id='su']")
sleep(2)
driver.quit()
