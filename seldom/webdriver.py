"""
selenium webdriver API
"""
import os
import time
import warnings
import platform
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as cService
from appium.webdriver.common.appiumby import AppiumBy
from seldom.logging import log
from seldom.running.config import Seldom
from seldom.logging.exceptions import NotFindElementError
from seldom.utils.webdriver_manager_extend import ChromeDriverManager
from seldom.testdata import get_timestamp


__all__ = ["WebDriver", "WebElement"]


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
    'ios_uiautomation': AppiumBy.IOS_UIAUTOMATION,
    'ios_predicate': AppiumBy.IOS_PREDICATE,
    'ios_class_chain': AppiumBy.IOS_CLASS_CHAIN,
    'android_uiautomator': AppiumBy.ANDROID_UIAUTOMATOR,
    'android_viewtag': AppiumBy.ANDROID_VIEWTAG,
    'android_data_matcher': AppiumBy.ANDROID_DATA_MATCHER,
    'android_view_matcher': AppiumBy.ANDROID_VIEW_MATCHER,
    'windows_uiautomation': AppiumBy.WINDOWS_UI_AUTOMATION,
    'accessibility_id': AppiumBy.ACCESSIBILITY_ID,
    'image': AppiumBy.IMAGE,
    'custom': AppiumBy.CUSTOM,
}


class WebElement:
    """web element API"""

    def __init__(self, **kwargs) -> None:
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        by, self.value = next(iter(kwargs.items()))

        self.by = LOCATOR_LIST.get(by)
        if self.by is None:
            raise ValueError(f"The find element is not supported: {by}. ")
        self.find_elem_info = None
        self.find_elem_warn = None

    def get_elements(self, index: int = None, empty=False):
        """
        Judge element positioning way, and returns the element.
        """

        for _ in range(Seldom.timeout):
            elems = Seldom.driver.find_elements(by=self.by, value=self.value)
            if len(elems) >= 1:
                self.find_elem_info = f"Find {len(elems)} element: {self.by}={self.value} "
                break
            time.sleep(1)
        else:
            self.find_elem_warn = f"❌ Find 0 element through: {self.by}={self.value}"

        elem = Seldom.driver.find_elements(self.by, self.value)
        if len(elem) == 0 and empty is False:
            raise NotFindElementError(self.find_elem_warn)

        if len(elem) == 0 and empty is True:
            return []

        if index is None:
            return elem

        return elem[index]

    @staticmethod
    def show_element(elem) -> None:
        """
        Show the elements of the operation
        :param elem:
        """
        if (Seldom.app_server is not None) and (Seldom.app_info is not None):
            return None
        style_red = 'arguments[0].style.border="2px solid #FF0000"'
        style_blue = 'arguments[0].style.border="2px solid #00FF00"'
        style_null = 'arguments[0].style.border=""'
        if Seldom.debug is True:
            for _ in range(2):
                Seldom.driver.execute_script(style_red, elem)
                time.sleep(0.2)
                Seldom.driver.execute_script(style_blue, elem)
                time.sleep(0.2)
            Seldom.driver.execute_script(style_blue, elem)
            time.sleep(0.2)
            Seldom.driver.execute_script(style_null, elem)

    @property
    def info(self):
        """return element info"""
        return self.find_elem_info

    @property
    def warn(self):
        """return element warn"""
        return self.find_elem_warn


