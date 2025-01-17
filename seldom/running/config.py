"""
Seldom configuration file
"""
import logging
import threading
import requests


class Seldom:
    """
    Seldom browser driver
    """
    _thread_local = threading.local()

    @property
    def driver(self):
        """
        Browser or App driver
        """
        return getattr(self._thread_local, 'driver', None)

    @driver.setter
    def driver(self, value):
        self._thread_local.driver = value

    @property
    def base_url(self):
        """
        API base url
        """
        return getattr(self._thread_local, 'base_url', None)

    @base_url.setter
    def base_url(self, value):
        self._thread_local.base_url = value

    timeout = 10
    debug = False
    compare_url = None
    app_server = None
    app_info = None
    app_package = None
    extensions = None
    env = None
    api_data_url = None
    benchmark = False


Seldom = Seldom()


class BrowserConfig:
    """
    Define run browser config
    """
    NAME = None
    REPORT_PATH = None
    REPORT_TITLE = "Seldom Test Report"
    LOG_PATH = None

    # driver config
    options = None
    command_executor = ""
    executable_path = None


def base_url():
    """return base url"""
    return Seldom.base_url


def driver():
    """return driver"""
    return Seldom.driver


def env():
    """return env"""
    return Seldom.env


class FileRunningConfig:
    """
    file runner config
    """
    api_excel_file_name = None


def report_local_style() -> bool:
    """
    Check report with local style
    :return:
    """
    try:
        resp = requests.get("https://telegraph-image-cq2.pages.dev")
        if resp.status_code != 200:
            return True
        else:
            return False
    except BaseException as msg:
        logging.debug(msg)
        return True
