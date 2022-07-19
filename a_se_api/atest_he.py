from he_se import HeSe

he = HeSe()
he.open("https://www.baidu.com").type(name="wd", text="selenium").click(id="su").close()
