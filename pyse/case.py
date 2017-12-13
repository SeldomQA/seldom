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

    def assertTitle(self, title, second=3, msg=None):
        '''
        Asserts whether the current title is in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertTitle("title"[,second,msg])
        '''
        if title == None:
            raise NameError("'title' can't be empty.")
        for s in range(second):
            try:
                self.assertIn(title, self.driver.get_title(), msg)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(title, self.driver.get_title(), msg)

    def assertNotTitle(self, title, second=3, msg=None):
        '''
        Asserts whether the current title is NOT in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertNotTitle("title"[,second,msg])
        '''
        if title == None:
            raise NameError("'title' can't be empty.")
        for s in range(second):
            try:
                self.assertNotIn(title, self.driver.get_title(), msg)
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertNotIn(title, self.driver.get_title(), msg)

    def assertUrl(self, url, second=3, msg=None):
        '''
        Asserts whether the current URL is in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertUrl("url"[,second,msg])
        '''
        if url == None:
            raise NameError("'URL' can't be empty.")
        for s in range(second):
            try:
                self.assertEqual(url, self.driver.get_url(), msg)
            except AssertionError:
                sleep(1)
        else:
            self.assertEqual(url, self.driver.get_url(), msg)

    def assertNotUrl(self, url, second=3, msg=None):
        '''
        Asserts whether the current URL is NOT in line with expectations.
        The default is 3 seconds.

        Usage:
        driver.assertNotUrl("url"[,second,msg])
        '''
        if url == None:
            raise NameError("'URL' can't be empty.")
        for s in range(second):
            try:
                self.assertNotEqual(url, self.driver.get_url(), msg)
            except AssertionError:
                sleep(1)
        else:
            self.assertNotEqual(url, self.driver.get_url(), msg)

    def assertText(self, actual_el, expect_result, msg=None):
        '''
        Asserts whether the text of the current page conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        driver.assertText("#el","text"[,msg])
        '''
        if actual_el == None or expect_result == None:
            raise NameError("'actual' or 'exect' can't be empty.")
        actual_result = self.driver.get_text(actual_el)
        self.assertEqual(actual_result, expect_result, msg)

    def assertNotText(self, actual_el, expect_result, msg=None):
        '''
        Asserts whether the text of the current page NOT conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        driver.assertNotText("#el","text"[,msg])
        '''
        if actual_el == None or expect_result == None:
            raise NameError("'actual' or 'exect' can't be empty.")
        actual_result = self.driver.get_text(actual_el)
        self.assertNotEqual(actual_result, expect_result, msg)
