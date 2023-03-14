# appium API

## appium lab

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

# 返回当前上下文
context = appium_lab.context()
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
# 返回当前窗口尺寸
size = appium_lab.size()
```

## appium driver

`AppDriver` 封装了App相关的操作。


```python
import seldom


class TestApp(seldom.TestCase):
    """
    Test App
    """

    def test_bbs_search(self):
        """
        appium api
        """
        # app置于后台10s
        self.background_app(10)
        # 检查设备上是否安装了应用程序
        self.is_app_installed("bundle_id")
        # 安装app
        self.install_app("/app/path/xxx.apk")
        # 删除app
        self.remove_app("app_id")
        # 启动app
        self.launch_app()
        # 关闭app
        self.close_app()
        # 如果app正在运行，终止运行
        self.terminate_app("app_id")
        # 如果app未运行，则激活它或者在后台运行
        self.activate_app("app_id")
        # 查询app 状态
        state = self.query_app_state("app_id")
        print(state)
        # 从指定的设备返回应用程序字符串语言
        language, string = self.app_strings()
        print(language, string)
        # 启动起app
        self.reset()

```

> 目前 seldom 集成的 appium API 并不完整，在使用过程中如有问题，欢迎提 [issues](https://github.com/SeldomQA/seldom/issues)。