from XTestRunner import SMTP as XSMTP
from XTestRunner import DingTalk as XDingTalk
from seldom.running.config import BrowserConfig


class SMTP(XSMTP):

    def sendmail(self, to, subject=None, attachments=None):
        """
        seldom send email
        :param to:
        :param subject:
        :param attachments:
        :return
        """
        if attachments is None:
            attachments = BrowserConfig.REPORT_PATH
        if subject is None:
            subject = BrowserConfig.REPORT_TITLE
        self.sender(to=to, subject=subject, attachments=attachments)


class DingTalk(XDingTalk):
    """
    send dingtalk, Inherit XTestRunner DingTalk Class
    """
