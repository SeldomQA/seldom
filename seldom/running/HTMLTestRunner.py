import os
import io
import sys
import copy
import time
import datetime
import unittest
from xml.sax import saxutils
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from seldom.logging import log

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")

# ---------------------------
# Define the HTML template directory
# --------------------------
env = Environment(loader=FileSystemLoader(HTML_DIR))


class OutputRedirector(object):
    """
    Wrapper to redirect stdout or stderr 
    """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


class RunResult:
    """
    Test run results
    """
    passed = 0
    failed = 0
    errors = 0
    skipped = 0


class CustomTemplate(object):
    """
    Define a HTML template for report customerization and generation.
    Overall structure of an HTML report
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
        3: 'skip',
    }

    DEFAULT_TITLE = 'Unit Test Report'

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(name)s</td>
    <td>%(desc)s</td>
    <td></td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail</a></td>
    <td>&nbsp;</td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'>
        <div class='testcase'>%(casename)s</div>
    </td>
    <td style="color: #495057">
        <div>%(desc)s</div>
    </td>
    <td style="color: #495057">
        <div>%(runtime)s s</div>
    </td>
    <td colspan='5' align='center'>
    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>
    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->
    </td>
    <td>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'>
        <div class='testcase'>%(casename)s</div>
    </td>
    <td style="color: #495057">
        <div>%(desc)s</div>
    </td>
    <td style="color: #495057">
        <div>%(runtime)s s</div>
    </td>
    <td colspan='5' align='center'>%(status)s</td>
    <td>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    IMG_TMPL = r"""
<a  onfocus='this.blur();' href="javacript:void(0);" onclick="show_img(this)">show</a>
<div align="center" class="screenshots"  style="display:none">
    <a class="close_shots"  onclick="hide_img(this)">❌</a>
    {images}
    <div class="imgyuan"></div>
