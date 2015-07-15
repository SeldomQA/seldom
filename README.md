# pyse
WebUI automation testing framework based on Selenium

介绍：
  pyse基于selenium（webdriver）进行了简单的二次封装，比selenium提供的方法操作更简洁。
  
特点：
* 所有方法只xpath定位，webdriver提供了8种定位方法（id\name\class name\tag name\link text\partial link text\xpath\css selector）
但xpath一定程度可以替代id\name\class name\tag name 等方法，本框架所提供的click_text()方法可以替代link text方法，所以只用xpath
定位对不影响框架本身对元素的定位能力，又保证了定位方法的一致性。
* 本框架只是对selenium（webdriver）原方法的简单封装，大概30个方法，经过我的自动实践，这些方法完全够用于我们的自动化项目。
* 集成了HTMLTestRunner 测试报告，使生成报告变得很简单。

安装及前提条件：
Python2.7 :https://www.python.org/
selenium  :https://pypi.python.org/pypi/selenium
安装pyse ,将其克隆到本地，将pyse目录放到..\Python27\Lib\site-packages\目录下

例子：

