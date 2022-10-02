"""
send message file
"""
import os
from XTestRunner import SMTP as XSMTP
from XTestRunner import DingTalk as XDingTalk
from seldom.running.config import BrowserConfig
from seldom.utils import file


class SMTP(XSMTP):
    """send email class"""

    def sendmail(self, to: [str, list], subject: str = None, attachments: str = None, delete: bool = False) -> None:
        """
        seldom send email
        :param to:
        :param subject:
        :param attachments:
        :param delete: delete report&log file
        :return
        """
        if attachments is None:
            attachments = BrowserConfig.REPORT_PATH
        if subject is None:
            subject = BrowserConfig.REPORT_TITLE
        self.sender(to=to, subject=subject, attachments=attachments)
        if delete is True:
            file.remove(BrowserConfig.REPORT_PATH)
            is_exist = os.path.isfile(BrowserConfig.LOG_PATH)
            if is_exist is True:
                with open(BrowserConfig.LOG_PATH, "r+", encoding="utf-8") as log_file:
                    log_file.truncate(0)


class DingTalk(XDingTalk):
    """
    send dingtalk, Inherit XTestRunner DingTalk Class
    """
