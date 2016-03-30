# coding=utf-8
import pyse
from time import sleep

def test_baidu():
    ''' baidu search key : pyse '''
    driver = pyse.Pyse("chrome")
    driver.open("https://www.baidu.com")
    driver.type("#kw","pyse")
    driver.click("#su")
    sleep(1)
    title = driver.get_title()
    assert title=="pyse_百度搜索"
    driver.quit()

if __name__ == '__main__':
    test_pro = pyse.TestRunner()
    test_pro.run()