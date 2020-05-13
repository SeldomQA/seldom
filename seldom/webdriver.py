# coding=utf-8
import time
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from seldom.logging import log
from seldom.running.config import Seldom
from seldom.logging.exceptions import NotFindElementError


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


def find_element(elem):
    """
    Find if the element exists.
    """
    for i in range(Seldom.timeout):
        elems = Seldom.driver.find_elements(by=elem[0], value=elem[1])
        if len(elems) == 1:
            log.info("✅ Find element: {by}={value} ".format(
                by=elem[0], value=elem[1]))
            break
        elif len(elems) > 1:
            log.warn("❓ Find {n} elements through: {by}={value}".format(
                n=len(elems), by=elem[0], value=elem[1]))
            break
        else:
            time.sleep(1)
    else:
        error_msg = "❌ Find 0 elements through: {by}={value}".format(
            by=elem[0], value=elem[1])
        log.error(error_msg)
        raise NotFindElementError(error_msg)


def get_element(index, **kwargs):
    """
    Judge element positioning way, and returns the element.
    """
    if not kwargs:
        raise ValueError("Please specify a locator")
    if len(kwargs) > 1:
        raise ValueError("Please specify only one locator")

    by, value = next(iter(kwargs.items()))
    try:
        LOCATOR_LIST[by]
    except KeyError:
        raise ValueError("Element positioning of type '{}' is not supported. ".format(by))

    if by == "id_":
        find_element((By.ID, value))
        elem = Seldom.driver.find_elements_by_id(value)[index]
    elif by == "name":
        find_element((By.NAME, value))
        elem = Seldom.driver.find_elements_by_name(value)[index]
    elif by == "class_name":
        find_element((By.CLASS_NAME, value))
        elem = Seldom.driver.find_elements_by_class_name(value)[index]
    elif by == "tag":
        find_element((By.TAG_NAME, value))
        elem = Seldom.driver.find_elements_by_tag_name(value)[index]
    elif by == "link_text":
        find_element((By.LINK_TEXT, value))
        elem = Seldom.driver.find_elements_by_link_text(value)[index]
    elif by == "partial_link_text":
        find_element((By.PARTIAL_LINK_TEXT, value))
        elem = Seldom.driver.find_elements_by_partial_link_text(value)[index]
    elif by == "xpath":
        find_element((By.XPATH, value))
        elem = Seldom.driver.find_elements_by_xpath(value)[index]
    elif by == "css":
        find_element((By.CSS_SELECTOR, value))
        elem = Seldom.driver.find_elements_by_css_selector(value)[index]
    else:
        raise NameError(
            "Please enter the correct targeting elements,'id_/name/class_name/tag/link_text/xpath/css'.")

    style_red = 'arguments[0].style.border="2px solid red"'
    Seldom.driver.execute_script(style_red, elem)

    return elem


