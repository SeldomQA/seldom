# coding=utf-8
import os
import time
import logging
import unittest
from .HTML_test_runner import HTMLTestRunner

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main(path=None,
         title="pyse Test Report",
         description="Test case execution",
         debug=False):
    """
    runner test case
    :param path:
    :param title:
    :param description:
    :param debug:
    :return:
    """
    if path is None:
        path = "./"

    if debug is False:
        for filename in os.listdir(path):
            if filename == "reports":
                break
        else:
            os.mkdir(path + '/reports')

        now = time.strftime("%Y_%m_%d_%H_%M_%S")

        with(open("./reports/" + now + "result.html", 'wb')) as fp:
            tests = unittest.defaultTestLoader.discover(path, pattern='test*.py')
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            runner.run(tests)
    else:
        tests = unittest.defaultTestLoader.discover(path, pattern='test*.py')
        runner = unittest.TextTestRunner(verbosity=2)
        logger.info("pyse run test 🛫🛫!")
        runner.run(tests)
        logger.info("End of the test 🔚!")


if __name__ == '__main__':
    main()

