import seldom
from seldom import data
from seldom import skip
# from seldom.logging import log
#
# log.debug("abc")

# class BaiduTest(seldom.AppCase):
#
#     @skip()
#     def test_mweb(self):
#         """a simple test case """
#         self.open("https://m.baidu.com")
#
#         self.type(id_="index-kw", text="appium mobile web")
#         self.click(id_="index-bn")
#
#     def test_cal(self):
#         self.click(id_="com.android.calculator2:id/digit_1")
#         self.click(id_="com.android.calculator2:id/op_add")
#         self.click(id_="com.android.calculator2:id/digit_2")
#         self.click(id_="com.android.calculator2:id/eq")
#         text = self.get_text(id_="com.android.calculator2:id/result")
#         self.assertText(text, "3")
#
#     @skip()
#     def test_hybrid(self):
#         # # 获得当前上下文
#         # context = driver.context
#         # print(context)
#         #
#         # # 获得所有上下文
#         # all_context = driver.contexts
#         # for context in all_context:
#         #     print(context)
#
#         # 切换上下文
#         self.switch_to_web()
#
#         # 进入webview模式进行操作
#         self.type(id_="sb_form_q", text="appium mobile web")
#         self.click(id_="sbBtn")
#         self.sleep(2)
#
#
# if __name__ == '__main__':
#
#     # 原生应用
#     desired_caps = {
#         'deviceName': 'Android Emulator',
#         'automationName': 'Appium',
#         'platformName': 'Android',
#         'platformVersion': '7.0',
#         'appPackage': 'com.android.calculator2',
#         'appActivity': '.Calculator',
#         'noReset': True
#     }
#
#     # mweb应用
#     mweb = {
#         "deviceName": "Android Emulator",
#         "automationName": "Appium",
#         "platformName": "Android",
#         "platformVersion": "7.0",
#         "browserName": "Chrome"
#     }
#
#     # 混合应用
#     caps = {
#         "deviceName": "Android Emulator",
#         "automationName": "Appium",
#         "platformName": "Android",
#         "platformVersion": "7.0",
#         "appPackage": "com.example.webview",
#         "appActivity": ".MainActivity"
#     }
#
#     seldom.app(desired_capabilities=desired_caps)
#
