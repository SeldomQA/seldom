import os
import sys
import time
import inspect
import platform
import logging.handlers
from colorama import Fore, Style
from seldom.running.config import BrowserConfig

__all__ = [
    "debug", "info", "error", "warn", "_print",
    "set_level", "set_level_to_debug", "set_level_to_info", "set_level_to_warn", "set_level_to_error"
]

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
file_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(file_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)


now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
if BrowserConfig.LOG_PATH is None:
    BrowserConfig.LOG_PATH = os.path.join(os.getcwd(), "reports", now_time + "_log.log")
if BrowserConfig.REPORT_PATH is None:
    BrowserConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", now_time + "_result.html")

file_handler = logging.FileHandler(BrowserConfig.LOG_PATH, encoding='utf-8')


_logger = logging.getLogger('seldom')
_logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler(sys.stdout)


if platform.system().lower() == "windows":
    _logger.addHandler(file_handler)
    _logger.addHandler(_handler)
else:
    _logger.addHandler(file_handler)
    _logger.addHandler(_handler)
    # _logger.removeHandler(_handler)


def debug(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(now + " [DEBUG] " + str(msg))


def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.info(Fore.GREEN + now + " [INFO] " + str(msg) + Style.RESET_ALL)


def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.error(Fore.RED + now + " [ERROR] " + str(msg) + Style.RESET_ALL)


def warn(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.warning(Fore.YELLOW + now + " [WARNING] " + str(msg) + Style.RESET_ALL)


def _print(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(Fore.BLUE + now + " [PRINT] " + str(msg) + Style.RESET_ALL)


def set_level(level):
    """ 设置log级别

    :param level: logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR
    :return:
    """
    _logger.setLevel(level)


def set_level_to_debug():
    _logger.setLevel(logging.DEBUG)


def set_level_to_info():
    _logger.setLevel(logging.INFO)


def set_level_to_warn():
    _logger.setLevel(logging.WARN)


def set_level_to_error():
    _logger.setLevel(logging.ERROR)
