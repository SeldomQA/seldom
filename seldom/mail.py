import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from seldom.running.config import BrowserConfig, RunResult
from seldom.logging import log


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
            <table width="50%" cellpadding="0" cellspacing="0"
                style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;display:inline-block;font-size:14px;overflow:hidden;border-radius:7px;background-color:#fff;margin:0;border:1px solid #e9e9e9"
                bgcolor="#fff">
                <tbody>
                    <tr
                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:16px;vertical-align:top;color:#fff;font-weight:500;text-align:center;border-radius:3px 3px 0 0;background-color:#354052;margin:0;padding:20px"
                            align="center" bgcolor="#354052" valign="top">
                            <span style="margin-top:20px;display:block"> Seldom Test Report </span>
                        </td>
                    </tr>
                    <tr
                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;vertical-align:top;margin:0;padding:20px"
                            valign="top">
                            <font color="#888888">
                            </font>
                            <font color="#888888">

                            </font>
                            <table width="100%" cellpadding="0" cellspacing="0"
                                style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">

                                <tbody>
                                    <tr
                                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;vertical-align:top;margin:0;padding:0 0 20px"
                                            valign="top">
                                            通过用例: {mail_pass}
                                        </td>
                                    </tr>

                                    <tr
                                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;vertical-align:top;margin:0;padding:0 0 20px"
                                            valign="top">
                                            失败用例: {mail_fail}
                                        </td>
                                    </tr>

                                    <tr
                                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;vertical-align:top;margin:0;padding:0 0 20px"
                                            valign="top">
                                            错误用例: {mail_error}
                                        </td>
                                    </tr>

                                    <tr
                                        style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;margin:0">
                                        <td style="font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;box-sizing:border-box;font-size:14px;vertical-align:top;margin:0;padding:0 0 20px"
                                            valign="top">
                                            跳过用例: {mail_skip}
                                        </td>
                                    </tr>   
                                </tbody>
                            </table>
                            <font color="#888888">
                            </font>
                        </td>
                    </tr>
                </tbody>
            </table>
            """.format(mail_pass=str(RunResult.passed), 
                       mail_fail=str(RunResult.failed),
                       mail_error=str(RunResult.errors),
                       mail_skip=str(RunResult.skiped))
        
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
    smtp = SMTP("user@126.com", "password", "smtp.126.com")
    smtp.sender("recipient@126.com")
