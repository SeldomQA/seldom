import unittest
from time import sleep
from seldom.webdriver import WebDriver
from seldom.running.config import Seldom
from seldom.logging import log


class TestCase(unittest.TestCase, WebDriver):

    def assertTitle(self, title=None):
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
                log.info("assert title: {title}.".format(title=self.get_title))
                break
            except AssertionError:
                sleep(1)
        else:
            log.error("assert fail: {title}.".format(title=title))
            self.assertEqual(title, self.get_title)

    def assertInTitle(self, title=None):
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
                log.info("assertIn title: {title}.".format(title=self.get_title))
                break
            except AssertionError:
                sleep(1)
        else:
            log.error("assertIn fail: {title}.".format(title=title))
            self.assertIn(title, self.get_title)

    def assertUrl(self, url):
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
                log.info("assert url: {url}.".format(url=self.get_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.error("assert fail: {url}.".format(url=url))
            self.assertEqual(url, self.get_url)

    def assertInUrl(self, url=None):
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
                log.info("assertIn url: {url}.".format(url=self.get_url))
                break
            except AssertionError:
                sleep(1)
        else:
            log.error("assertIn fail: {url}.".format(url=url))
            self.assertIn(url, self.get_url)

    def assertText(self, text=None):
        """
        Asserts whether the text of the current page conforms to expectations.

        Usage:
        self.assertText("text")
        """
        if text is None:
            raise AssertionError("The assertion text cannot be empty.")

        elem = self.driver.find_element_by_tag_name("html")
        for _ in range(Seldom.timeout):
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
