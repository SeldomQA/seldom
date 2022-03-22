# coding=utf-8
import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from seldom.logging import log
from seldom.running.config import Seldom
from seldom.utils.webdriver_manager_extend import ChromeDriverManager
from seldom.webdriver import WebElement

__all__ = ["Case"]


class Case(object):
    """
    Webdriver Basic method chaining
    Write test cases quickly.
    """

    def __init__(self, url: str = None, desc: str = None):
        self.url = url
        log.info("🔖 Test Case: {}".format(desc))

    def open(self, url: str = None):
        """
        open url.

        Usage:
            open("https://www.baidu.com")
        """
        if isinstance(Seldom.driver, SeleniumWebDriver) is False:
            Seldom.driver = Chrome(executable_path=ChromeDriverManager().install())
        if self.url is not None:
            log.info("📖 {}".format(self.url))
            Seldom.driver.get(self.url)
        else:
            log.info("📖 {}".format(url))
            Seldom.driver.get(url)
        return self

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
            max_window()
        """
        Seldom.driver.maximize_window()
        return self

    def set_window(self, wide: int = 0, high: int = 0):
        """
        Set browser window wide and high.

        Usage:
            .set_window(wide,high)
        """
        Seldom.driver.set_window_size(wide, high)
        return self

    def find(self, css: str, index: int = 0):
        """
        find element
        """
        web_elem = WebElement(css=css)
        Seldom.element = elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info("🔍 find {info}.".format(info=web_elem.info))
        return self

    def find_text(self, text: str, index: int = 0):
        """
        find link text

        Usage:
            find_text("新闻")
        """
        web_elem = WebElement(link_text=text)
        Seldom.element = elem = web_elem.get_elements(index)
        web_elem.show_element(elem)
        log.info("🔍 find {} text.".format(web_elem.info))
        return self

    def type(self, text):
        """
        type text.
        """
        log.info(f"✅ input '{text}'.")
        Seldom.element.send_keys(text)
        return self

    def click(self):
        """
        click.
        """
        log.info("✅ click.")
        Seldom.element.click()
        return self

    def clear(self):
        """
        clear input.
        Usage:
            clear()
        """
        log.info("✅ clear.")
        Seldom.element.clear()
        return self

    def submit(self):
        """
        submit input
        Usage:
            submit()
        """
        log.info("✅ clear.")
        Seldom.element.submit()
        return self

    def enter(self):
        """
        enter.
        Usage:
            enter()
        """
        log.info("✅ enter.")
        Seldom.element.send_keys(Keys.ENTER)
        return self

    def move_to_click(self):
        """
        Moving the mouse to the middle of an element. and click element.
        Usage:
            move_to_click()
        """
        elem = Seldom.element
        log.info("✅ Move to the element and click.")
        ActionChains(Seldom.driver).move_to_element(elem).click(elem).perform()
        return self

    def right_click(self):
        """
        Right click element.

        Usage:
            right_click()
        """
        elem = Seldom.element
        log.info("✅ right click.")
        ActionChains(Seldom.driver).context_click(elem).perform()
        return self

    def move_to_element(self):
        """
        Mouse over the element.

        Usage:
            move_to_element()
        """
        elem = Seldom.element
        log.info("✅ move to element.")
        ActionChains(Seldom.driver).move_to_element(elem).perform()
        return self

    def click_and_hold(self):
        """
        Mouse over the element.

        Usage:
            move_to_element()
        """

        elem = Seldom.element
        log.info("✅ click and hold.")
        ActionChains(Seldom.driver).click_and_hold(elem).perform()
        return self

    def double_click(self):
        """
        Double click element.

        Usage:
            double_click()
        """
        elem = Seldom.element
        log.info("✅ double click.")
        ActionChains(Seldom.driver).double_click(elem).perform()
        return self

    def close(self):
        """
        Closes the current window.

        Usage:
            close()
        """
        Seldom.driver.close()
        return self

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
            quit()
        """
        Seldom.driver.quit()
        return self

    def refresh(self):
        """
        Refresh the current page.

        Usage:
            refresh()
        """
        log.info("🔄️ refresh page.")
        Seldom.driver.refresh()
        return self

    def alert(self):
        """
        get alert.
        Usage:
            alert()
        """
        log.info("✅ alert.")
        Seldom.alert = Seldom.driver.switch_to.alert
        return self

    def accept(self):
        """
        Accept warning box.

        Usage:
            alert().accept()
        """
        log.info("✅ accept alert.")
        Seldom.alert.accept()
        return self

    def dismiss(self):
        """
        Dismisses the alert available.

        Usage:
            alert().dismiss()
        """
        log.info("✅ dismiss alert.")
        Seldom.driver.switch_to.alert.dismiss()
        return self

    def switch_to_frame(self):
        """
        Switch to the specified frame.

        Usage:
            switch_to_frame()
        """
        elem = Seldom.element
        log.info("✅  switch to frame.")
        Seldom.driver.switch_to.frame(elem)
        return self

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
            switch_to_frame_out()
        """
        log.info("✅ switch to frame out.")
        Seldom.driver.switch_to.default_content()
        return self

    def switch_to_window(self, window: int):
        """
        Switches focus to the specified window.

        :Args:
         - window: window index. 1 represents a newly opened window (0 is the first one)

        :Usage:
            switch_to_window(1)
        """
        log.info("✅ switch to the {} window.".format(str(window)))
        all_handles = Seldom.driver.window_handles
        Seldom.driver.switch_to.window(all_handles[window])
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
            file_path = os.path.join(img_dir, str(time.time()).split(".")[0] + ".png")
        if Seldom.debug is True:
            log.info(f"📷️  screenshot -> ({file_path}).")
            Seldom.driver.save_screenshot(file_path)
        else:
            log.info("📷️  screenshot -> HTML report.")
            self.images.append(Seldom.driver.get_screenshot_as_base64())
        return self

    def element_screenshot(self, file_path: str = None):
        """
        Saves a element screenshot of the element to a PNG image file.

        Usage:
            element_screenshot()
            element_screenshot(file_path='/Screenshots/foo.png')
        """
        elem = Seldom.element
        if file_path is None:
            img_dir = os.path.join(os.getcwd(), "reports", "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            file_path = os.path.join(img_dir, str(time.time()).split(".")[0] + ".png")
        if Seldom.debug is True:
            log.info(f"📷️ element screenshot -> ({file_path}).")
            elem.screenshot(file_path)
        else:
            log.info("📷️ element screenshot -> HTML Report.")
            self.images.append(elem.screenshot_as_base64)
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
        elem = Seldom.element
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
        log.info("💤️ sleep: {}s.".format(str(sec)))
        time.sleep(sec)
        return self