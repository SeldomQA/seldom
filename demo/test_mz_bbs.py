#coding=utf-8
from pyse import Pyse
from time import sleep

driver = Pyse("chrome")

driver.open("http://bbs.meizu.cn")
driver.type("//*[@name='srchtxt']",u"手机")
driver.open_new_window("//*[@name='searchsubmit']")
sleep(2)
print driver.get_title()
driver.quit()