class WebDriver(object):
    """
        Seldom framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """
    original_window = None

    def get(self, url):
        """
        get url.

        Usage:
        self.get("https://www.baidu.com")
        """
        Seldom.driver.get(url)

    def open(self, url):
        """
        open url.

        Usage:
        self.open("https://www.baidu.com")
        """
        self.get(url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        self.max_window()
        """
        Seldom.driver.maximize_window()

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        self.set_window(wide,high)
        """
        Seldom.driver.set_window_size(wide, high)

    def type(self, text, clear=False, index=0, **kwargs):
        """
        Operation input box.

        Usage:
        self.type(css="#el", text="selenium")
        """
        if clear is True:
            self.clear(index, **kwargs)
        elem = get_element(index, **kwargs)
        log.info("🖋 input '{text}'.".format(text=text))
        elem.send_keys(text)
    
    def type_enter(self, text, clear=False, index=0, **kwargs):
        """
        Enter text and enter directly.

        Usage:
        self.type_enter(css="#el", text="selenium")
        """
        if clear is True:
            self.clear(index, **kwargs)
        elem = get_element(index, **kwargs)
        log.info("🖋 ➕ 🖱 input '{text}' and enter.".format(text=text))
        elem.send_keys(text)
        elem.send_keys(Keys.ENTER)

    def clear(self, index=0, **kwargs):
        """
        Clear the contents of the input box.

        Usage:
        self.clear(css="#el")
        """
        elem = get_element(index, **kwargs)
        elem.clear()

    def click(self, index=0, **kwargs):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        self.click(css="#el")
        """
        elem = get_element(index, **kwargs)
        log.info("🖱 click.")
        elem.click()

    def slow_click(self, index=0, **kwargs):
        """
        Moving the mouse to the middle of an element. and click element.
        Usage:
        self.slow_click(css="#el")
        """
        elem = get_element(index, **kwargs)
        ActionChains(Seldom.driver).move_to_element(elem).click(elem).perform()

    def right_click(self, index=0, **kwargs):
        """
        Right click element.

        Usage:
        self.right_click(css="#el")
        """
        elem = get_element(index, **kwargs)
        ActionChains(Seldom.driver).context_click(elem).perform()

    def move_to_element(self, index=0, **kwargs):
        """
        Mouse over the element.

        Usage:
        self.move_to_element(css="#el")
        """
        elem = get_element(index, **kwargs)
        ActionChains(Seldom.driver).move_to_element(elem).perform()

    def click_and_hold(self, index=0, **kwargs):
        """
        Mouse over the element.

        Usage:
        self.move_to_element(css="#el")
        """
        elem = get_element(index, **kwargs)
        ActionChains(Seldom.driver).click_and_hold(elem).perform()

    def double_click(self, index=0, **kwargs):
        """
        Double click element.

        Usage:
        self.double_click(css="#el")
        """
        elem = get_element(index, **kwargs)
        ActionChains(Seldom.driver).double_click(elem).perform()

    def click_text(self, text):
        """
        Click the element by the link text

        Usage:
        self.click_text("新闻")
        """
        find_element((By.LINK_TEXT, text))
        Seldom.driver.find_element_by_link_text(text).click()

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        self.close()
        """
        Seldom.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        self.quit()
        """
        Seldom.driver.quit()

    def submit(self, index=0, **kwargs):
        """
        Submit the specified form.

        Usage:
        driver.submit(css="#el")
        """
        elem = get_element(index, **kwargs)
        elem.submit()

    def refresh(self):
        """
        Refresh the current page.

        Usage:
        self.refresh()
        """
        Seldom.driver.refresh()

    def execute_script(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        self.execute_script("window.scrollTo(200,1000);")
        """
        Seldom.driver.execute_script(script)

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

    def get_attribute(self, attribute=None, index=0, **kwargs):
        """
        Gets the value of an element attribute.

        Usage:
        self.get_attribute(css="#el", attribute="type")
        """
        if attribute is None:
            raise ValueError("attribute is not None")
        elem = get_element(index, **kwargs)
        return elem.get_attribute(attribute)

    def get_text(self, index=0, **kwargs):
        """
        Get element text information.

        Usage:
        self.get_text(css="#el")
        """
        elem = get_element(index, **kwargs)
        return elem.text

    def get_display(self, index=0, **kwargs):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        self.get_display(css="#el")
        """
        elem = get_element(index, **kwargs)
        return elem.is_displayed()

    @property
    def get_title(self):
        """
        Get window title.

        Usage:
        self.get_title()
        """
        return Seldom.driver.title

    @property
    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        self.get_url()
        """
        return Seldom.driver.current_url

    @property
    def get_alert_text(self):
        """
        Gets the text of the Alert.

        Usage:
        self.get_alert_text()
        """
        return Seldom.driver.switch_to.alert.text

    def wait(self, secs=10):
        """
        Implicitly wait.All elements on the page.

        Usage:
        self.wait(10)
        """
        Seldom.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        self.accept_alert()
        """
        Seldom.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        self.dismiss_alert()
        """
        Seldom.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, index=0, **kwargs):
        """
        Switch to the specified frame.

        Usage:
        self.switch_to_frame(css="#el")
        """
        elem = get_element(index, **kwargs)
        Seldom.driver.switch_to.frame(elem)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        self.switch_to_frame_out()
        """
        Seldom.driver.switch_to.default_content()

    def open_new_window(self, index=0, **kwargs):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        self.open_new_window(link_text="注册")
        """
        warnings.warn("This method is not recommended",
                      DeprecationWarning, stacklevel=2)
        original_window = Seldom.driver.current_window_handle
        elem = get_element(index, **kwargs)
        elem.click()
        all_handles = Seldom.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                Seldom.driver.switch_to.window(handle)

    @property
    def current_window_handle(self):
        """
        Returns the handle of the current window.

        :Usage:
            self.current_window_handle
        """
        return Seldom.driver.current_window_handle

    @property
    def new_window_handle(self):
        """
        Returns the handle of the new window.

        :Usage:
            self.new_window_handle
        """
        new_handle = self.window_handles
        return new_handle[-1]

    @property
    def window_handles(self):
        """
        Returns the handles of all windows within the current session.

        :Usage:
            self.window_handles
        """
        all_handles = Seldom.driver.window_handles
        return all_handles

    def switch_to_window(self, window_name):
        """
        Switches focus to the specified window.

        :Args:
         - window_name: The name or window handle of the window to switch to.

        :Usage:
            self.switch_to_window('main')
        """
        Seldom.driver.switch_to.window(window_name)

    def screenshots(self, file_path):
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
        self.screenshots('/Screenshots/foo.png')
        """
        Seldom.driver.save_screenshot(file_path)

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
        elem = get_element(index=0, **kwargs)
        if value is not None:
            Select(elem).select_by_value(value)
        elif text is not None:
            Select(elem).select_by_visible_text(text)
        elif index is not None:
            Select(elem).select_by_index(index)
        else:
            raise ValueError(
                '"value" or "text" or "index" options can not be all empty.')

    def get_cookies(self):
        """
        Returns a set of dictionaries, corresponding to cookies visible in the current session.
        Usage:
            self.get_cookies()
        """
        return Seldom.driver.get_cookies()

    def get_cookie(self, name):
        """
        Returns information of cookie with ``name`` as an object.
        Usage:
            self.get_cookie()
        """
        return Seldom.driver.get_cookie(name)

    def add_cookie(self, cookie_dict):
        """
        Adds a cookie to your current session.
        Usage:
            self.add_cookie({'name' : 'foo', 'value' : 'bar'})
        """
        if isinstance(cookie_dict, dict):
            Seldom.driver.add_cookie(cookie_dict)
        else:
            raise TypeError("Wrong cookie type.")

    def add_cookies(self, cookie_list):
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

    def delete_cookie(self, name):
        """
        Deletes a single cookie with the given name.
        Usage:
            self.delete_cookie('my_cookie')
        """
        Seldom.driver.delete_cookie(name)

    def delete_all_cookies(self):
        """
        Delete all cookies in the scope of the session.
        Usage:
            self.delete_all_cookies()
        """
        Seldom.driver.delete_all_cookies()

    @staticmethod
    def sleep(sec):
        """
        Usage:
            self.sleep(seconds)
        """
        time.sleep(sec)
