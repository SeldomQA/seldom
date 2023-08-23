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
    REPORT_FOLDER = None
    REPORT_IMAGE = []
    record = False
    fps = 45
    frame_second = 5
    threadLock = False
    log = False
    iOS_perf_obj = None
    duration_times = 3
    stress_times = 3
    CASE_ERROR = []
    PERF_ERROR = []
    LOGS_ERROR = []
    WRITE_EXCEL = []
