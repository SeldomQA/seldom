import unittest
from time import sleep
from .webdriver import WebDriver
from .driver import browser
from .running.test_runner import Browser


class TestCase(unittest.TestCase, WebDriver):

    @classmethod
    def setUpClass(cls):
        cls.driver = browser(Browser.name, Browser.driver_path)
        cls.timeout = 10

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def assertTitle(self, title=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(self.timeout):
            try:
                self.assertEqual(title, self.get_title())
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(title, self.get_title())

    def assertInTitle(self, title=None):
        """
        Asserts whether the current title is in line with expectations.

        Usage:
        self.assertInTitle("title")
        """
        if title is None:
            raise AssertionError("The assertion title cannot be empty.")
        for _ in range(self.timeout):
            try:
                self.assertIn(title, self.get_title())
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(title, self.get_title())

    def assertUrl(self, url):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(self.timeout):
            try:
                self.assertEqual(url, self.get_url())
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(url, self.get_url())

    def assertInUrl(self, url=None):
        """
        Asserts whether the current URL is in line with expectations.

        Usage:
        self.assertInUrl("url")
        """
        if url is None:
            raise AssertionError("The assertion URL cannot be empty.")
        for _ in range(self.timeout):
            try:
                self.assertIn(url, self.get_url())
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(url, self.get_url())

    def assertText(self, text=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = self.driver.find_element_by_tag_name("html")
        for _ in range(self.timeout):
            if elem.is_displayed():
                try:
                    self.assertIn(text, elem.text)
                    break
                except AssertionError:
                    sleep(1)
        else:
            self.assertIn(text, elem.text)

    def assertAlertText(self, text=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertAlertText("text")
        """
        if text is None:
            raise NameError("Alert text cannot be empty.")
        alert_text = self.get_alert_text()
        self.assertEqual(alert_text, text)
