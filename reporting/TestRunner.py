#coding=utf-8
from selenium import webdriver
import unittest,HTMLTestRunner
import time,os

class TestRunner(object):

    def __init__(self,testcase):
        self.testcase = testcase

    def run(self):

        now = time.strftime("%Y-%m-%d %H_%M_%S")

        for filename in os.listdir(self.testcase):
            if filename == "report":
                break
        else:
            os.mkdir(self.testcase+'\\report')

        filename = self.testcase+'\\report\\'+now+'result.html'
        fp = file(filename, 'wb')
        runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Automated test report',description='Test case execution results')
        discover=unittest.defaultTestLoader.discover(self.testcase,pattern='*_case.py',top_level_dir=None)
        runner.run(discover)
        fp.close()

if __name__ == '__main__':
    test = TestRunner("D:\\mz_test\\mztestpro\\test")
    test.run()