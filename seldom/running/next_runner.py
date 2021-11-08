# coding=utf-8
import os
import re
import ast
import unittest
import webbrowser
from xmlrunner import XMLTestRunner
import inspect
from seldom.logging import log
from seldom.driver import Browser
from seldom.running.HTMLTestRunner import HTMLTestRunner
from seldom.running.config import Seldom, BrowserConfig
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver

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
    def __init__(self, path=None, browser=None, base_url=None, debug=False, timeout=10,
                 report=None, title="Seldom Test Report", description="Test case execution",
                 rerun=0, save_last_run=False):
        """
        runner test case
        :param path:
        :param browser:
        :param base_url:
        :param report:
        :param title:
        :param description:
        :param debug:
        :param rerun:
        :param save_last_run:
        :param timeout:
        :return:
        """
        print(seldom_str)
        self.path = path
        self.report = report
        self.title = title
        self.description = description
        self.debug = debug
        self.rerun = rerun
        self.save_last_run = save_last_run

        if isinstance(timeout, int) is False:
            raise TypeError("Timeout {} is not integer.".format(timeout))

        if isinstance(debug, bool) is False:
            raise TypeError("Debug {} is not Boolean type.".format(debug))

        Seldom.timeout = timeout
        Seldom.debug = debug
        Seldom.base_url = base_url

        # Global launch browser
        if browser is not None:
            BrowserConfig.NAME = browser
            Seldom.driver = Browser(BrowserConfig.NAME)

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
            suits = unittest.defaultTestLoader.discover(file_dir, this_file)
        else:
            if len(self.path) > 3:
                if self.path[-3:] == ".py":
                    if "/" in self.path:
                        path_list = self.path.split("/")
                        path_dir = self.path.replace(path_list[-1], "")
                        suits = unittest.defaultTestLoader.discover(path_dir, pattern=path_list[-1])
                    else:
                        suits = unittest.defaultTestLoader.discover(os.getcwd(), pattern=self.path)
                else:
                    suits = unittest.defaultTestLoader.discover(self.path)
            else:
                suits = unittest.defaultTestLoader.discover(self.path)

        self._run_test_case(suits)

        # Close browser globally
        if isinstance(Seldom.driver, SeleniumWebDriver):
            Seldom.driver.quit()

    def _run_test_case(self, suits):
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
                    runner = HTMLTestRunner(stream=fp, title=self.title, description=self.description)
                    runner.run(suits, rerun=self.rerun, save_last_run=self.save_last_run)

            log.printf("generated html file: file:///{}".format(report_path))
            log.printf("generated log file: file:///{}".format(BrowserConfig.LOG_PATH))
            webbrowser.open_new("file:///{}".format(report_path))
        else:
            runner = unittest.TextTestRunner(verbosity=2)
            runner.run(suits)
            log.printf("A run the test in debug mode without generating HTML report!")


main = TestMain


if __name__ == '__main__':
    main()
