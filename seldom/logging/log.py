import io
import os
import sys
import time
import inspect
from loguru._logger import Core as _Core
from loguru._logger import Logger
from seldom.running.config import BrowserConfig


stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
exec_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(exec_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)

now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
if BrowserConfig.LOG_PATH is None:
    BrowserConfig.LOG_PATH = os.path.join(report_dir, "seldom_log.log")
if BrowserConfig.REPORT_PATH is None:
    BrowserConfig.REPORT_PATH = os.path.join(report_dir, now_time + "_result.html")


class SeldomLogger(Logger):

    def __init__(self, level: str = "DEBUG", colorlog: bool = True):
        self._colorlog = colorlog
        self._console_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</> {file} <level>| {level} | {message}</level>"
        self._log_format = "{time: YYYY-MM-DD HH:mm:ss} {file} | {level} | {message}"
        self._level = level
        self.logfile = BrowserConfig.LOG_PATH
        self.stderr_bak = sys.stderr
        super().__init__(core=_Core(),
                         exception=None,
                         depth=0,
                         record=False,
                         lazy=False,
                         colors=False,
                         raw=False,
                         capture=True,
                         patcher=None,
                         extra={})
        self.set_level(self._colorlog, self._console_format, self._level)

    def set_level(self, colorlog: bool = True, format: str = None, level: str = "TRACE"):
        if format is None:
            format = self._console_format
        self.remove()
        sys.stderr = io.StringIO()
        self.add(sys.stderr, level=level, format=format)
        self.add(self.stderr_bak, level=level, colorize=colorlog, format=format)
        self.add(self.logfile, level=level, colorize=colorlog, format=self._log_format, encoding="utf-8")


# log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR
log = SeldomLogger(level="TRACE")
