# coding=utf-8
import os
import time
import unittest
from ..logging import log
from ..driver import browser as b
from .HTMLTestRunner import HTMLTestRunner

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


class Seldom:
    """
    Seldom browser driver
    """
    driver = None


class BrowserConfig:
    """
    Define run browser config
    """
    name = None
    driver_path = None
    grid_url = None


def main(path=None,
         browser=None,
         title="Seldom Test Report",
         description="Test case execution",
         debug=False,
         rerun=0,
         save_last_run=False,
         driver_path=None,
         grid_url=None):
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
    :param grid_url:
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
        BrowserConfig.name = "chrome"
    else:
        BrowserConfig.name = browser
        BrowserConfig.grid_url = grid_url

    if driver_path is not None:
        ret = os.path.exists(driver_path)
        if ret is False:
            raise ValueError("Browser - driven path error，Please check if the file exists. => {}".format(driver_path))
        BrowserConfig.driver_path = driver_path

    """
    Global launch browser
    """
    Seldom.driver = b(BrowserConfig.name, BrowserConfig.driver_path, BrowserConfig.grid_url)

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
            log.info(seldom_str)
            runner.run(suits, rerun=rerun, save_last_run=save_last_run)
        print("generated html file: file:///{}".format(report))
    else:
        runner = unittest.TextTestRunner(verbosity=2)
        log.info("A run the test in debug mode without generating HTML report!")
        log.info(seldom_str)
        runner.run(suits)

    """
    Close browser globally
    """
    Seldom.driver.quit()


if __name__ == '__main__':
    main()
