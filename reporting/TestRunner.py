# coding=utf-8
from TestReport import HTMLTestRunner
import unittest
import time
import os


class TestRunner(object):

    def __init__(self, cases="./"):
        self.cases = cases

    def run(self, title_text='Pyse Test Report', description_text=''):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases+'\\report')
            os.mkdir(self.cases+'\\report'+'\\image')
        
        base_dir = os.path.dirname(os.path.dirname(__file__))
        f = open(base_dir+"\\reporting\\report.txt", "w")
        f.write(self.cases+'\\report'+'\\image')

        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        filename = self.cases+'\\report\\'+now+'result.html'
        fp = file(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title=title_text, description=description_text)
        discover = unittest.defaultTestLoader.discover(self.cases, pattern='*_case.py', top_level_dir=None)
        runner.run(discover)
        fp.close()


if __name__ == '__main__':
    test = TestRunner()
    test.run()
