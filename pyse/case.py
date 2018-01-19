import unittest
from pyse import Pyse
from time import sleep


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def assertTitle(self, title, second=3):
        '''
        Asserts whether the current title is in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertTitle("title")
        '''
        if title == None:
            raise NameError("'title' can't be empty.")
        for s in range(second):
            try:
                self.assertIn(title, self.driver.get_title())
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(title, self.driver.get_title())

    def assertUrl(self, url, second=3):
        '''
        Asserts whether the current URL is in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertUrl("url")
        '''
        if url == None:
            raise NameError("'URL' can't be empty.")
        for s in range(second):
            try:
                self.assertEqual(url, self.driver.get_url())
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(url, self.driver.get_url())

    def assertText(self, actual_el, expect_result):
        '''
        Asserts whether the text of the current page conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        driver.assertText("#el","text")
        '''
        if actual_el is None or expect_result is None:
            raise NameError("'actual' or 'exect' can't be empty.")
        actual_result = self.driver.get_text(actual_el)
        self.assertEqual(actual_result, expect_result)

    def assertAlert(self, expect_text):
        '''
        Asserts whether the text of the current page conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        driver.assertText("#el","text")
        '''

        if expect_text is None:
            raise NameError("'expect_text' can't be empty.")
        alert_text = self.driver.get_alert_text()
        self.assertEqual(alert_text, expect_text)
