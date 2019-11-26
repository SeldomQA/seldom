# coding=utf-8
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


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


class WebDriver(object):
    """
        Seldom framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """
    driver = None
    original_window = None

    def wait_element(self, el):
        """
        Waiting for an element to display.
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(el)
            )
        except TimeoutException:
            return False
        else:
            return True

    def get_element(self, **kwargs):
        """
        Judge element positioning way, and returns the element.
        """
        by, value = next(iter(kwargs.items()))
        try:
            LOCATOR_LIST[by]
        except KeyError:
            raise ValueError("Element positioning of type '{}' is not supported. ".format(by))

        error = "Unable to locate elements, ({by}='{value}').".format(by=by, value=value)
        if by == "id_":
            req = self.wait_element((By.ID, value))
            if req is True:
                element = self.driver.find_element_by_id(value)
            else:
                raise NoSuchElementException(error)
        elif by == "name":
            req = self.wait_element((By.NAME, value))
            if req is True:
                element = self.driver.find_element_by_name(value)
            else:
                raise NoSuchElementException(error)
        elif by == "class_name":
            req = self.wait_element((By.CLASS_NAME, value))
            if req is True:
                element = self.driver.find_element_by_class_name(value)
            else:
                raise NoSuchElementException(error)
        elif by == "link_text":
            req = self.wait_element((By.LINK_TEXT, value))
            if req is True:
                element = self.driver.find_element_by_link_text(value)
            else:
                raise NoSuchElementException(error)
        elif by == "xpath":
            req = self.wait_element((By.XPATH, value))
            if req is True:
                element = self.driver.find_element_by_xpath(value)
            else:
                raise NoSuchElementException(error)
        elif by == "css":
            req = self.wait_element((By.CSS_SELECTOR, value))
            if req is True:
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise NoSuchElementException(error)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        """
        open url.

        Usage:
        self.open("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        self.max_window()
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        self.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def type(self, text, clear=True, **kwargs):
        """
        Operation input box.

        Usage:
        self.type(css="#el", text="selenium")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        if clear is True:
            self.clear(**kwargs)
        el = self.get_element(**kwargs)
        el.send_keys(text)

    def clear(self, **kwargs):
        """
        Clear the contents of the input box.

        Usage:
        self.clear(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        el.clear()

    def click(self, **kwargs):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        self.click(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        el.click()

    def right_click(self, **kwargs):
        """
        Right click element.

        Usage:
        self.right_click(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, **kwargs):
        """
        Mouse over the element.

        Usage:
        self.move_to_element(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, **kwargs):
        """
        Double click element.

        Usage:
        self.double_click(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        ActionChains(self.driver).double_click(el).perform()

    def click_text(self, text):
        """
        Click the element by the link text

        Usage:
        self.click_text("新闻")
        """
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        self.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        self.quit()
        """
        self.driver.quit()

    def submit(self, **kwargs):
        """
        Submit the specified form.

        Usage:
        driver.submit(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        el.submit()

    def refresh(self):
        """
        Refresh the current page.

        Usage:
        self.refresh()
        """
        self.driver.refresh()

    def execute_script(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        self.execute_script("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def window_scroll(self, width=None, height=None):
        """
        Setting width and height of window scroll bar.
        Usage:
        self.window_scroll(width=300, height=500)
        """
        if width is None:
            width = "0"
        if height is None:
            height = "0"
        js = "window.scrollTo({w},{h});".format(w=str(width), h=str(height))
        self.execute_script(js)

    def get_attribute(self, attribute=None, **kwargs):
        """
        Gets the value of an element attribute.

        Usage:
        self.get_attribute(css="#el", attribute="type")
        """
        if attribute is None:
            raise ValueError("attribute is not None")
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        return el.get_attribute(attribute)

    def get_text(self, **kwargs):
        """
        Get element text information.

        Usage:
        self.get_text(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        return el.text

    def get_display(self, **kwargs):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        self.get_display(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        return el.is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        self.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        self.get_url()
        """
        return self.driver.current_url

    def get_alert_text(self):
        """
        Gets the text of the Alert.

        Usage:
        self.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def wait(self, secs=10):
        """
        Implicitly wait.All elements on the page.

        Usage:
        self.wait(10)
        """
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        self.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        self.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, **kwargs):
        """
        Switch to the specified frame.

        Usage:
        self.switch_to_frame(css="#el")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        frame_elem = self.get_element(**kwargs)
        self.driver.switch_to.frame(frame_elem)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        self.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, **kwargs):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        self.open_new_window(link_text="注册")
        """
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        original_window = self.driver.current_window_handle
        el = self.get_element(**kwargs)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def screenshots(self, file_path):
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
        self.screenshots('/Screenshots/foo.png')
        """
        self.driver.save_screenshot(file_path)

    def select(self, value=None, text=None, index=None, **kwargs):
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
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        el = self.get_element(**kwargs)
        if value is not None:
            Select(el).select_by_value(value)
        elif text is not None:
            Select(el).select_by_visible_text(text)
        elif index is not None:
            Select(el).select_by_index(index)
        else:
            raise ValueError(
                '"value" or "text" or "index" options can not be all empty.')

    @staticmethod
    def sleep(sec):
        """
        Usage:
            self.sleep(seconds)
        """
        time.sleep(sec)