</div>
"""


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    """
    note: _TestResult is a pure representation of results.
    It lacks the output and reporting ability compares to unittest._TextTestResult.
    """

    def __init__(self, verbosity=1, rerun=0, save_last_run=False):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.skip_count = 0
        self.verbosity = verbosity
        self.rerun = rerun
        self.save_last_run = save_last_run
        self.status = 0
        self.runs = 0
        self.result = []
        self.case_start_time = None
        self.case_end_time = None

    def startTest(self, test):
        self.case_start_time = time.time()
        test.images = getattr(test, "images", [])
        test.runtime = getattr(test, "runtime", None)
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        """
        Usually one of addSuccess, addError or addFailure would have been called.
        But there are some path in unittest that would bypass this.
        We must disconnect stdout in stopTest(), which is guaranteed to be called.
        """
        if self.rerun and self.rerun >= 1:
            if self.status == 1:
                self.runs += 1
                if self.runs <= self.rerun:
                    if self.save_last_run:
                        t = self.result.pop(-1)
                        if t[0] == 1:
                            self.failure_count -= 1
                        else:
                            self.error_count -= 1
                    test = copy.copy(test)
                    sys.stderr.write("Retesting... ")
                    sys.stderr.write(str(test))
                    sys.stderr.write('..%d \n' % self.runs)
                    doc = getattr(test, '_testMethodDoc', u"") or u''
                    if doc.find('->rerun') != -1:
                        doc = doc[:doc.find('->rerun')]
                    desc = "%s->rerun:%d" % (doc, self.runs)
                    if isinstance(desc, str):
                        desc = desc
                    test._testMethodDoc = desc
                    test(self)
                else:
                    self.status = 0
                    self.runs = 0
        self.complete_output()
        self.case_end_time = time.time()
        case_run_time = self.case_end_time - self.case_start_time
        test.runtime = "%.2f" % case_run_time

    def addSuccess(self, test):
        self.success_count += 1
        self.status = 0
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.' + str(self.success_count))

    def addError(self, test, err):
        self.error_count += 1
        self.status = 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if type(getattr(test, "driver", "")).__name__ == 'WebDriver':
            driver = getattr(test, "driver")
            test.images.append(driver.get_screenshot_as_base64())
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        self.status = 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if type(getattr(test, "driver", "")).__name__ == 'WebDriver':
            driver = getattr(test, "driver")
            test.images.append(driver.get_screenshot_as_base64())
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

    def addSkip(self, test, reason):
        self.skip_count += 1
        self.status = 0
        TestResult.addSkip(self, test, reason)
        output = self.complete_output()
        self.result.append((3, test, output, reason))
        if self.verbosity > 1:
            sys.stderr.write('S')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('S')


class HTMLTestRunner(CustomTemplate):
    """
    Run the test class
    """

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None, save_last_run=True):
        self.stream = stream
        self.verbosity = verbosity
        self.save_last_run = save_last_run
        self.run_times = 0
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = ""
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test, rerun=0, save_last_run=False):
        """
        Run the given test case or test suite.
        """
        result = _TestResult(self.verbosity, rerun=rerun, save_last_run=save_last_run)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.run_times += 1
        self.generate_report(test, result)
        return result

    def sort_result(self, result_list):
        """
        unittest does not seems to run in any particular order.
        Here at least we want to group them together by class.
        """
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def get_report_attributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []

        RunResult.passed = result.success_count
        RunResult.failed = result.failure_count
        RunResult.errors = result.error_count
        RunResult.skipped = result.skip_count
        if result.success_count:
            status.append('Passed:%s' % result.success_count)
        if result.failure_count:
            status.append('Failed:%s' % result.failure_count)
        if result.error_count:
            status.append('Errors:%s' % result.error_count)
        if result.skip_count:
            status.append('Skipped:%s' % result.skip_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'

        return [
            {"name": "Start Time", "value": startTime},
            {"name": "Duration", "value": duration},
            {"name": "Status", "value": status},
        ]

    def generate_report(self, test, result):
        template = env.get_template('template.html')
        stylesheet = env.get_template('stylesheet.html').render()
        report_attrs = self.get_report_attributes(result)

        generator = 'HTMLTestRunner %s' % "1.0.0"
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        chart = self._generate_chart(result)

        html_content = template.render(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            chart_script=chart,
            channel=self.run_times,
        )
        self.stream.write(html_content.encode('utf8'))

    def _generate_heading(self, report_attrs):
        heading = env.get_template('heading.html').render(
            title=self.title,
            parameters=report_attrs,
            description=self.description,
        )

        return heading

    def _generate_report(self, result):
        rows = []
        sorted_result = self.sort_result(result.result)
        for cid, (cls, cls_results) in enumerate(sorted_result):
            # subtotal for a class
            np = nf = ne = ns = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                elif n == 2:
                    ne += 1
                else:
                    ns += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ or ""
            # desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                name=name,
                desc=doc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s.%s' % (self.run_times, cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = env.get_template('report.html').render(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            skip=str(result.skip_count),
            total=str(result.success_count + result.failure_count + result.error_count),
            channel=str(self.run_times),
        )
        return report

    def _generate_chart(self, result):
        chart = env.get_template('charts_script.html').render(
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            skip=str(result.skip_count),
        )
        return chart

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1','et1.1', 'st1.1' etc
        has_output = bool(o or e)
        if n == 0:
            tmp = "p"
        elif n == 1:
            tmp = "f"
        elif n == 2:
            tmp = "e"
        else:
            tmp = "s"
        tid = tmp + 't%d.%d.%d' % (self.run_times, cid + 1, tid + 1)
        # tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        # desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            ue = e
        else:
            ue = e
        script = """%(id)s: %(output)s""" % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )
        # add image
        if getattr(t, 'images', []):
            tmp = ""
            for i, img in enumerate(t.images):
                if i == 0:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: block;" class="img"/>\n""".format(img)
                else:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: none;" class="img"/>\n""".format(img)
            screenshots_html = self.IMG_TMPL.format(images=tmp)
        else:
            screenshots_html = """"""

        # add runtime
        if getattr(t, 'runtime', []):
            runtime = t.runtime
        else:
            runtime = "0.00"

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
            casename=name,
            desc=doc,
            runtime=runtime,
            script=script,
            status=self.STATUS[n],
            img=screenshots_html
        )
        rows.append(row)
        if not has_output:
            return


class SMTP(object):
    """
    Mail function based on SMTP protocol
    """

    def __init__(self, user, password, host, port=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = str(port) if port is not None else "465"

    def sender(self, to=None, subject=None, contents=None, attachments=None):
        if to is None:
            raise ValueError("Please specify the email address to send")

        if subject is None:
            subject = 'Unit Test Report'
        if contents is None:
            contents = env.get_template('mail.html').render(
                mail_pass=str(RunResult.passed),
                mail_fail=str(RunResult.failed),
                mail_error=str(RunResult.errors),
                mail_skip=str(RunResult.skipped)
            )

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.user
        msg['To'] = to

        text = MIMEText(contents, 'html', 'utf-8')
        msg.attach(text)

        if attachments is not None:
            att_name = "report.html"
            if "\\" in attachments:
                att_name = attachments.split("\\")[-1]
            if "/" in attachments:
                att_name = attachments.split("/")[-1]

            att = MIMEApplication(open(attachments, 'rb').read())
            att['Content-Type'] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="{}"'.format(att_name)
            msg.attach(att)

        smtp = smtplib.SMTP_SSL(self.host, self.port)
        try:
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, to, msg.as_string())
            log.info(" 📧 Email sent successfully!!")
        except BaseException as msg:
            log.error('❌ Email failed to send!!' + msg.__str__())
        finally:
            smtp.quit()
