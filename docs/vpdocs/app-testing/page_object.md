# Page Object

在编写App自动化测试时，推荐使用`page object models`(简称 PO设计模式)。你可以看到seldom并没有完全封装appium的API，我们可以借助
poium 来实现基于元素的定位。

github: https://github.com/SeldomQA/poium

__pip 安装__

```shell
> pip install poium
```

__使用poium__

在seldom中基于poium实现元素的定位和操作。

```python
import seldom
from seldom.appium_lab.android import UiAutomator2Options
from poium import Page, Element, Elements


class BBSPage(Page):
    search_input = Element(id_="com.meizu.flyme.flymebbs:id/nw")
    search_button = Element(id_="com.meizu.flyme.flymebbs:id/o1")
    search_result = Elements(id_="com.meizu.flyme.flymebbs:id/a29")


class TestBBS(seldom.TestCase):

    def start(self):
        self.bbs_page = BBSPage(self.driver)

    def test_bbs(self):
        self.sleep(5)
        self.bbs_page.search_input.click()
        self.bbs_page.search_input.send_keys("flyme")
        self.bbs_page.search_button.click()
        elems = self.bbs_page.search_result
        for title in elems:
            self.assertIn("flyme", title.text.lower())


if __name__ == '__main__':
    # 定义运行App
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

__定位方法__

poium 支持的定位方法。

```shell
# selenium
css = "xx"
id_ = "xx"
name = "xx"
xpath = "xx"
link_text = "xx"
partial_link_text = "xx"
tag = "xx"
class_name = "xx"

# appium
ios_uiautomation = "xx"
ios_predicate = "xx"
ios_class_chain = "xx"
android_uiautomator = "xx"
android_viewtag = "xx"
android_data_matcher = "xx"
android_view_matcher = "xx"
windows_uiautomation = "xx"
accessibility_id = "xx"
image = "xx"
custom = "xx"
```

__`Element`类参数__

* timeout: 设置超时检查次数，默认为5。
* index: 设置元素索引，当你的定位方式默认匹配到多个元素时，默认返回第1个，即为0.
* describe: 设置元素描述，默认为undefined, 建议为每个元素增加描述。
