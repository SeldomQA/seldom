import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from .running.test_runner import BrowserConfig
from .logging import log


class SMTP(object):

    def __init__(self, user, password, host, port=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = str(port) if port is not None else "465"

    def sender(self, to=None, subject=None, contents=None, attachments=None):
        if to is None:
            raise ValueError("Please specify the email address to send")

        if subject is None:
            subject = 'Seldom Test Report'
        if contents is None:
            contents = """
            <div class="heading card">
                <h1>Seldom Test Report</h1>
            </div>
            """

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.user
        msg['To'] = to

        text = MIMEText(contents, 'html', 'utf-8')
        msg.attach(text)

        if attachments is None:
            attachments = BrowserConfig.report_path

        att_name = "report.html"
        if "\\" in attachments:
            att_name = attachments.split("\\")[-1]
        if "/" in attachments:
            att_name = attachments.split("/")[-1]

        att = MIMEApplication(open(attachments, 'rb').read())
        att['Content-Type'] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(att_name)
        msg.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(self.host)
        smtp.login(self.user, self.password)
        smtp.sendmail(self.user, to, msg.as_string())
        smtp.quit()
        log.info("Email sent successfully!!")


if __name__ == '__main__':
    smtp = SMTP("testingwtb@126.com", "a123456", "smtp.126.com")
    smtp.sender("testingwtb@126.com", attachments=r"D:\git\seldom\reports\2020_03_17_00_03_31_result.html")
