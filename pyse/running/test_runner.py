# coding=utf-8
import time
import os
from .HTML_test_runner import HTMLTestRunner
import unittest


class TestRunner(object):
    ''' Run test '''

    def __init__(self, cases="./",title="pyse Test Report",description="Test case execution"):
        self.cases = cases
        self.title = title
        self.des = description

    def run(self):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases+'/report')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        fp = open("./report/" + now + "result.html", 'wb')
        tests = unittest.defaultTestLoader.discover(self.cases,pattern='test*.py',top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases, pattern='test*.py', top_level_dir=None)
        runner = unittest.TextTestRunner(verbosity=2)
        print("pyse test start:")
        runner.run(tests)
        print("test end!!!")


if __name__ == '__main__':
    test = TestRunner()
    test.run()
