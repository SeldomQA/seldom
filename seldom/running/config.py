"""
Seldom configuration file
"""


class Seldom:
    """
    Seldom browser driver
    """
    driver = None
    timeout = None
    debug = None


class BrowserConfig:
    """
    Define run browser config
    """
    name = None
    report_path = None


class RunResult:
    """
    Test run results
    """
    passed = 0
    failed = 0
    errors = 0
    skiped = 0
