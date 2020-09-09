"""
Seldom configuration file
"""


class Seldom:
    """
    Seldom browser driver
    """
    application = None
    driver = None
    timeout = None
    debug = None

    # app config
    command_executor = None
    desired_capabilities = None


class BrowserConfig:
    """
    Define run browser config
    """
    name = None
    driver_path = None
    grid_url = None
    report_path = None


class RunResult:
    """
    Test run results
    """
    passed = 0
    failed = 0
    errors = 0
    skiped = 0
