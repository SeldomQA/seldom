# coding=utf-8
import time
import os


class TestRunner(object):

    def __init__(self, cases="./"):
        self.cases = cases

    def run(self):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases+'/report')

        # base_dir = os.path.dirname(os.path.dirname(__file__))
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        test_report = "nosetests "+self.cases+" --with-html --html-report="+self.cases+"report/"+now+"report.html"
        # print test_report
        os.system(test_report)


if __name__ == '__main__':
    test = TestRunner()
    test.run()
