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
    compare_url = None
    app_server = None
    app_info = None
    env = None
    api_data_url = None


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
    executable_path = ""


class AppConfig:
    """
    Define run uiautomator2 and facebook-wda config
    """
    PERF_OUTPUT_FOLDER = None
    PERF_RUN_FOLDER = None
    REPORT_IMAGE = []
    WRITE_EXCEL = []
    FPS = 45
    FRAME_SECONDS = 5
    DURATION_TIMES = 3
    STRESS_TIMES = 3
    log = False
