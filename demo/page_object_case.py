#coding=utf-8
from pyse import Pyse
from time import sleep

class Page(object):
	'''
	基本类，用于所页面的继承
	'''
	login_url = 'http://www.126.com'

	def __init__(self, selenium_driver, base_url=login_url, parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent
	
	def _iopen(self,url):
		url = self.base_url + url
		self.driver.open(url)
		assert self.on_page(),'Did not land on %s' % url

	def iopen(self):
		self._iopen(self.url)

	def on_page(self):
		return self.driver.get_url() == (self.base_url + self.url)

class LoginPage(Page):
	'''
	126邮箱登录页面模型
	'''
	url = '/'
	
	def type_username(self,username):
		self.driver.type("//*[@id='idInput']",username)
	
	def type_password(self,password):
		self.driver.type("//*[@id='pwdInput']",password)
	
	def submit(self):
		self.driver.click("//*[@id='loginBtn']")


def test_user_login(driver, username, password):
	"""
	测试获取的用户名密码 是否可以登录
	"""
	login_page = LoginPage(driver)
	login_page.iopen()
	login_page.type_username(username)
	login_page.type_password(password)
	login_page.submit()


def main():
	try:
		driver = Pyse("chrome")
		username = 'testingwtb'
		password = 'a123456'
		test_user_login(driver, username, password)
		sleep(3)
		text = driver.get_text("//span[@id='spnUid']")
		assert(text == 'testingwtb@126.com'),u"用户名称不匹配，登录失败!"
	finally:
		# 关闭浏览器窗口
		driver.close()

if __name__ == '__main__':
	main()