import unittest
import jmespath
from time import sleep
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from seldom.webdriver import WebDriver
from seldom.request import HttpRequest
from seldom.running.config import Seldom
from seldom.logging import log
from seldom.logging.exceptions import NotFindElementError
from seldom.utils import diff_json, AssertInfo
from seldom.request import ResponseResult


class TestCase(unittest.TestCase, WebDriver, HttpRequest):

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
        self.start()

    def tearDown(self):
        self.end()

    @property
    def driver(self):
        """
        return browser driver
        """
        return Seldom.driver

    def assertTitle(self, title=None, msg=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertEqual(title, Seldom.driver.title)
                log.info("👀 assert title: {title}.".format(
                    title=Seldom.driver.title))
                break
            except AssertionError:
                sleep(1)
        else:
            print("abc")
            log.warn("❌ assert fail: {title}.".format(title=title))
            self.assertEqual(title, Seldom.driver.title, msg=msg)

    def assertInTitle(self, title=None, msg=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertInTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertIn(title, Seldom.driver.title)
                log.info("👀 assertIn title: {title}.".format(
                    title=Seldom.driver.title))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assertIn fail: {title}.".format(title=title))
            self.assertIn(title, Seldom.driver.title, msg=msg)

    def assertUrl(self, url, msg=None):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertEqual(url, Seldom.driver.current_url)
                log.info("👀 assert url: {url}.".format(url=Seldom.driver.current_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assert fail: {url}.".format(url=url))
            self.assertEqual(url, Seldom.driver.current_url, msg=msg)

    def assertInUrl(self, url=None, msg=None):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertInUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(Seldom.timeout + 1):
            try:
                self.assertIn(url, Seldom.driver.current_url)
                log.info("👀 assertIn url: {url}.".format(url=Seldom.driver.current_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assertIn fail: {url}.".format(url=url))
            self.assertIn(url, Seldom.driver.current_url, msg=msg)

    def assertText(self, text=None, msg=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = Seldom.driver.find_element_by_tag_name("html")
        for _ in range(Seldom.timeout + 1):
            if elem.is_displayed():
                try:
                    self.assertIn(text, elem.text)
                    log.info("👀 assertText: {text}.".format(text=text))
                    break
                except AssertionError:
                    sleep(1)
        else:
            self.assertIn(text, elem.text, msg=msg)

    def assertAlertText(self, text=None, msg=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertAlertText("text")
        """
        if text is None:
            raise NameError("Alert text cannot be empty.")
        alert_text = Seldom.driver.switch_to.alert.text
        self.assertEqual(alert_text, text, msg=msg)

    def assertElement(self, msg=None, **kwargs):
        """
        Asserts whether the element exists.

        Usage:
        self.assertElement("text")
        """
        if msg is None:
            msg = "No elements found"
        for _ in range(Seldom.timeout + 1):
            try:
                log.info("👀 assertElement.")
                self.get_elements(**kwargs)
                break
            except NotFindElementError:
                sleep(1)
        else:
            print("time out")
            self.assertTrue(False, msg=msg)

    def assertNotElement(self, msg=None, **kwargs):
        """
        Asserts if the element does not exist.

        Usage:
        self.assertNotElement("text")
        """
        if msg is None:
            msg = "Find the element"

            try:
                log.info("👀 assertNotElement.")
                self.get_elements(**kwargs)
            except NotFindElementError:
                pass
            else:
                self.assertFalse(True, msg=msg)

    def assertStatusCode(self, status_code, msg=None):
        """
        Asserts the HTTP status code
        """
        self.assertEqual(ResponseResult.status_code, status_code, msg=msg)

    def assertSchema(self, schema):
        """
        Assert JSON Schema
        doc: https://json-schema.org/
        """
        try:
            validate(instance=ResponseResult.response, schema=schema)
        except ValidationError as msg:
            self.assertEqual("Response data", "Schema data", msg)
        else:
            self.assertTrue(True)

    def assertJSON(self, assert_json):
        """
        Assert JSON data
        """
        AssertInfo.data = []
        diff_json(ResponseResult.response, assert_json)
        if len(AssertInfo.data) == 0:
            self.assertTrue(True)
        else:
            self.assertEqual("Response data", "Assert data", msg=AssertInfo.data)

    def assertPath(self, path, value):
        """
        Assert path data
        doc: https://jmespath.org/
        """
        search_value = jmespath.search(path, ResponseResult.response)
        if search_value is None:
            self.assertEqual(path, None, msg="{} No match".format(path))
        else:
            self.assertEqual(search_value, value)

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
