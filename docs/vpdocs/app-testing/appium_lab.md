# appium API

appium API继承 selenium API，所以，操作方法是通用的。在seldom 中，请参考web UI 中的seldom API。

## appium 定位

* 支持定位类型

seldom 支持定位如下，包括selenium/appium。

| 类型              | 定位                   | **kwargs                    |
|-----------------|----------------------|-----------------------------|
| selenium/appium | id                   | id_="id"                    |
| selenium        | mame                 | name="name"                 |
| selenium/appium | class                | class_name="class"          |
| selenium        | tag                  | tag="input"                 |
| selenium        | link_text            | link_text="文字链接"            |
| selenium        | partial_link_text    | partial_link_text="文字链"     |
| selenium/appium | xpath                | xpath="//*[@id='11']"       |
| selenium        | css                  | cass="input#id"             |
| appium          | ios_uiautomation     | ios_uiautomation = "xx"     |
| appium          | ios_predicate        | ios_predicate = "xx"        |
| appium          | ios_class_chain      | ios_class_chain = "xx"      |
| appium          | android_uiautomator  | android_uiautomator = "xx"  |
| appium          | android_viewtag      | android_viewtag = "xx"      |
| appium          | android_data_matcher | android_data_matcher = "xx" |
| appium          | android_view_matcher | android_view_matcher = "xx" |
| appium          | windows_uiautomation | windows_uiautomation = "xx" |
| appium          | accessibility_id     | accessibility_id = "xx"     |
| appium          | image                | image = "xx"                |
| appium          | custom               | custom = "xx"               |

* 定位用法

```python
import seldom
from seldom.appium_lab.android import UiAutomator2Options


class TestBBS(seldom.TestCase):

    def test_bbs(self):
        """定位方法用法"""
        self.click(id_="com.meizu.flyme.flymebbs:id/nw")
        self.sleep(2)
        self.type(android_uiautomator='new UiSelector().resourceId("com.meizu.flyme.flymebbs:id/nw")', text="flyme")
        ...


if __name__ == '__main__':
    capabilities = {
        "automationName": "UiAutomator2",
        "platformName": "Android",
        "appPackage": "com.meizu.flyme.flymebbs",
        "appActivity": "com.meizu.myplus.ui.splash.SplashActivity",
        "noReset": True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(app_server="http://127.0.0.1:4723", app_info=options, debug=True)
```

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
    ...
```

* 启动appium server

```python
from seldom.appium_lab.appium_service import AppiumService

if __name__ == '__main__':
    # 启动 Appium Server
    app_ser = AppiumService(
        addr="127.0.0.1",
        port="4723",
        use_plugins="images",
        args=["--allow-cors", "--tmp", "C:\Windows\Temp"])
    app_ser.start_service()
```

参数说明：

* `addr`: appium server 地址, 默认： `127.0.0.1`
* `port`: appium server 端口， 默认：`4723`
* `log`: 设置 appium server 日志， 默认：`appium_server_1734493548.log`
* `use_plugins`: 设置使用的插件，默认None，不使用。
* `args`: 支持添加更多的参数，例如 `args=["--allow-cors", "--tmp", "C:\Windows\Temp"]`

启动日志：

```shell
2024-12-18 11:52:54 | INFO     | appium_service.py | MainThread | 🚀 launch appium server: ['--address', '127.0.0.1', '--port', '4723', '--log', 'D:\\github\\seldomQA\\seldom\\seldom\\appium_lab\\appium_server_1734493974.log', '--use-plugins', 'iamges,ocr', '--allow-cors']
```

`AppiumLab` 类中分以下几类操作:

__Action__

`Action`中提供基本滑动/触摸操作。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab()
# 触摸坐标位
appium_lab.tap(x=100, y=200)
# 上划
appium_lab.swipe_up()
# 下划
appium_lab.swipe_down()
# 左划
appium_lab.swipe_left()
# 右划
appium_lab.swipe_right()
# 从x坐标滑动到y坐标
appium_lab.drag_from_to()
```

__Switch__

`Switch`中提供基本上下文切换操作。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab()

# 返回当前上下文
context = appium_lab.context()
# 切换原生app
appium_lab.switch_to_app()
# 切换webview
appium_lab.switch_to_web()
# 切换flutter
appium_lab.switch_to_flutter()
# 切换OCR
appium_lab.switch_to_ocr()
```

__Find__

`Find`中提供基于文本的查找，一个元素可以没有ID、name，但一定有显示的文本，这里提供了一组基于文本的查找。

```python
from seldom.appium_lab import AppiumLab

appium_lab = AppiumLab()

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

appium_lab = AppiumLab()

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
        # 点击图片
        self.click_image("/you/path/xxx.png")

```

> 目前 seldom 集成的 appium API
> 并不完整，在使用过程中如有问题，欢迎提 [issues](https://github.com/SeldomQA/seldom/issues)。