class WebDriver:
    """
        Seldom framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """

    class Keys:
        """
        Achieve keyboard shortcuts

        Usage:
            self.Keys(id_="kw").enter()
        """

        def __init__(self, index: int = 0, **kwargs) -> None:
            self.web_elem = WebElement(**kwargs)
            self.elem = self.web_elem.get_elements(index)
            self.web_elem.show_element(self.elem)

        def input(self, text="") -> None:
            log.info(f"✅ {self.web_elem.info}, input '{text}'.")
            self.elem.send_keys(text)

        def enter(self) -> None:
            log.info(f"✅ {self.web_elem.info}, enter.")
            self.elem.send_keys(Keys.ENTER)

        def select_all(self) -> None:
            log.info(f"✅ {self.web_elem.info}, ctrl+a.")
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "a")
            else:
                self.elem.send_keys(Keys.CONTROL, "a")

        def cut(self) -> None:
            log.info(f"✅ {self.web_elem.info}, ctrl+x.")
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "x")
            else:
                self.elem.send_keys(Keys.CONTROL, "x")

        def copy(self) -> None:
            log.info(f"✅ {self.web_elem.info}, ctrl+c.")
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "c")
            else:
                self.elem.send_keys(Keys.CONTROL, "c")

        def paste(self) -> None:
            log.info(f"✅ {self.web_elem.info}, ctrl+v.")
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "v")
            else:
                self.elem.send_keys(Keys.CONTROL, "v")

        def backspace(self) -> None:
            log.info(f"✅ {self.web_elem.info}, backspace.")
            self.elem.send_keys(Keys.BACKSPACE)

        def delete(self) -> None:
            log.info(f"✅ {self.web_elem.info}, delete.")
            self.elem.send_keys(Keys.DELETE)

        def tab(self) -> None:
            log.info(f"✅ {self.web_elem.info}, tab.")
            self.elem.send_keys(Keys.TAB)

        def space(self) -> None:
            log.info(f"✅ {self.web_elem.info}, space.")
            self.elem.send_keys(Keys.SPACE)

    class Alert:

        @property
        def text(self) -> str:
            """
            Gets the text of the Alert.
            """
            log.info(f"✅ alert text: {Seldom.driver.switch_to.alert.text}.")
            return Seldom.driver.switch_to.alert.text

        @staticmethod
        def dismiss() -> None:
            """
            Dismisses the alert available.
            """
            log.info("✅ dismiss alert.")
            return Seldom.driver.switch_to.alert.dismiss()

        @staticmethod
        def accept():
            """
            Accepts the alert available.

            Usage::
            Alert(driver).accept() # Confirm a alert dialog.
            """
            log.info("✅ accept alert.")
            return Seldom.driver.switch_to.alert.accept()

        @staticmethod
        def send_keys(text: str) -> None:
            """
            Send Keys to the Alert.

            :Args:
             - text: The text to be sent to Alert.
            """
            log.info(f"✅ input alert '{text}'.")
            return Seldom.driver.switch_to.alert.send_keys(text)

    @staticmethod
    def visit(url: str) -> None:
        """
        visit url.

        Usage:
            self.visit("https://www.baidu.com")
        """
        log.info(f"📖 {url}")
        if isinstance(Seldom.driver, SeleniumWebDriver) is False:
            Seldom.driver = Chrome(service=cService(ChromeDriverManager().install()))
        Seldom.driver.get(url)

    def open(self, url: str) -> None:
        """
        open url.

        Usage:
            self.open("https://www.baidu.com")
        """
        self.visit(url)

    @staticmethod
    def get_log(log_type: str):
        """
        Gets the log for a given log type

        :Usage:
            self.get_log('browser')
            self.get_log('driver')
            self.get_log('client')
            self.get_log('server')
        """
        return Seldom.driver.get_log(log_type)

    @staticmethod
    def max_window() -> None:
        """
        Set browser window maximized.

        Usage:
            self.max_window()
        """
        Seldom.driver.maximize_window()

    @staticmethod
    def set_window(wide: int = 0, high: int = 0) -> None:
        """
        Set browser window wide and high.

        Usage:
            self.set_window(wide,high)
        """
        Seldom.driver.set_window_size(wide, high)

    @staticmethod
    def get_windows() -> dict:
        """
         Gets the width and height of the current window.

        :Usage:
            driver.get_windows()
        """
        return Seldom.driver.get_window_size()

    def type(self, text: str, clear: bool = False, enter: bool = False, click: bool = False, index: int = 0, **kwargs) -> None:
        """
        Operation input box.

        Usage:
            self.type(css="#el", text="selenium")
        """
        if clear is True:
            self.clear(index, **kwargs)
        if click is True:
            self.click(index, **kwargs)
            self.sleep(0.5)
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> input '{text}'.")
        elem.send_keys(text)
        if enter is True:
            elem.send_keys(Keys.ENTER)

    def type_enter(self, text: str, clear: bool = False, index: int = 0, **kwargs) -> None:
        """
        Enter text and enter directly.

        Usage:
            self.type_enter(css="#el", text="selenium")
        """
        if clear is True:
            self.clear(index, **kwargs)
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> input '{text}' and enter.")
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)

    @staticmethod
    def clear(index: int = 0, **kwargs) -> None:
        """
        Clear the contents of the input box.

        Usage:
            self.clear(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> clear input.")
        elem.clear()

    @staticmethod
    def click(index: int = 0, **kwargs) -> None:
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
            self.click(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> click.")
        elem.click()

    @staticmethod
    def slow_click(index: int = 0, **kwargs) -> None:
        """
        Moving the mouse to the middle of an element. and click element.

        Usage:
            self.slow_click(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> slow click.")
        ActionChains(Seldom.driver).move_to_element(elem).click(elem).perform()

    @staticmethod
    def right_click(index: int = 0, **kwargs) -> None:
        """
        Right click element.

        Usage:
            self.right_click(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> right click.")
        ActionChains(Seldom.driver).context_click(elem).perform()

    @staticmethod
    def move_to_element(index: int = 0, **kwargs) -> None:
        """
        Mouse over the element.

        Usage:
            self.move_to_element(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> move to element.")
        ActionChains(Seldom.driver).move_to_element(elem).perform()

    @staticmethod
    def click_and_hold(index: int = 0, **kwargs) -> None:
        """
        Mouse over the element.

        Usage:
            self.move_to_element(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> click and hold.")
        ActionChains(Seldom.driver).click_and_hold(elem).perform()

    @staticmethod
    def drag_and_drop_by_offset(index: int = 0, x: int = 0, y: int = 0, **kwargs) -> None:
        """
        Holds down the left mouse button on the source element,
           then moves to the target offset and releases the mouse button.

        :Args:
         - source: The element to mouse down.
         - x: X offset to move to.
         - y: Y offset to move to.
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        action = ActionChains(Seldom.driver)
        log.info(f"✅ {web_elem.info} -> drag and drop by offset.")
        action.drag_and_drop_by_offset(elem, x, y).perform()

    @staticmethod
    def double_click(index: int = 0, **kwargs) -> None:
        """
        Double click element.

        Usage:
            self.double_click(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> double click.")
        ActionChains(Seldom.driver).double_click(elem).perform()

    @staticmethod
    def click_text(text: str, index: int = 0) -> None:
        """
        Click the element by the link text

        Usage:
            self.click_text("新闻")
        """
        web_elem = WebElement(link_text=text)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> click link.")
        elem.click()

    @staticmethod
    def close() -> None:
        """
        Closes the current window.

        Usage:
            self.close()
        """
        if isinstance(Seldom.driver, SeleniumWebDriver) is True:
            Seldom.driver.close()

    @staticmethod
    def quit() -> None:
        """
        Quit the driver and close all the windows.

        Usage:
            self.quit()
        """
        Seldom.driver.quit()

    @staticmethod
    def submit(index: int = 0, **kwargs) -> None:
        """
        Submit the specified form.

        Usage:
            driver.submit(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> submit.")
        elem.submit()

    @staticmethod
    def refresh() -> None:
        """
        Refresh the current page.

        Usage:
            self.refresh()
        """
        log.info("🔄️ refresh page.")
        Seldom.driver.refresh()

    @staticmethod
    def execute_script(script: str, *args):
        """
        Execute JavaScript scripts.

        Usage:
            self.execute_script("window.scrollTo(200,1000);")
        """
        return Seldom.driver.execute_script(script, *args)

    def window_scroll(self, width: int = 0, height: int = 0) -> None:
        """
        Setting width and height of window scroll bar.

        Usage:
            self.window_scroll(width=300, height=500)
        """
        js = f"window.scrollTo({width},{height});"
        self.execute_script(js)

    def element_scroll(self, css: str, width: int = 0, height: int = 0) -> None:
        """
        Setting width and height of element scroll bar.

        Usage:
            self.element_scroll(css=".class", width=300, height=500)
        """
        scroll_life = f'document.querySelector("{css}").scrollLeft = {width};'
        scroll_top = f'document.querySelector("{css}").scrollTop = {height};'
        self.execute_script(scroll_life)
        self.execute_script(scroll_top)

    @staticmethod
    def get_attribute(attribute=None, index: int = 0, **kwargs) -> str:
        """
        Gets the value of an element attribute.

        Usage:
            self.get_attribute(css="#el", attribute="type")
        """
        if attribute is None:
            raise ValueError("attribute is not None")
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> get attribute：{attribute}.")
        return elem.get_attribute(attribute)

    @staticmethod
    def get_text(index: int = 0, **kwargs) -> str:
        """
        Get element text information.

        Usage:
            self.get_text(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> get text: {elem.text}.")
        return elem.text

    @staticmethod
    def get_display(index: int = 0, **kwargs) -> bool:
        """
        Gets the element to display,The return result is true or false.

        Usage:
            self.get_display(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        result = elem.is_displayed()
        log.info(f"✅ {web_elem.info} -> element is display: {result}.")
        return result

    @property
    def get_title(self) -> str:
        """
        Get window title.

        Usage:
            self.get_title()
        """
        log.info(f"✅ get title: {Seldom.driver.title}.")
        return Seldom.driver.title

    @property
    def get_url(self) -> str:
        """
        Get the URL address of the current page.

        Usage:
            self.get_url()
        """
        log.info(f"✅ get current url: {Seldom.driver.current_url}.")
        return Seldom.driver.current_url

    @property
    def alert(self) -> Alert:
        """return Alert class"""
        alert = self.Alert()
        return alert

    @property
    def get_alert_text(self) -> str:
        """
        Gets the text of the Alert.

        Usage:
            self.get_alert_text()
        """
        warnings.warn("use self.alert.text instead", DeprecationWarning, stacklevel=2)
        log.info(f"✅ alert text: {Seldom.driver.switch_to.alert.text}.")
        return Seldom.driver.switch_to.alert.text

    @staticmethod
    def wait(secs: int = 10) -> None:
        """
        Implicitly wait.All elements on the page.

        Usage:
            self.wait(10)
        """
        log.info(f"⌛️ implicitly wait: {secs}s.")
        Seldom.driver.implicitly_wait(secs)

    @staticmethod
    def accept_alert() -> None:
        """
        Accept warning box.

        Usage:
            self.accept_alert()
        """
        warnings.warn("use self.alert.accept() instead", DeprecationWarning, stacklevel=2)
        log.info("✅ accept alert.")
        Seldom.driver.switch_to.alert.accept()

    @staticmethod
    def dismiss_alert() -> None:
        """
        Dismisses the alert available.

        Usage:
            self.dismiss_alert()
        """
        warnings.warn("use self.alert.dismiss() instead", DeprecationWarning, stacklevel=2)
        log.info("✅ dismiss alert.")
        Seldom.driver.switch_to.alert.dismiss()

    @staticmethod
    def switch_to_frame(index: int = 0, **kwargs) -> None:
        """
        Switch to the specified frame.

        Usage:
            self.switch_to_frame(css="#el")
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> switch to frame.")
        Seldom.driver.switch_to.frame(elem)

    @staticmethod
    def switch_to_frame_parent() -> None:
        """
        Switches focus to the parent context. If the current context is the top
        level browsing context, the context remains unchanged.

        Usage:
            self.switch_to_frame_parent()
        """
        log.info("✅ switch to parent frame.")
        Seldom.driver.switch_to.parent_frame()

    @staticmethod
    def switch_to_frame_out() -> None:
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
            self.switch_to_frame_out()
        """
        log.info("✅ switch to frame out.")
        Seldom.driver.switch_to.default_content()

    @staticmethod
    def switch_to_window(window: int) -> None:
        """
        Switches focus to the specified window.

        :Args:
         - window: window index. 1 represents a newly opened window (0 is the first one)

        :Usage:
            self.switch_to_window(1)
        """
        log.info(f"✅ switch to the {window} window.")
        all_handles = Seldom.driver.window_handles
        Seldom.driver.switch_to.window(all_handles[window])

    @staticmethod
    def switch_to_new_window(type_hint=None) -> None:
        """
        Switches to a new top-level browsing context.

        The type hint can be one of "tab" or "window". If not specified the
        browser will automatically select it.

        :Usage:
            self.switch_to_new_window('tab')
        """
        log.info("✅ switch to new window.")
        Seldom.driver.switch_to.new_window(type_hint=type_hint)

    @staticmethod
    def save_screenshot(file_path: str = None, index: int = 0, **kwargs) -> None:
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
            self.save_screenshot()
            self.save_screenshot('/Screenshots/foo.png')
            self.save_screenshot(id_="bLogo", index=0)
        """

        if file_path is None:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, get_timestamp() + ".png")

        if len(kwargs) == 0:
            log.info(f"📷️  screenshot -> ({file_path}).")
            Seldom.driver.save_screenshot(file_path)
        else:
            log.info(f"📷️  element screenshot -> ({file_path}).")
            web_elem = WebElement(**kwargs)
            elem = web_elem.get_elements(index)
            elem.screenshot(file_path)

    def screenshots(self) -> None:
        """
        Saves a screenshots of the current window to HTML report.

        Usage:
            self.screenshots()
        """
        if Seldom.debug is True:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, get_timestamp() + ".png")
            log.info(f"📷️  screenshot -> ({file_path}).")
            Seldom.driver.save_screenshot(file_path)
        else:
            log.info("📷️  screenshot -> HTML report.")
            self.images.append(Seldom.driver.get_screenshot_as_base64())

    def element_screenshot(self, index: int = 0, **kwargs) -> None:
        """
        Saves an element screenshot of the element to HTML report.

        Usage:
            self.element_screenshot(css="#id")
            self.element_screenshot(css="#id", index=0)
        """

        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        if Seldom.debug is True:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, get_timestamp() + ".png")
            log.info(f"📷️ element screenshot -> ({file_path}).")
            elem.screenshot(file_path)
        else:
            log.info("📷️ element screenshot -> HTML Report.")
            self.images.append(elem.screenshot_as_base64)

    @staticmethod
    def select(value: str = None, text: str = None, index: int = None, **kwargs) -> None:
        """
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against

        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>

            self.select(css="#nr", value='20')
            self.select(css="#nr", text='每页显示20条')
            self.select(css="#nr", index=2)
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(0)
        web_elem.show_element(elem)
        log.info(f"✅ {web_elem.info} -> select option.")
        if value is not None:
            Select(elem).select_by_value(value)
        elif text is not None:
            Select(elem).select_by_visible_text(text)
        elif index is not None:
            Select(elem).select_by_index(index)
        else:
            raise ValueError(
                '"value" or "text" or "index" options can not be all empty.')

    @staticmethod
    def get_cookies() -> list:
        """
        Returns a set of dictionaries, corresponding to cookies visible in the current session.
        Usage:
            self.get_cookies()
        """
        return Seldom.driver.get_cookies()

    @staticmethod
    def get_cookie(name: str) -> dict:
        """
        Returns information of cookie with ``name`` as an object.
        Usage:
            self.get_cookie("name")
        """
        return Seldom.driver.get_cookie(name)

    @staticmethod
    def add_cookie(cookie_dict: dict) -> None:
        """
        Adds a cookie to your current session.
        Usage:
            self.add_cookie({'name' : 'foo', 'value' : 'bar'})
        """
        if isinstance(cookie_dict, dict):
            Seldom.driver.add_cookie(cookie_dict)
        else:
            raise TypeError("Wrong cookie type.")

    @staticmethod
    def add_cookies(cookie_list: list) -> None:
        """
        Adds a cookie to your current session.
        Usage:
            cookie_list = [
                {'name' : 'foo', 'value' : 'bar'},
                {'name' : 'foo', 'value' : 'bar'}
            ]
            self.add_cookies(cookie_list)
        """
        if isinstance(cookie_list, list):
            for cookie in cookie_list:
                if isinstance(cookie, dict):
                    Seldom.driver.add_cookie(cookie)
                else:
                    raise TypeError("Wrong cookie type.")
        else:
            raise TypeError("Wrong cookie type.")

    @staticmethod
    def delete_cookie(name: str) -> None:
        """
        Deletes a single cookie with the given name.
        Usage:
            self.delete_cookie('my_cookie')
        """
        Seldom.driver.delete_cookie(name)

    @staticmethod
    def delete_all_cookies() -> None:
        """
        Delete all cookies in the scope of the session.
        Usage:
            self.delete_all_cookies()
        """
        Seldom.driver.delete_all_cookies()

    @staticmethod
    def sleep(sec: int) -> None:
        """
        Usage:
            self.sleep(seconds)
        """
        log.info(f"💤️ sleep: {sec}s.")
        time.sleep(sec)

    @staticmethod
    def check_element(css: str = None) -> None:
        """
        Check that the element exists

        Usage:
        self.check_element(css="#el")
        """
        if css is None:
            raise NameError("Please enter a CSS selector")

        log.info("👀 check element.")
        js = f'return document.querySelectorAll("{css}")'
        ret = Seldom.driver.execute_script(js)
        if len(ret) > 0:
            for i in range(len(ret)):
                js = f'return document.querySelectorAll("{css}")[{i}].outerHTML;'
                ret = Seldom.driver.execute_script(js)
                log.info(f"{i} -> {ret}")
        else:
            log.warning("No elements were found.")

    @staticmethod
    def get_elements(**kwargs):
        """
        Get a set of elements

        Usage:
        ret = self.get_elements(css="#el")
        print(len(ret))
        """
        web_elem = WebElement(**kwargs)
        elems = web_elem.get_elements(empty=True)
        if len(elems) == 0:
            log.warning(f"{web_elem.warn}.")
        else:
            log.info(f"✅ {web_elem.info}.")
        return elems

    @staticmethod
    def get_element(index: int = 0, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        log.info(f"✅ {web_elem.info}.")
        return elem

    @staticmethod
    def switch_to_app() -> None:
        """
        appium API
        Switch to native app.
        """
        log.info("🔀 switch to native app.")
        current_context = Seldom.driver.current_context
        if current_context != "NATIVE_APP":
            Seldom.driver.switch_to.context('NATIVE_APP')

    @staticmethod
    def switch_to_web(context=None) -> None:
        """
        appium API
        Switch to web view.
        """
        log.info("🔀 switch to webview.")
        current_context = Seldom.driver.current_context
        if context is not None:
            Seldom.driver.switch_to.context(context)
        elif "WEBVIEW" in current_context:
            return
        else:
            all_context = Seldom.driver.contexts
            for context in all_context:
                if "WEBVIEW" in context:
                    Seldom.driver.switch_to.context(context)
                    break
            else:
                raise NameError("No WebView found.")

    @staticmethod
    def switch_to_flutter() -> None:
        """
        appium API
        Switch to flutter app.
        """
        log.info("🔀 switch to flutter.")
        current_context = Seldom.driver.current_context
        if current_context != "NATIVE_APP":
            Seldom.driver.switch_to.context('FLUTTER')
