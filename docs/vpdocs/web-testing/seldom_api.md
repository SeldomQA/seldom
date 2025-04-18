# Seldom API

### 查找元素

seldom 提供了8中定位方式，与Selenium保持一致。

* id_
* name
* class_name
* tag
* link_text
* partial_link_text
* css
* xpath

__使用方式__

```python
# **kwargs
self.type(id_="kw", text="seldom")
self.type(name="wd", text="seldom")
self.type(class_name="s_ipt", text="seldom")
self.type(tag="input", text="seldom")
self.type(xpath="//input[@id='kw']", text="seldom")
self.type(css="#kw", text="seldom")
self.click(link_text="hao123")
self.click(partial_link_text="hao")

# selector
self.type("id=kw", text="seldom")
self.type("name=wd", text="seldom")
self.type("class=s_ipt", text="seldom")
self.type("tag=input", text="seldom")
self.type("//input[@id='kw']", text="seldom")  # xpath
self.type("#kw", text="seldom")  # css
self.click("text=hao123")
self.click("text*=hao")
```

> seldom 3.10.0 引入新的 selector 定位，弱化了selenium/appium 的定位类型方式。

* `**kwargs` 和 `selector` 定位对比。

| 类型              | 定位                   | **kwargs                    | selector                  |
|-----------------|----------------------|-----------------------------|---------------------------|
| selenium/appium | id                   | id_="id"                    | "id=id"                   |
| selenium        | mame                 | name="name"                 | "name=name"               |
| selenium/appium | class                | class_name="class"          | "class=class"             |
| selenium        | tag                  | tag="input"                 | "tag=input"               |
| selenium        | link_text            | link_text="文字链接"            | "text=文字链接"               |
| selenium        | partial_link_text    | partial_link_text="文字链"     | "text~=文字链"               |
| selenium/appium | xpath                | xpath="//*[@id='11']"       | "//*[@id='11']"           |
| selenium        | css                  | css="input#id"              | "input#id"                |
| appium          | ios_predicate        | ios_predicate = "xx"        | "ios_predicate=xx"        |
| appium          | ios_class_chain      | ios_class_chain = "xx"      | "ios_predicate=xx"        |
| appium          | android_uiautomator  | android_uiautomator = "xx"  | "android_uiautomator=xx"  |
| appium          | android_viewtag      | android_viewtag = "xx"      | "android_viewtag=xx"      |
| appium          | android_data_matcher | android_data_matcher = "xx" | "android_data_matcher=xx" |
| appium          | android_view_matcher | android_view_matcher = "xx" | "android_view_matcher=xx" |
| appium          | accessibility_id     | accessibility_id = "xx"     | "accessibility_id=xx"     |
| appium          | image                | image = "xx"                | "image=xx"                |
| appium          | custom               | custom = "xx"               | "custom=xx"               |

__帮助信息__

