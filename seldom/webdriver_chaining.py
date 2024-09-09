"""
WebDriver chaining API
"""
import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from seldom.logging import log
from seldom.running.config import Seldom, BrowserConfig
from seldom.webdriver import WebElement
from seldom.testdata import get_timestamp
from seldom.driver import Browser

__all__ = ["Steps"]


class Steps:
    """
    WebDriver Basic method chaining
    Write test cases quickly.
    """

    def __init__(self, browser=None, url: str = None, desc: str = None, images: list = []):
        if browser is not None:
            self.browser = Browser(browser, BrowserConfig.executable_path, BrowserConfig.options,
                                   BrowserConfig.command_executor)
            Seldom.driver = self.browser
        else:
            self.browser = Seldom.driver
        self.url = url
        self.element_obj = None
        self.alert_obj = None
        self.desc = desc
        log.info(f"🔖 Test Case: {self.desc}")
        self.images = images

    def open(self, url: str = None):
        """
        open url.

        Usage:
            open("https://www.baidu.com")
        """
        if self.url is not None:
            log.info(f"📖 {self.url}")
            self.browser.get(self.url)
        else:
            log.info(f"📖 {url}")
            self.browser.get(url)
        return self

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
            max_window()
        """
        self.browser.maximize_window()
        return self

    def set_window(self, wide: int = 0, high: int = 0):
        """
        Set browser window wide and high.

        Usage:
            .set_window(wide,high)
        """
        self.browser.set_window_size(wide, high)
        return self

    def find(self, css: str, index: int = 0):
        """
        find element
        """
        if len(css) > 5 and css[:5] == "text=":
            web_elem = WebElement(self.browser, link_text=css[5:])
        elif len(css) > 6 and css[:6] == "text*=":
            web_elem = WebElement(self.browser, partial_link_text=css[6:])
        else:
            web_elem = WebElement(self.browser, css=css)
        self.element_obj = elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"🔍 find {web_elem.info}.")
        return self

    def find_text(self, text: str, index: int = 0):
        """
        find link text

        Usage:
            find_text("新闻")
        """
        web_elem = WebElement(self.browser, link_text=text)
        self.element_obj = elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info(f"🔍 find {web_elem.info} text.")
        return self

    def type(self, text):
        """
        type text.
        """
        log.info(f"✅ input '{text}'.")
        self.element_obj.send_keys(text)
        return self

    def click(self):
        """
        click.
        """
        log.info("✅ click.")
        self.element_obj.click()
        return self

    def clear(self):
        """
        clear input.
        Usage:
            clear()
        """
        log.info("✅ clear.")
        self.element_obj.clear()
        return self

    def submit(self):
        """
        submit input
        Usage:
            submit()
        """
        log.info("✅ submit.")
        self.element_obj.submit()
        return self

    def enter(self):
        """
        enter.
        Usage:
            enter()
        """
        log.info("✅ enter.")
        self.element_obj.send_keys(Keys.ENTER)
        return self

    def move_to_click(self):
        """
        Moving the mouse to the middle of an element. and click element.
        Usage:
            move_to_click()
        """
        elem = self.element_obj
        log.info("✅ Move to the element and click.")
        ActionChains(self.browser).move_to_element(elem).click(elem).perform()
        return self

    def right_click(self):
        """
        Right click element.

        Usage:
            right_click()
        """
        elem = self.element_obj
        log.info("✅ right click.")
        ActionChains(self.browser).context_click(elem).perform()
        return self

    def move_to_element(self):
        """
        Mouse over the element.

        Usage:
            move_to_element()
        """
        elem = self.element_obj
        log.info("✅ move to element.")
        ActionChains(self.browser).move_to_element(elem).perform()
        return self

    def click_and_hold(self):
        """
        Mouse over the element.

        Usage:
            move_to_element()
        """

        elem = self.element_obj
        log.info("✅ click and hold.")
        ActionChains(self.browser).click_and_hold(elem).perform()
        return self

    def double_click(self):
        """
        Double click element.

        Usage:
            double_click()
        """
        elem = self.element_obj
        log.info("✅ double click.")
        ActionChains(self.browser).double_click(elem).perform()
        return self

    def close(self):
        """
        Closes the current window.

        Usage:
            close()
        """
        self.browser.close()
        return self

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
            quit()
        """
        self.browser.quit()
        return self

    def refresh(self):
        """
        Refresh the current page.

        Usage:
            refresh()
        """
        log.info("🔄️ refresh page.")
        self.browser.refresh()
        return self

    def alert(self):
        """
        get alert.
        Usage:
            alert()
        """
        log.info("🔍 alert.")
        self.alert_obj = self.browser.switch_to.alert
        return self

    def accept(self):
        """
        Accept warning box.

        Usage:
            alert().accept()
        """
        log.info("✅ accept alert.")
        self.alert_obj.accept()
        return self

    def dismiss(self):
        """
        Dismisses the alert available.

        Usage:
            alert().dismiss()
        """
        log.info("✅ dismiss alert.")
        self.browser.switch_to.alert.dismiss()
        return self

    def switch_to_frame(self):
        """
        Switch to the specified frame.

        Usage:
            switch_to_frame()
        """
        elem = self.element_obj
        log.info("✅  switch to frame.")
        self.browser.switch_to.frame(elem)
        return self

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
            switch_to_frame_out()
        """
        log.info("✅ switch to frame out.")
        self.browser.switch_to.default_content()
        return self

    def switch_to_window(self, window: int):
        """
        Switches focus to the specified window.

        :Args:
         - window: window index. 1 represents a newly opened window (0 is the first one)

        :Usage:
            switch_to_window(1)
        """
        log.info(f"✅ switch to the {window} window.")
        all_handles = self.browser.window_handles
        self.browser.switch_to.window(all_handles[window])
        return self

    def screenshots(self, file_path: str = None):
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
            screenshots()
            screenshots('/Screenshots/foo.png')
        """
        if file_path is None:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, get_timestamp() + ".png")
        log.info(f"📷️  screenshot -> ({file_path}).")
        self.browser.save_screenshot(file_path)
        return self

    def element_screenshot(self, file_path: str = None):
        """
        Saves the element screenshot of the element to a PNG image file.

        Usage:
            element_screenshot()
            element_screenshot(file_path='/Screenshots/foo.png')
        """
        elem = self.element_obj
        if file_path is None:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, get_timestamp() + ".png")
        log.info(f"📷️ element screenshot -> ({file_path}).")
        elem.screenshot(file_path)
        return self

    def select(self, value: str = None, text: str = None, index: int = None):
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

            select(value='20')
            select(text='每页显示20条')
            select(index=2)
        """
        elem = self.element_obj
        log.info("✅ select option.")
        if value is not None:
            Select(elem).select_by_value(value)
        elif text is not None:
            Select(elem).select_by_visible_text(text)
        elif index is not None:
            Select(elem).select_by_index(index)
        else:
            raise ValueError(
                '"value" or "text" or "index" options can not be all empty.')
        return self

    def sleep(self, sec: int):
        """
        Usage:
            self.sleep(seconds)
        """
        log.info(f"💤️ sleep: {sec}s.")
        time.sleep(sec)
        return self
