import os
import sys
import time
import inspect
from loguru import logger
from seldom.running.config import BrowserConfig
from seldom.running.config import Seldom

stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
if BrowserConfig.LOG_PATH is None:
    BrowserConfig.LOG_PATH = os.path.join(os.getcwd(), "reports", "seldom_log.log")
if BrowserConfig.REPORT_PATH is None:
    BrowserConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", now_time + "_result.html")


class Logger:
    def __init__(self, level: str = "INFO", colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._formator = "<fg #66CDAA>[<fg #FA8072>{level}</> {time:YYMMDD HH:mm:ss} {file}]</>  <lvl>{message}</lvl>"
        self._lvl = level
        self.logfile = open(BrowserConfig.LOG_PATH, "w")
        self.df_config(self._colorlog, self._formator, self._lvl)

    def __del__(self):
        self.logfile.close()

    def df_config(self, colorlog: bool, formator: str, console_lvl: str, log_lvl: str = "DEBUG"):
        self.logger.configure(
            handlers=[
                dict(sink=sys.stderr, level=console_lvl, colorize=colorlog, format=formator),
                dict(sink=self.logfile, level=log_lvl, format=formator),
            ],
            # levels=[dict(name="INFO", no=20, color="<yellow>")],
        )

    def set_level(self, console_lvl: str, log_lvl: str = "DEBUG"):
        self.logger.configure(
            handlers=[
                dict(sink=sys.stderr, level=console_lvl, colorize=self._colorlog, format=self._formator),
                dict(sink=self.logfile, level=log_lvl, format=self._formator),
            ],
        )

    def trace(self, msg: str):
        now = time.strftime("-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [DEBUG] " + str(msg))
        return self.logger.trace(msg)

    def debug(self, msg: str):
        now = time.strftime("-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [DEBUG] " + str(msg))
        return self.logger.debug(msg)

    def info(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [INFO] " + str(msg))
        return self.logger.info(msg)

    def success(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [WARNING] " + str(msg))
        return self.logger.success(msg)

    def warn(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [WARNING] " + str(msg))
        return self.logger.warning(msg)

    def error(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [ERROR] " + str(msg))
        return self.logger.error(msg)

    def critical(self, msg: str):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        if Seldom.debug is False:
            print(now + " [ERROR] " + str(msg))
        return self.logger.critical(msg)

    def printf(self, msg: str):
        return self.logger.success(msg)


log = Logger(level="INFO")
