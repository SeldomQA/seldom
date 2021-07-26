"""
Seldom configuration file
"""


class Seldom:
    """
    Seldom browser driver
    """
    driver = None
    timeout = 10
    debug = False
    base_url = None


class BrowserConfig:
    """
    Define run browser config
    """
    NAME = None
    REPORT_PATH = None
    LOG_PATH = None
