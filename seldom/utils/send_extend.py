from XTestRunner import SMTP as XSMTP
from XTestRunner import DingTalk as XDingTalk
from seldom.running.config import BrowserConfig
from seldom.utils import file


class SMTP(XSMTP):

    def sendmail(self, to, subject=None, attachments=None, delete=False):
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
            file.remove(BrowserConfig.LOG_PATH)


class DingTalk(XDingTalk):
    """
    send dingtalk, Inherit XTestRunner DingTalk Class
    """
