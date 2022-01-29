# coding=utf-8
import os
import re
import ast
import json as sys_json
import inspect
import unittest
import webbrowser
from xmlrunner import XMLTestRunner
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from seldom.driver import Browser
from seldom.logging import log
from seldom.logging.exceptions import SeldomException
from seldom.running.DebugTestRunner import DebugTestRunner
from seldom.running.HTMLTestRunner import HTMLTestRunner
from seldom.running.config import Seldom, BrowserConfig
from seldom.running.loader_extend import seldomTestLoader


INIT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__init__.py")
_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open(INIT_FILE, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

seldom_str = """
              __    __              
   ________  / /___/ /___  ____ ____ 
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v{v}
-----------------------------------------
                             @itest.info
""".format(v=version)


class TestMain(object):
    """
    Reimplemented Seldom Runner, Support for Web and API
    """
    TestSuits = []

    def __init__(self, path=None, browser=None, base_url=None, debug=False, timeout=10,
                 report=None, title="Seldom Test Report", description="Test case execution",
                 rerun=0, save_last_run=False, whitelist=[], blacklist=[], auto=True):
        """
        runner test case
        :param path:
        :param browser:
        :param base_url:
        :param report:
        :param title:
        :param description:
        :param debug:
        :param timeout:
        :param rerun:
        :param save_last_run:
        :param whitelist:
        :param blacklist:
        :param auto:
        :return:
        """
        print(seldom_str)
        self.path = path
        self.browser = browser
        self.report = report
        self.title = title
        self.description = description
        self.debug = debug
        self.rerun = rerun
        self.save_last_run = save_last_run
        self.whitelist = whitelist
        self.blacklist = blacklist

        if isinstance(timeout, int) is False:
            raise TypeError("Timeout {} is not integer.".format(timeout))

        if isinstance(debug, bool) is False:
            raise TypeError("Debug {} is not Boolean type.".format(debug))

        Seldom.timeout = timeout
        Seldom.debug = debug
        Seldom.base_url = base_url

        # ----- Global open browser -----
        self.open_browser()

        if self.path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            print(ins.filename)
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            self.TestSuits = seldomTestLoader.discover(file_dir, this_file)
        else:
            if len(self.path) > 3:
                if self.path[-3:] == ".py":
                    if "/" in self.path:
                        path_list = self.path.split("/")
                        path_dir = self.path.replace(path_list[-1], "")
                        self.TestSuits = seldomTestLoader.discover(path_dir, pattern=path_list[-1])
                    else:
                        self.TestSuits = seldomTestLoader.discover(os.getcwd(), pattern=self.path)
                else:
                    self.TestSuits = seldomTestLoader.discover(self.path)
            else:
                self.TestSuits = seldomTestLoader.discover(self.path)

        if auto is True:
            self.run(self.TestSuits)

        # ----- Close browser globally -----
        self.close_browser()

    def run(self, suits):
        """
        run test case
        """
        if self.debug is False:
            for filename in os.listdir(os.getcwd()):
                if filename == "reports":
                    break
            else:
                os.mkdir(os.path.join(os.getcwd(), "reports"))

            if (self.report is None) and (BrowserConfig.REPORT_PATH is not None):
                report_path = BrowserConfig.REPORT_PATH
            else:
                report_path = BrowserConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", self.report)

            with(open(report_path, 'wb')) as fp:
                if report_path.split(".")[-1] == "xml":
                    runner = XMLTestRunner(output=fp)
                    runner.run(suits)
                else:
                    runner = HTMLTestRunner(stream=fp, title=self.title, description=self.description,
                                            blacklist=self.blacklist, whitelist=self.whitelist)
                    runner.run(suits, rerun=self.rerun, save_last_run=self.save_last_run)

            log.printf("generated html file: file:///{}".format(report_path))
            log.printf("generated log file: file:///{}".format(BrowserConfig.LOG_PATH))
            webbrowser.open_new("file:///{}".format(report_path))
        else:
            runner = DebugTestRunner(
                blacklist=self.blacklist,
                whitelist=self.whitelist,
                verbosity=2)
            runner.run(suits)
            log.printf("A run the test in debug mode without generating HTML report!")

    def open_browser(self):
        """
        If you set up a browser, open the browser
        """
        if self.browser is not None:
            BrowserConfig.NAME = self.browser
            Seldom.driver = Browser(BrowserConfig.NAME)

    @staticmethod
    def close_browser():
        """
        How to open the browser, close the browser
        """
        if isinstance(Seldom.driver, SeleniumWebDriver):
            Seldom.driver.quit()
            Seldom.driver = None


class TestMainExtend(TestMain):
    """
    TestMain tests class extensions.
    1. Collect use case information and return to the list
    2. Execute the use cases based on the use case list
    """

    def __init__(self, path=None, browser=None, base_url=None, debug=False, timeout=10,
                 report=None, title="Seldom Test Report", description="Test case execution",
                 rerun=0, save_last_run=False, whitelist=[], blacklist=[], auto=False):

        if path is None:
            raise FileNotFoundError("Specify a file path")

        super().__init__(path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
                         report=report, title=title, description=description,
                         rerun=rerun, save_last_run=save_last_run, whitelist=whitelist, blacklist=blacklist,
                         auto=auto)

    @staticmethod
    def collect_cases(json=False):
        """
        Return the collected case information.
        SeldomTestLoader.collectCaseInfo = True
        """
        if json is True:
            return sys_json.dumps(seldomTestLoader.collectCaseList)
        return seldomTestLoader.collectCaseList

    @staticmethod
    def _diff_case(file_name: str, class_name: str, method_name: str, data: list) -> bool:
        """
        Diff use case information
        :param file_name:
        :param class_name:
        :param method_name:
        :param data:
        :return:
        """
        for d in data:
            d_file = d.get("file", None)
            d_class = d.get("class").get("name", None)
            d_method = d.get("method").get("name", None)
            if (d_file is None) or (d_class is None) or (d_method is None):
                raise SeldomException(
                    """Use case format error, please refer to: https://github.com/SeldomQA/seldom/blob/master/docs/platform.md""")
            if file_name == d_file and class_name == d_class and method_name == d_method:
                return True

        return False

    def run_cases(self, data: list) -> None:
        """
        run list case
        :param data:
        :return:
        """
        if isinstance(data, list) is False:
            raise TypeError("Use cases must be lists.")

        if len(data) == 0:
            log.error("There are no use cases to execute")
            return

        suit = unittest.TestSuite()
        for suits in self.TestSuits:
            for cases in suits:
                for case in cases:
                    file_name = case.__module__
                    class_name = case.__class__.__name__
                    method_name = str(case).split(" ")[0]
                    ret = self._diff_case(file_name, class_name, method_name, data)
                    if ret is True:
                        suit.addTest(case)

        self.run(suit)
        self.close_browser()


main = TestMain

if __name__ == '__main__':
    main()
