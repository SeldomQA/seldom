import sys
import logging.handlers
from colorama import Fore, Style

_logger = logging.getLogger('seldom')
_logger.setLevel(logging.DEBUG)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
_logger.addHandler(_handler)


def debug(msg):
    _logger.debug("DEBUG " + str(msg))


def info(msg):
    _logger.info(Fore.GREEN + "INFO " + str(msg) + Style.RESET_ALL)


def error(msg):
    _logger.error(Fore.RED + "ERROR " + str(msg) + Style.RESET_ALL)


def warn(msg):
    _logger.warning(Fore.YELLOW + "WARNING " + str(msg) + Style.RESET_ALL)


def _print(msg):
    _logger.debug(Fore.BLUE + "PRINT " + str(msg) + Style.RESET_ALL)


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
