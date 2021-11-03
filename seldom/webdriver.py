# coding=utf-8
import time
import platform
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from seldom.logging import log
from seldom.running.config import Seldom
from seldom.logging.exceptions import NotFindElementError

__all__ = ["WebDriver"]


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


class WebElement(object):

    def __init__(self, **kwargs) -> None:
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        self.by, self.value = next(iter(kwargs.items()))
        try:
            LOCATOR_LIST[self.by]
        except KeyError:
            raise ValueError("Element positioning of type '{}' is not supported. ".format(self.by))
        self.find_elem_info = None
        self.find_elem_warn = None

    def __find_element(self, elem: tuple) -> None:
        """
        Find if the element exists.
        """
        for _ in range(Seldom.timeout):
            elems = Seldom.driver.find_elements(by=elem[0], value=elem[1])
            if len(elems) >= 1:
                self.find_elem_info = "Find {number} element: {by}={value} ".format(
                    number=str(len(elems)), by=elem[0], value=elem[1])
                break
            else:
                time.sleep(1)
        else:
            self.find_elem_warn = "❌ Find 0 element through: {by}={value}".format(
                by=elem[0], value=elem[1])

    def get_elements(self, index: int = None):
        """
        Judge element positioning way, and returns the element.
        """

        if self.by == "id_":
            self.__find_element((By.ID, self.value))
            elem = Seldom.driver.find_elements(By.ID, self.value)
        elif self.by == "name":
            self.__find_element((By.NAME, self.value))
            elem = Seldom.driver.find_elements(By.NAME, self.value)
        elif self.by == "class_name":
            self.__find_element((By.CLASS_NAME, self.value))
            elem = Seldom.driver.find_elements(By.CLASS_NAME, self.value)
        elif self.by == "tag":
            self.__find_element((By.TAG_NAME, self.value))
            elem = Seldom.driver.find_elements(By.TAG_NAME, self.value)
        elif self.by == "link_text":
            self.__find_element((By.LINK_TEXT, self.value))
            elem = Seldom.driver.find_elements(By.LINK_TEXT, self.value)
        elif self.by == "partial_link_text":
            self.__find_element((By.PARTIAL_LINK_TEXT, self.value))
            elem = Seldom.driver.find_elements(By.PARTIAL_LINK_TEXT, self.value)
        elif self.by == "xpath":
            self.__find_element((By.XPATH, self.value))
            elem = Seldom.driver.find_elements(By.XPATH, self.value)
        elif self.by == "css":
            self.__find_element((By.CSS_SELECTOR, self.value))
            elem = Seldom.driver.find_elements(By.CSS_SELECTOR, self.value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id_/name/class_name/tag/link_text/xpath/css'.")
        if index is None:
            return elem
        elif len(elem) == 0:
            raise NotFindElementError(self.find_elem_warn)
        else:
            return elem[index]

    @staticmethod
    def show_element(elem):
        """
        Show the elements of the operation
        :param elem:
        """
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
        else:
            for _ in range(2):
                Seldom.driver.execute_script(style_red, elem)
                time.sleep(0.1)
                Seldom.driver.execute_script(style_blue, elem)
                time.sleep(0.1)
            Seldom.driver.execute_script(style_blue, elem)
            time.sleep(0.3)
            Seldom.driver.execute_script(style_null, elem)

    @property
    def info(self):
        return self.find_elem_info

    @property
    def warn(self):
        return self.find_elem_warn


class WebDriver(object):
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

        def __init__(self, index: int  = 0, **kwargs) -> None:
            self.web_elem = WebElement(**kwargs)
            self.elem = self.web_elem.get_elements()
            self.web_elem.show_element(self.elem[index])

        def input(self, text="") -> None:
            log.info("✅ {info}, input '{text}'.".format(info=self.web_elem.info, text=text))
            self.elem.send_keys(text)

        def enter(self) -> None:
            log.info("✅ {info}, enter.".format(info=self.web_elem.info))
            self.elem.send_keys(Keys.ENTER)

        def select_all(self) -> None:
            log.info("✅ {info}, ctrl+a.".format(info=self.web_elem.info))
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "a")
            else:
                self.elem.send_keys(Keys.CONTROL, "a")

        def cut(self) -> None:
            log.info("✅ {info}, ctrl+x.".format(info=self.web_elem.info))
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "x")
            else:
                self.elem.send_keys(Keys.CONTROL, "x")

        def copy(self) -> None:
            log.info("✅ {info}, ctrl+c.".format(info=self.web_elem.info))
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "c")
            else:
                self.elem.send_keys(Keys.CONTROL, "c")

        def paste(self) -> None:
            log.info("✅ {info}, ctrl+v.".format(info=self.web_elem.info))
            if platform.system().lower() == "darwin":
                self.elem.send_keys(Keys.COMMAND, "v")
            else:
                self.elem.send_keys(Keys.CONTROL, "v")

        def backspace(self) -> None:
            log.info("✅ {info}, backspace.".format(info=self.web_elem.info))
            self.elem.send_keys(Keys.BACKSPACE)

        def delete(self) -> None:
            log.info("✅ {info}, delete.".format(info=self.web_elem.info))
            self.elem.send_keys(Keys.DELETE)

        def tab(self) -> None:
            log.info("✅ {info}, tab.".format(info=self.web_elem.info))
            self.elem.send_keys(Keys.TAB)

        def space(self) -> None:
            log.info("✅ {info}, space.".format(info=self.web_elem.info))
            self.elem.send_keys(Keys.SPACE)

    @staticmethod
    def visit(url: str) -> None:
        """
        visit url.

        Usage:
            self.visit("https://www.baidu.com")
        """
        log.info("📖 {}".format(url))
        if isinstance(Seldom.driver, SeleniumWebDriver) is False:
            Seldom.driver = Chrome()
        Seldom.driver.get(url)

    def open(self, url: str) -> None:
        """
        open url.

        Usage:
            self.open("https://www.baidu.com")
        """
        self.visit(url)

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

    def type(self, text: str, clear: bool = False, enter: bool = False, index: int = 0, **kwargs) -> None:
        """
        Operation input box.

        Usage:
            self.type(css="#el", text="selenium")
        """
        if clear is True:
            self.clear(index, **kwargs)
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info("✅ {info}, input '{text}'.".format(info=web_elem.info, text=text))
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
        log.info("✅ {info}, input '{text}' and enter.".format(info=web_elem.info, text=text))
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
        log.info("✅ {}, clear input.".format(web_elem.info))
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
        log.info("✅ {}, click.".format(web_elem.info))
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
        log.info("✅ {}, slow click.".format(web_elem.info))
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
        log.info("✅ {}, right click.".find(web_elem.info))
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
        log.info("✅ {}, move to element.".format(web_elem.info))
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
        log.info("✅ {}, click and hold.".format(web_elem.info))
        ActionChains(Seldom.driver).click_and_hold(elem).perform()

    @staticmethod
    def drag_and_drop_by_offset(index:int = 0, x: int = 0, y: int = 0, **kwargs) -> None:
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
        log.info("✅ {}, drag and drop by offset.".format(web_elem.info))
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
        log.info("✅ {}, double click.".format(web_elem.info))
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
        log.info("✅ {}, click link.".format(web_elem.info))
        elem.click()

    @staticmethod
    def close() -> None:
        """
        Closes the current window.

        Usage:
            self.close()
        """
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
        log.info("✅ {}, submit.".format(web_elem.info))
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
        js = "window.scrollTo({w},{h});".format(w=str(width), h=str(height))
        self.execute_script(js)

    def element_scroll(self, css: str, width: int = 0, height: int = 0) -> None:
        """
        Setting width and height of element scroll bar.

        Usage:
            self.element_scroll(css=".class", width=300, height=500)
        """
        scroll_life = 'document.querySelector("{css}").scrollLeft = {w};'.format(css=css, w=str(width))
        scroll_top = 'document.querySelector("{css}").scrollTop = {h};'.format(css=css, h=str(height))
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
        log.info("✅ {info}, get attribute：{att}.".format(info=web_elem.info, att=attribute))
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
        log.info("✅ {info}, get text: {text}.".format(info=web_elem.info, text=elem.text))
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
        log.info("✅ {info}, element is display: {r}.".format(info=web_elem.info, r=result))
        return result

    @property
    def get_title(self) -> str:
        """
        Get window title.

        Usage:
            self.get_title()
        """
        log.info("✅ get title: {}.".format(Seldom.driver.title))
        return Seldom.driver.title

    @property
    def get_url(self) -> str:
        """
        Get the URL address of the current page.

        Usage:
            self.get_url()
        """
        log.info("✅ get current url: {}.".format(Seldom.driver.current_url))
        return Seldom.driver.current_url

    @property
    def get_alert_text(self) -> str:
        """
        Gets the text of the Alert.

        Usage:
            self.get_alert_text()
        """
        log.info("✅ alert text: {}.".format(Seldom.driver.switch_to.alert.text))
        return Seldom.driver.switch_to.alert.text

    @staticmethod
    def wait(secs: int = 10) -> None:
        """
        Implicitly wait.All elements on the page.

        Usage:
            self.wait(10)
        """
        log.info("⌛️ implicitly wait: {}s.".format(str(secs)))
        Seldom.driver.implicitly_wait(secs)

    @staticmethod
    def accept_alert() -> None:
        """
        Accept warning box.

        Usage:
            self.accept_alert()
        """
        log.info("✅ accept alert.")
        Seldom.driver.switch_to.alert.accept()

    @staticmethod
    def dismiss_alert() -> None:
        """
        Dismisses the alert available.

        Usage:
            self.dismiss_alert()
        """
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
        log.info("✅ {}, switch to frame.".format(web_elem.info))
        Seldom.driver.switch_to.frame(elem)

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
        log.info("✅ switch to the {} window.".format(str(window)))
        all_handles = Seldom.driver.window_handles
        Seldom.driver.switch_to.window(all_handles[window])

    def screenshots(self, file_path: str = None) -> None:
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
        self.screenshots('/Screenshots/foo.png')
        """
        log.info("📷️  screenshot.")
        if file_path is None:
            self.images.append(Seldom.driver.get_screenshot_as_base64())
        else:
            Seldom.driver.save_screenshot(file_path)

    def screenshot(self, file_path: str = None, index: int = 0, **kwargs) -> None:
        """
        Saves a screenshot of the element to a PNG image file.

        Usage:
        self.screenshot(css="#id", file_path='/Screenshots/foo.png')
        """
        log.info("📷️ element screenshot.")
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        if file_path is None:
            self.images.append(elem.screenshot_as_base64)
        else:
            elem.screenshot(file_path)

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
        elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info("✅ {}, select option.".format(web_elem.info))
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
            self.add_cookie(cookie_list)
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
        log.info("💤️ sleep: {}s.".format(str(sec)))
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
        js = 'return document.querySelectorAll("{css}")'.format(css=css)
        ret = Seldom.driver.execute_script(js)
        if len(ret) > 0:
            for i in range(len(ret)):
                js = 'return document.querySelectorAll("{css}")[{i}].outerHTML;'.format(css=css, i=i)
                ret = Seldom.driver.execute_script(js)
                print("{} ->".format(i), ret)
        else:
            log.warn("No elements were found.")

    @staticmethod
    def get_elements(**kwargs):
        """
        Get a set of elements

        Usage:
        ret = self.get_elements(css="#el")
        print(len(ret))
        """
        web_elem = WebElement(**kwargs)
        elems = web_elem.get_elements()
        if len(elems) == 0:
            log.warn("{}.".format(web_elem.warn))
        else:
            log.info("✅ {}.".format(web_elem.info))
        return elems

    @staticmethod
    def get_element(index: int=0, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        web_elem = WebElement(**kwargs)
        elem = web_elem.get_elements(index)
        log.info("✅ {}.".format(web_elem.info))
        return elem
