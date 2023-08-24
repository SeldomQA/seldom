"""
seldom test case
"""
import wda
import uiautomator2
import unittest
from urllib.parse import unquote
from time import sleep
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from selenium.webdriver.common.by import By
from appium.webdriver import Remote
from seldom.driver import Browser
from seldom.webdriver import WebDriver
from seldom.appdriver import AppDriver
from seldom.u2driver import U2Driver
from seldom.wdadriver import WDADriver
from seldom.request import HttpRequest, ResponseResult, formatting
from seldom.running.config import Seldom, BrowserConfig, AppConfig
from seldom.logging import log
from seldom.logging.exceptions import NotFindElementError
from seldom.utils import diff_json, AssertInfo, jmespath


class TestCase(unittest.TestCase, WebDriver, AppDriver, U2Driver, WDADriver, HttpRequest):
    """seldom TestCase class"""

    def start_class(self):
        """
        Hook method for setting up class fixture before running tests in the class.
        """
        pass

    def end_class(self):
        """
        Hook method for deconstructing the class fixture after running all tests in the class.
        """
        pass

    @classmethod
    def setUpClass(cls):
        cls().start_class()

    @classmethod
    def tearDownClass(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        pass

    def end(self):
        """
        Hook method for deconstructing the test fixture after testing it.
        """
        pass

    def setUp(self):
        self.images = []
        # lunch appium
        if (Seldom.app_server is not None) and (Seldom.app_info is not None):
            Seldom.driver = Remote(Seldom.app_server, Seldom.app_info)
        elif (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'Android'):
            """lunch uiautomator2"""
            Seldom.driver = uiautomator2.connect_usb(Seldom.app_info.get('deviceName'))
        elif (Seldom.app_server is None) and (Seldom.app_info.get('platformName') == 'iOS'):
            """lunch facebook-wda"""
            Seldom.driver = wda.USBClient(udid=Seldom.app_info.get('udid'))
        self.start()

    def tearDown(self):
        self.end()
        # close appium
        if (Seldom.app_server is not None) and (Seldom.app_info is not None):
            Seldom.driver.quit()
        elif (Seldom.app_server is None) and (Seldom.app_info is not None):
            """upload performance related chart data"""
            self.images = AppConfig.REPORT_IMAGE

    @property
    def base_url(self):
        """
        return base url (http)
        """
        return Seldom.base_url

    @property
    def driver(self):
        """
        return browser driver (web)
        """
        return Seldom.driver

    @staticmethod
    def browser(name: str):
        """
        launch browser
        :param name: browser name
        """
        Seldom.driver = Browser(name=name)

    @staticmethod
    def new_browser():
        """
        launch new browser
        """
        browser = Browser(BrowserConfig.NAME)
        return browser

    def assertTitle(self, title: str = None, msg: str = None) -> None:
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")

        log.info(f"👀 assertTitle -> {title}.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertEqual(title, Seldom.driver.title)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(title, Seldom.driver.title, msg=msg)

    def assertInTitle(self, title: str = None, msg: str = None) -> None:
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertInTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")

        log.info(f"👀 assertInTitle -> {title}.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertIn(title, Seldom.driver.title)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(title, Seldom.driver.title, msg=msg)

    def assertUrl(self, url: str = None, msg: str = None) -> None:
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")

        log.info(f"👀 assertUrl -> {url}.")
        current_url = unquote(Seldom.driver.current_url)
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertEqual(url, current_url)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(url, current_url, msg=msg)

    def assertInUrl(self, url: str = None, msg: str = None) -> None:
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertInUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")

        log.info(f"👀 assertInUrl -> {url}.")
        for _ in range(Seldom.timeout + 1):
            current_url = unquote(Seldom.driver.current_url)
            try:
                self.assertIn(url, current_url)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(url, Seldom.driver.current_url, msg=msg)

    def assertText(self, text: str = None, msg: str = None) -> None:
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = Seldom.driver.find_element(By.TAG_NAME, "html")
        log.info(f"👀 assertText -> {text}.")
        for _ in range(Seldom.timeout + 1):
            if elem.is_displayed():
                try:
                    self.assertIn(text, elem.text)
                    break
                except AssertionError:
                    sleep(1)
        else:
            self.assertIn(text, elem.text, msg=msg)

    def assertNotText(self, text: str = None, msg: str = None) -> None:
        """
        Asserts that the current page does not contain the specified text.

        Usage:
        self.assertNotText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = Seldom.driver.find_element(By.TAG_NAME, "html")

        log.info(f"👀 assertNotText -> {text}.")
        for _ in range(Seldom.timeout + 1):
            if elem.is_displayed():
                try:
                    self.assertNotIn(text, elem.text)
                    break
                except AssertionError:
                    sleep(1)
        else:
            self.assertNotIn(text, elem.text, msg=msg)

    def assertAlertText(self, text: str = None, msg: str = None) -> None:
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertAlertText("text")
        """
        if text is None:
            raise NameError("Alert text cannot be empty.")

        log.info(f"👀 assertAlertText -> {text}.")
        alert_text = Seldom.driver.switch_to.alert.text
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertEqual(alert_text, text, msg=msg)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(alert_text, text, msg=msg)

    def assertElement(self, index: int = 0, msg: str = None, **kwargs) -> None:
        """
        Asserts whether the element exists.

        Usage:
        self.assertElement(css="#id")
        """
        log.info("👀 assertElement.")
        if msg is None:
            msg = "No element found"
        try:
            if Seldom.app_info.get('platformName') == 'Android':
                self.get_elements_u2(index=index, **kwargs)
            elif Seldom.app_info.get('platformName') == 'iOS':
                self.get_element_wda(index=index, **kwargs)
            else:
                self.get_element(index=index, **kwargs)
            elem = True
        except NotFindElementError:
            elem = False

        self.assertTrue(elem, msg=msg)

    def assertNotElement(self, index: int = 0, msg: str = None, **kwargs) -> None:
        """
        Asserts if the element does not exist.

        Usage:
        self.assertNotElement(css="#id")
        """
        log.info("👀 assertNotElement.")
        if msg is None:
            msg = "Find the element"

        timeout_backups = Seldom.timeout
        Seldom.timeout = 2
        try:
            if Seldom.app_info.get('platformName') == 'Android':
                self.get_elements_u2(index=index, **kwargs)
            elif Seldom.app_info.get('platformName') == 'iOS':
                self.get_element_wda(index=index, **kwargs)
            else:
                self.get_element(index=index, **kwargs)
            elem = True
        except NotFindElementError:
            elem = False

        Seldom.timeout = timeout_backups

        self.assertFalse(elem, msg=msg)

    def assertStatusCode(self, status_code: int, msg: str = None) -> None:
        """
        Asserts the HTTP status code
        """
        log.info(f"👀 assertStatusCode -> {status_code}.")
        self.assertEqual(ResponseResult.status_code, status_code, msg=msg)

    def assertSchema(self, schema, response=None) -> None:
        """
        Assert JSON Schema
        doc: https://json-schema.org/
        """
        log.info(f"👀 assertSchema -> {formatting(schema)}.")

        if response is None:
            response = ResponseResult.response

        try:
            validate(instance=response, schema=schema)
        except ValidationError as msg:
            self.assertEqual("Response data", "Schema data", msg)

    def assertJSON(self, assert_json, response=None, exclude=None) -> None:
        """
        Assert JSON data
        """
        log.info(f"👀 assertJSON -> {assert_json}.")
        if response is None:
            response = ResponseResult.response

        AssertInfo.warning = []
        AssertInfo.error = []
        diff_json(response, assert_json, exclude)
        if len(AssertInfo.warning) != 0:
            log.warning(AssertInfo.warning)
        if len(AssertInfo.error) != 0:
            self.assertEqual("Response data", "Assert data", msg=AssertInfo.error)

    def assertPath(self, path, value) -> None:
        """
        Assert path data
        doc: https://jmespath.org/
        """
        log.info(f"👀 assertPath -> {path} >> {value}.")
        search_value = jmespath(ResponseResult.response, path)
        self.assertEqual(search_value, value)

    def assertInPath(self, path, value) -> None:
        """
        Assert path data
        doc: https://jmespath.org/
        """
        log.info(f"👀 assertInPath -> {path} >> {value}.")
        search_value = jmespath(ResponseResult.response, path)
        self.assertIn(value, search_value)

    def xSkip(self, reason):
        """
        Skip this test.
        :param reason:
        Usage:
        if data is None:
            self.xSkip("data is None.")
        """
        self.skipTest(reason)

    def xFail(self, msg):
        """
        Fail immediately, with the given message
        :param msg:
        Usage:
        if data is None:
            self.xFail("This case fails.")
        """
        self.fail(msg)
