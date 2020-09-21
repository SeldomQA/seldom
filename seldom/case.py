import unittest
from time import sleep
from seldom.webdriver import WebDriver
from seldom.running.config import Seldom
from seldom.logging import log


class TestCase(unittest.TestCase, WebDriver):

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
        self.start()

    def tearDown(self):
        self.end()

    def assertTitle(self, title=None, msg=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(Seldom.timeout):
            try:
                self.assertEqual(title, self.get_title)
                log.info("👀 assert title: {title}.".format(
                    title=self.get_title))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assert fail: {title}.".format(title=title))
            self.assertEqual(title, self.get_title, msg=msg)

    def assertInTitle(self, title=None, msg=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertInTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(Seldom.timeout):
            try:
                self.assertIn(title, self.get_title)
                log.info("👀 assertIn title: {title}.".format(
                    title=self.get_title))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assertIn fail: {title}.".format(title=title))
            self.assertIn(title, self.get_title, msg=msg)

    def assertUrl(self, url, msg=None):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(Seldom.timeout):
            try:
                self.assertEqual(url, self.get_url)
                log.info("👀 assert url: {url}.".format(url=self.get_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assert fail: {url}.".format(url=url))
            self.assertEqual(url, self.get_url, msg=msg)

    def assertInUrl(self, url=None, msg=None):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertInUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(Seldom.timeout):
            try:
                self.assertIn(url, self.get_url)
                log.info("👀 assertIn url: {url}.".format(url=self.get_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.warn("❌ assertIn fail: {url}.".format(url=url))
            self.assertIn(url, self.get_url, msg=msg)

    def assertText(self, text=None, msg=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = Seldom.driver.find_element_by_tag_name("html")
        for _ in range(Seldom.timeout):
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
        alert_text = self.get_alert_text()
        self.assertEqual(alert_text, text, msg=msg)

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
