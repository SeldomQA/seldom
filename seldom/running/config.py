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
    name = None
    report_path = None