* [CSS选择器](https://www.w3school.com.cn/cssref/css_selectors.asp)
* [xpath语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

__使用下标__

有时候无法通过一种定位找到单个元素，那么可以通过`index`指定一组元素中的第几个。

```py
self.type(tag="input", index=7, text="seldom")
```

通过`tag="input"`匹配出一组元素， `index=7` 指定这一组元素中的第8个，`index`默认下标为`0`。

### 断言

seldom 提供了一组针对Web页面的断言方法。

__使用方法__

```python
# 断言标题是否等于"title"
self.assertTitle("title")

# 断言标题是否包含"title"
self.assertInTitle("title")

# 断言URL是否等于
self.assertUrl("url")

# 断言URL是否包含
self.assertInUrl("url")

# 断言页面包含“text”
self.assertText("text")

# 断言页面不包含“text”
self.assertNotText("text")

# 断言警告是否存在"text" 提示信息
self.assertAlertText("text")

# 断言元素是否存在
self.assertElement(css="#kw")

# 断言元素是否不存在
self.assertNotElement(css="#kwasdfasdfa")
```

### WebDriver API

seldom简化了selenium中的API，使操作Web页面更加简单。

大部分API都由`WebDriver`类提供：

```python
import seldom


class TestCase(seldom.TestCase):

    def test_seldom_api(self):
        # Accept warning box. ->  Be removed in the future
        self.accept_alert()

        # Adds a cookie to your current session.
        self.add_cookie({'name': 'foo', 'value': 'bar'})

        # Adds a cookie to your current session.
        cookie_list = [
            {'name': 'foo', 'value': 'bar'},
            {'name': 'foo', 'value': 'bar'}
        ]
        self.add_cookies(cookie_list)

        # Clear the contents of the input box.
        self.clear(css="#el")

        # It can click any text / image can be clicked
        # Connection, check box, radio buttons, and even drop-down box etc..
        self.click(css="#el")

        # Mouse over the element.
        self.move_to_element(css="#el")

        # Click the element by the link text
        self.click_text("新闻")

        # Simulates the user clicking the "close" button in the titlebar of a popup window or tab.
        self.close()

        # Delete all cookies in the scope of the session.
        self.delete_all_cookies()

        # Deletes a single cookie with the given name.
        self.delete_cookie('my_cookie')

        # Dismisses the alert available.  ->  Be removed in the future
        self.dismiss_alert()

        # Double click element.
        self.double_click(css="#el")

        # Execute JavaScript scripts.
        self.execute_script("window.scrollTo(200,1000);")

        # Setting width and height of window scroll bar.
        self.window_scroll(width=300, height=500)

        # Setting width and height of element scroll bar.
        self.element_scroll(css=".class", width=300, height=500)

        # open url.
        self.open("https://www.baidu.com")

        # Gets the text of the Alert.  ->  Be removed in the future
        alert_title = self.get_alert_text

        # Execute Chrome Devtools Protocol command and get returned result 
        self.execute_cdp_cmd('Runtime.evaluate', {'expression': "alert('hello world')"})

        # Gets the value of an element attribute.
        self.get_attribute(css="#el", attribute="type")

        # Returns information of cookie with ``name`` as an object.
        self.get_cookie(name="kkk")

        # Returns a set of dictionaries, corresponding to cookies visible in the current session.
        self.get_cookies()

        # Gets the element to display,The return result is true or false.
        self.get_display(css="#el")

        # Get a set of elements
        self.get_element(css="#el", index=0)

        # Get element text information.
        self.get_text(css="#el")

        # Get window title.
        title = self.get_title

        # Get the URL address of the current page.
        url = self.get_url

        # Gets the log for a given log type
        logs = self.get_log("browser")

        # Set browser window maximized.
        self.max_window()

        # open url.
        self.open("https://www.baidu.com")

        # Quit the driver and close all the windows.
        self.quit()

        # Refresh the current page.
        self.refresh()

        # Right click element.
        self.right_click(css="#el")

        # Saves a screenshots of the current window to a PNG image file.
        self.screenshots()  # Save to HTML report
        self.screenshots('/Screenshots/foo.png')  # Save to the specified directory

        # Saves a element screenshot of the element to a PNG image file.
        self.element_screenshot(css="#id")  # Save to HTML report
        self.element_screenshot(css="#id", file_path='/Screenshots/foo.png')  # Save to the specified directory

        """
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.
        <select name="NR" id="nr">
            <option value="10" selected="">每页显示10条</option>
            <option value="20">每页显示20条</option>
            <option value="50">每页显示50条</option>
        </select>
        """
        self.select(css="#nr", value='20')
        self.select(css="#nr", text='每页显示20条')
        self.select(css="#nr", index=2)

        # Set browser window wide and high.
        self.set_window(100, 200)

        # Submit the specified form.
        self.submit(css="#el")

        # Switch to the specified frame.
        self.switch_to_frame(css="#el")

        # Switches focus to the parent context. If the current context is the top
        # level browsing context, the context remains unchanged.
        self.switch_to_frame_parent()

        # Returns the current form machine form at the next higher level.
        # Corresponding relationship with switch_to_frame () method.
        self.switch_to_frame_out()

        # Switches focus to the specified window.
        # This switches to the new windows/tab (0 is the first one)
        self.switch_to_window(1)

        # Operation input box.
        self.type(css="#el", text="selenium")

        # Implicitly wait.All elements on the page.
        self.wait(10)

        # Setting width and height of window scroll bar.
        self.window_scroll(width=300, height=500)

        # alert operation. (seldom>=3.2.0)
        text = self.alert.text
        self.alert.accept()
        self.alert.dismiss()
        self.alert.send_keys("text")

```

### 键盘操作

有时候我们需要用到键盘操作，比如`Enter`，`Backspace`，`TAB`，或者`ctrl/command + a`、`ctrl/command + c`组合键操作，seldom提供了一组键盘操作。

__使用方法__

```py
import seldom


class Test(seldom.TestCase):

    def test_key(self):
        self.open("https://www.baidu.com")

        # 输入 seldomm
        self.Keys(css="#kw").input("seldomm")

        # 删除多输入的一个m
        self.Keys(id_="kw").backspace()

        # 输入“教程”
        self.Keys(id_="kw").input("教程")

        # ctrl+a 全选输入框内容
        self.Keys(id_="kw").select_all()

        # ctrl+x 剪切输入框内容
        self.Keys(id_="kw").cut()

        # ctrl+v 粘贴内容到输入框
        self.Keys(id_="kw").paste()

        # 通过回车键来代替单击操作
        self.Keys(id_="kw").enter()

        # 支持组合操作
        self.Keys(id_="kw").select_all().cut()  # 全选剪切
        self.Keys(id_="kw").select_all().delete()  # 全选删除


if __name__ == '__main__':
    seldom.main(browser="firefox", debug=True)

```

### 测试electron应用

Electron是一个使用 JavaScript、HTML 和 CSS 构建桌面应用程序的框架。 嵌入 Chromium 和 Node.js 到 二进制的 Electron 允许您保持一个
JavaScript代码代码库并创建 在Windows、macOS和Linux上运行的跨平台应用。

https://www.electronjs.org/

```python
import seldom


class DataDriverTest(seldom.TestCase):

    def start(self):
        # appium-desktop基于Electron开发的桌面应用
        self.app_path = f"C:\Program Files\Appium Server GUI\Appium Server GUI.exe"

    def test_case(self):
        """
        Used tuple test data
        """
        self.open_electron(app_path=self.app_path)
        self.sleep(10)
        self.switch_to_window(0)
        self.Keys(css="#simpleHostInput").select_all().delete()
        self.type(css="#simpleHostInput", text="127.0.0.1")
        self.Keys(css="#simplePortInput").select_all().delete()
        self.type(css="#simplePortInput", text="4724")
        self.click(css="#startServerBtn")
        self.sleep(5)


if __name__ == '__main__':
    seldom.main(debug=True)
```