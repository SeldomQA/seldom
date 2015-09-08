#coding=utf-8
from pyse import Pyse
from time import sleep

driver = Pyse("chrome")

driver.open("https://www.baidu.com")
driver.type("[name='wd']", u"pyse自动化测试")
driver.click("#kw")
sleep(2)
driver.quit()
