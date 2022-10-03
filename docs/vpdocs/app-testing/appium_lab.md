# appium lab 

`appium_lab` 封装了常用App操作

* 基本用法

```python
import seldom
from seldom.appium_lab import AppiumLab


class TestBBS(seldom.TestCase):

    def start(self):
        # 导入 AppiumLab
        self.appium_lab = AppiumLab(self.driver)

    def test_bbs(self):
        # 点击输入框
        self.click(id_="com.meizu.flyme.flymebbs:id/nw")
        self.sleep(2)
        # 判断当前虚拟键盘是否显示
        keyboard = self.appium_lab.is_keyboard_shown()
        print(keyboard)
        # 收起当前键盘
        self.appium_lab.hide_keyboard()
        self.sleep(3)

if __name__ == '__main__':
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    seldom.main(app_info=desired_caps, app_server="http://127.0.0.1:4723", debug=True)
```

`AppiumLab` 类中分以下几类操作:

__Action__

`Action`中提供基本滑动/触摸操作。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab(self.driver)
# 触摸坐标位
appium_lab.tap(x=100, y=200)
# 上划
appium_lab.swipe_up()
# 下划
appium_lab.swipe_down()
```

__Switch__

`Switch`中提供基本上下文切换操作。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab(self.driver)

# 切换原生app
appium_lab.switch_to_app()
# 切换webview
appium_lab.switch_to_web()
# 切换flutter
appium_lab.switch_to_flutter()
```

__Find__

`Find`中提供基于文本的查找，一个元素可以没有ID、name，但一定有显示的文本，这里提供了一组基于文本的查找。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab(self.driver)

# Android
appium_lab.find_view(text="xxx标题").click()
appium_lab.find_view(content_desc="xxx标题").click()
appium_lab.find_edit_text(text="xxx标题").click()
appium_lab.find_button(text="xxx标题").click()
appium_lab.find_button(content_desc="xxx标题").click()
appium_lab.find_text_view(text="xxx标题").click()
appium_lab.find_image_view(text="xxx标题").click()
appium_lab.find_check_box(text="xxx标题").click()

# iOS
appium_lab.find_static_text(text="xxx标题").click()
appium_lab.find_other(text="xxx标题").click()
appium_lab.find_text_field(text="xxx标题").click()
appium_lab.find_image(text="xxx标题").click()
appium_lab.find_ios_button(text="xxx标题").click()
```


__keyboard__

`keyboard`中提供基于键盘的输入和操作。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab(self.driver)

# 基于键盘输入（支持大小写）
appium_lab.key_text("Hello123")
# 手机home键
appium_lab.home()
# 手机返回键
appium_lab.back()
# 判断当前虚拟键盘是否显示（True/False）
ret = appium_lab.is_keyboard_shown()
print(ret)
# 收起虚拟键盘
appium_lab.hide_keyboard()
```
