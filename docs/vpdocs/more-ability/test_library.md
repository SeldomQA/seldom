# 支持更多测试库

seldom 集成了`selenium`、`appium`、`requests`，他们都是非常优秀且成熟的库，这并不是说，你不能在seldom使用其他的测试库。

seldom 作为一个测试框架，理论上可以与任何测试库一起使用。seldom提供的基础能力（数据驱动、随机数、测试报告、缓存...等）同样可以提升这些测试库的使用效率。

### 使用playwright

playwright就微软推出的优秀的 web UI 自动化测试库。

官方地址: https://playwright.dev/

* pip安装Playwright

```shell
> pip install playwright
```

* playwright 安装浏览器以及驱动

```shell
> playwright install
```

* 使用例子

```python
import seldom
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class Playwright(seldom.TestCase):

    def start(self):
        self.p = sync_playwright().start()
        self.chromium = self.p.chromium.launch()
        self.page = self.chromium.new_page()

    def end(self):
        self.chromium.close()
        self.p.stop()

    def test_playwright_start(self):
        """
        test playwright index page
        """
        self.page.goto("http://playwright.dev")
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

        get_started = self.page.locator('text=Get Started')
        expect(get_started).to_have_attribute('href', '/docs/intro')
        get_started.click()

        expect(self.page).to_have_url('http://playwright.dev/docs/intro')
        # 截图
        screenshot_bytes = self.page.screenshot()
        self.screenshots(image=screenshot_bytes)

    def test_playwright_todo(self):
        """
        test playwright todoMVC
        """
        self.page.goto("https://demo.playwright.dev/todomvc/#/")
        new_todo = self.page.locator(".new-todo")
        new_todo.fill("sleep")
        new_todo.press("Enter")
        new_todo.fill("code")
        new_todo.press("Enter")
        new_todo.fill("eat")
        new_todo.press("Enter")
        self.page.locator('li').filter(has_text='code').get_by_label('Toggle Todo').check()
        self.page.locator('li').filter(has_text='sleep').get_by_label('Toggle Todo').check()
        self.page.locator('li').filter(has_text='eat').get_by_label('Toggle Todo').check()
        # 截图
        screenshot_bytes = self.page.screenshot()
        self.screenshots(image=screenshot_bytes)


if __name__ == '__main__':
    seldom.main()
```

### 使用uiautomator2

uiautomator2是openatx推出的优秀的Android自动化测试工具，Api简单，同样得到广泛应用。

github地址: https://github.com/openatx/uiautomator2

* pip安装

```shell
pip install uiautomator2
```

* 使用例子

```python
import seldom
from seldom.extend_lib.adb import get_devices
import uiautomator2 as u2


class MyAppTest(seldom.TestCase):

    def start(self):
        # 链接设备
        self.d = u2.connect(self.device)
        # 启动App
        self.d.app_start("com.microsoft.bing")

    def end(self):
        # 停止app
        self.d.app_stop("com.microsoft.bing")

    def test_bing_app(self):
        """ 使用 uiautomator2 """
        self.d(resourceId="com.microsoft.bing:id/sa_hp_header_search_box").click()
        self.d(resourceId="com.microsoft.bing:id/input_container").set_text("seldomQA")
        self.d(resourceId="com.microsoft.bing:id/input_container").center()
        # ....


if __name__ == '__main__':
    devices = get_devices()
    seldom.main(debug=True, device=devices[0][0])
```

### 使用pyAutoGUI

pyAutoGUI专注于模拟鼠标和键盘操作，实现GUI的自动化。
适用于需要在多个操作系统（Windows、macOS、Linux）上模拟用户输入（如点击、拖动、输入文本等）的场景，如自动化测试、数据录入、游戏辅助等。

官方地址: https://github.com/asweigart/pyautogui

* pip安装pyAutoGUI

```shell
> pip install pyautogui
```

* 使用例子

```python
import os
import pyautogui
import seldom
from seldom.testdata import get_int


class TestPyAutoGUINote(seldom.TestCase):

    def start(self):
        # 打开记事本（这里使用运行命令来打开，确保路径正确）
        os.system('notepad.exe')
        self.sleep()

    def end(self):
        # 模拟按下 Alt+F4 关闭记事本
        pyautogui.hotkey('alt', 'f4')

    def test_write_and_save(self):
        """
        打开一个新的标签页写入内容并保存
        """
        # 模拟按下 Ctrl+t 创建一个新的标签页
        pyautogui.hotkey('ctrl', 't')

        self.sleep()
        pyautogui.press('shift')  # 切换英文输入法

        # 写入字符串到记事本
        pyautogui.write('Hello, this is a test string written by pyautogui.', interval=0.1)  # interval 参数设置每个字符之间的延迟时间

        # 模拟按下 Ctrl+S 保存文件
        pyautogui.hotkey('ctrl', 's')
        self.sleep()

        # 切换英文输入法
        pyautogui.press('shift')
        self.sleep()

        # 输入文件名 + 回车确定
        pyautogui.write(f'test_file{get_int()}.txt')
        self.sleep()
        pyautogui.press('enter')
        self.sleep()


if __name__ == '__main__':
    seldom.main()
```

### 使用auto-wing

AI在自动化领域已经得到相关的应用，出现了不少项目（`browser-use`、`Midscene.js`
等）。auto-wing是一款基于LLM的自动化工具。可以很好的整合到seldom框架中使用。

GitHub地址: https://github.com/SeldomQA/auto-wing

* pip安装auto-wing

```shell
> pip install autowing
```

* 配置大模型 `API_key`

在脚本目录下创建`.env`文件，配置LLM的`API_key`， 支持多模型：`openai`、`deepseek`、`qwen` 和 `doubao`。这里以 `deepseek`为例。

```env
.env
AUTOWING_MODEL_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-abdefghijklmnopqrstwvwxyz0123456789
```

* 使用例子

```python
import seldom
from seldom import Seldom
from autowing.selenium.fixture import create_fixture
from dotenv import load_dotenv


class TestBingSearch(seldom.TestCase):

    @classmethod
    def start_class(cls):
        # load .env file
        load_dotenv()
        # Create AI fixture
        ai_fixture = create_fixture()
        cls.ai = ai_fixture(Seldom.driver)

    def test_bing_search(self):
        """
        Test Bing search functionality using AI-driven automation.
        """
        self.open("https://cn.bing.com")

        self.ai.ai_action('搜索输入框输入"playwright"关键字，并回车')
        self.sleep(3)

        items = self.ai.ai_query('string[], 搜索结果列表中包含"playwright"相关的标题')

        self.assertGreater(len(items), 1)

        self.assertTrue(
            self.ai.ai_assert('检查搜索结果列表第一条标题是否包含"playwright"字符串')
        )


if __name__ == '__main__':
    seldom.main(browser="edge", debug=True)
```

