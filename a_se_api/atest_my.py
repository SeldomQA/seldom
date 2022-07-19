from my_se import MySe

se = MySe()
se.open("https://www.baidu.com")
se.by_name("wd").send_keys("selenium")
se.by_id("su").click()
se.close()
