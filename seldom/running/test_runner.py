# coding=utf-8
import os
import sys
import time
import logging
import unittest
from .HTMLTestRunner import HTMLTestRunner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


seldom_str = """
            _      _                   
           | |    | |                  
 ___   ___ | |  __| |  ___   _ __ ___  
/ __| / _ \| | / _` | / _ \ | '_ ` _ \ 
\__ \|  __/| || (_| || (_) || | | | | |
|___/ \___||_| \__,_| \___/ |_| |_| |_| 
-----------------------------------------
                             @itest.info
"""


class Browser:
    """
    Define run browser name
    """
    name = None
    driver_path = None


def main(path=None,
         browser=None,
         title="Seldom Test Report",
         description="Test case execution",
         debug=False,
         rerun=0,
         save_last_run=False,
         driver_path=None):
    """
    runner test case
    :param path:
    :param browser:
    :param title:
    :param description:
    :param debug:
    :param rerun:
    :param save_last_run:
    :param driver_path:
    :return:
    """

    if path is None:
        suits = unittest.defaultTestLoader.discover(os.getcwd())
    else:
        if len(path) > 3:
            if path[-3:] == ".py":
                if "/" in path:
                    path_list = path.split("/")
                    path_dir = path.replace(path_list[-1], "")
                    suits = unittest.defaultTestLoader.discover(path_dir, pattern=path_list[-1])
                else:
                    suits = unittest.defaultTestLoader.discover(os.getcwd(), pattern=path)
            else:
                suits = unittest.defaultTestLoader.discover(path)
        else:
            suits = unittest.defaultTestLoader.discover(path)

    if browser is None:
        Browser.name = "chrome"
    else:
        Browser.name = browser

    if driver_path is not None:
        ret = os.path.exists(driver_path)
        if ret is False:
            raise ValueError("Browser - driven path error，Please check if the file exists. => {}".format(driver_path))
        Browser.driver_path = driver_path

    if debug is False:
        for filename in os.listdir(os.getcwd()):
            if filename == "reports":
                break
        else:
            os.mkdir(os.path.join(os.getcwd(), "reports"))

        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        report = os.path.join(os.getcwd(), "reports", now + "_result.html")

        with(open(report, 'wb')) as fp:
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            print(seldom_str)
            runner.run(suits, rerun=rerun, save_last_run=save_last_run)
        print("generated html file: file:///{}".format(report))
    else:
        runner = unittest.TextTestRunner(verbosity=2)
        logger.info("seldom run test 🛫🛫!")
        print(seldom_str)
        runner.run(suits)
        logger.info("End of the test 🔚!")


if __name__ == '__main__':
    main()

