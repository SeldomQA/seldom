import io
import copy
import sys
import unittest
import datetime
from xml.sax import saxutils
from seldom.running.config import RunResult, Seldom
from seldom.logging.exceptions import TestFixtureRunError

"""
A TestRunner for use with the Python unit testing framework. It
generates a HTML report to show the result at a glance.
The simplest way to use this is to invoke its main method. E.g.
    import unittest
    import HTMLTestRunner
    ... define your tests ...
    if __name__ == '__main__':
        HTMLTestRunner.main()
For more customization options, instantiates a HTMLTestRunner object.
HTMLTestRunner is a counterpart to unittest's TextTestRunner. E.g.
    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
    # run the test
    runner.run(my_test_suite)
------------------------------------------------------------------------
Copyright (c) 2004-2020, Wai Yip Tung
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Wai Yip Tung , bugmaster"
__version__ = "0.9.0"

"""
Change History
Version 0.9.0
* Increased repeat execution
* Added failure screenshots
Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).
Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.
Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat <script> block as CDATA.
Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).
"""

# TODO: color stderr
# TODO: simplify javascript using ,ore than 1 class in the class attribute?


# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

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


# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.
    Overall structure of an HTML report
    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: 'pass',
        1: 'fail',
        2: 'error',
        3: 'skip',
    }

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.slim.min.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="http://apps.bdimg.com/libs/Chart.js/0.2.0/Chart.min.js"></script>
    <link rel="stylesheet" href="http://img.itest.info/seldom.css">

    %(stylesheet)s
</head>
<body>
<script language="javascript" type="text/javascript">
function show_img(obj) {
    var obj1 = obj.nextElementSibling
    obj1.style.display='block'
    var index = 0;//每张图片的下标，
    var len = obj1.getElementsByTagName('img').length;
    var imgyuan = obj1.getElementsByClassName('imgyuan')[0]
    //var start=setInterval(autoPlay,500);
    obj1.onmouseover=function(){//当鼠标光标停在图片上，则停止轮播
        clearInterval(start);
    }
    obj1.onmouseout=function(){//当鼠标光标停在图片上，则开始轮播
        start=setInterval(autoPlay,1000);
    }    
    for (var i = 0; i < len; i++) {
        var font = document.createElement('font')
        imgyuan.appendChild(font)
    }
    var lis = obj1.getElementsByTagName('font');//得到所有圆圈
    changeImg(0)
    var funny = function (i) {
        lis[i].onmouseover = function () {
            index=i
            changeImg(i)
        }
    }
    for (var i = 0; i < lis.length; i++) {
        funny(i);
    }
    
    function autoPlay(){
        if(index>len-1){
            index=0;
            clearInterval(start); //运行一轮后停止
        }
        changeImg(index++);
    }
    imgyuan.style.width= 25*len +"px";
    //对应圆圈和图片同步
    function changeImg(index) {
        var list = obj1.getElementsByTagName('img');
        var list1 = obj1.getElementsByTagName('font');
        for (i = 0; i < list.length; i++) {
            list[i].style.display = 'none';
            list1[i].style.backgroundColor = 'white';
        }
        list[index].style.display = 'block';
        list1[index].style.backgroundColor = 'red';
    }
}
function hide_img(obj){
    obj.parentElement.style.display = "none";
    obj.parentElement.getElementsByClassName('imgyuan')[0].innerHTML = "";
}
output_list = Array();
/* level - 0:Summary; 1:Failed; 2:Skip; 3:All */
function showCase(level, channel) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (["ft","pt","et","st"].indexOf(id.substr(0,2))!=-1){
           if ( level == 0 && id.substr(2,1) == channel ) {
                tr.className = 'hiddenRow';
            }
        }
        if (id.substr(0,3) == 'pt'+ channel) {
            if ( level == 1){
                tr.className = '';
            }
            else if  (level > 4 && id.substr(2,1) == channel ){
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
         }
        if (id.substr(0,3) == 'ft'+channel) {
            if (level == 2) {
                tr.className = '';
            }
            else if  (level > 4 && id.substr(2,1) == channel ){
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
          }
        if (id.substr(0,3) == 'et'+channel) {
            if (level == 3) {
                tr.className = '';
            }
            else if  (level > 4 && id.substr(2,1) == channel ){
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
        if (id.substr(0,3) == 'st'+channel) {
            if (level == 4) {
                tr.className = '';
            }
            else if  (level > 4 && id.substr(2,1) == channel ){
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}
function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        if (!tr) {
            tid = 'e' + tid0;
            tr = document.getElementById(tid);
        }
        if (!tr) {
            tid = 's' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}
function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
</script>
%(heading)s
%(report)s
%(ending)s
%(chart_script)s
</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { overflow: initial; }
/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 20px;
    margin-bottom: 1ex;
    margin-left: 10px;
    margin-right: 10px;
    width: 23%;
    float: left;
    padding-top: 10px;
    padding-left: 10px;
    padding-bottom: 10px;
    padding-right: 10px;
    box-shadow:0px 0px 5px #000;
}
.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}
a.popup_link:hover {
    color: red;
}
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 12pt;
    width: 500px;
}
}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
    margin-left: 10px;
}
#header_row {
    font-weight: bold;
    color: #606060;
    background-color: #f5f5f5;
    border-top-width: 10px;
    border-color: #d6e9c6;
	font-size: 15px;
}
#total_row  { font-weight: bold; background-color: #dee2e6;}
.passClass  { background-color: #d6e9c6; }
.failClass  { background-color: #faebcc; }
.errorClass { background-color: #ebccd1; }
.passCase   { color: #28a745; font-weight: bold;}
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.none {color: #009900 }
.testcase   { margin-left: 2em; }
/* -- ending ---------------------------------------------------------------------- */
#ending {
}
/* -- chars ---------------------------------------------------------------------- */
.testChars {width: 900px;margin-left: 0px;}
.error-color {
    color: #fff;
    background-color: #f44455;
    border-color: #f44455;
}
.pass-color {
    color: #fff;
    background-color: #5fc27e;
    border-color: #5fc27e;
}
.fail-color {
    color: #fff;
    background-color: #fcc100;
    border-color: #fcc100;
}
.skip-color {
    color: #fff;
    background-color: #6c757d;
    border-color: #6c757d;
}
/* -- screenshots ---------------------------------------------------------------------- */
.img{
	height: 100%;
	border-collapse: collapse;
}
.screenshots {
    z-index: 100;
	position:fixed;
	height: 80%;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
	display: none;
	box-shadow:1px 2px 20px #333333;
}
.imgyuan{
    height: 20px;
    border-radius: 12px;
    background-color: red;
    padding-left: 13px;
    margin: 0 auto;
    position: relative;
    top: -40px;
    background-color: rgba(1, 150, 0, 0.3);
}
.imgyuan font{
    border:1px solid white;
    width:11px; 
    height:11px;
    border-radius:50%;
    margin-right: 9px;
    margin-top: 4px;
    display: block;
    float: left;
    background-color: white;
}

</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """
<nav class="navbar navbar-expand navbar-light bg-white">
    <a class="sidebar-toggle d-flex mr-2">
        <i class="hamburger align-self-center"></i>
    </a>
    <h1 style="margin-bottom: 0px;">seldom</h1>
    <div class="navbar-collapse collapse">
        <ul class="navbar-nav ml-auto">
            <h3 style="float: right;">%(title)s</h3>
        </ul>
    </div>
</nav>
<div style="height: 260px; margin-top: 20px;">
<div class="col-12 col-lg-5 col-xl-3 d-flex" style="float:left">
    <div class='card flex-fill'>
        <div class="card-body my-2">
        <table class="table my-0">
            <tbody>
            %(parameters)s
            <tr><td>Description:</td><td class="text-right">%(description)s</td></tr>
            </tbody>
        </table>
        </div>
    </div>
</div>
<div style="float:left; margin-left: 10px; margin-top: 20px;">
    <p> Test Case Pie charts </p>
    <h2 class="d-flex align-items-center mb-0 font-weight-light pass-color">%(pass_count)s</h2>
    <a>PASSED</a><br>
    <h2 class="d-flex align-items-center mb-0 font-weight-light fail-color">%(fail_count)s</h2>
    <a>FAILED</a>
    <h2 class="d-flex align-items-center mb-0 font-weight-light error-color">%(error_count)s</h2>
    <a>ERRORS</a><br>
    <h2 class="d-flex align-items-center mb-0 font-weight-light skip-color">%(skip_count)s</h2>
    <a>SKIPED</a><br>
</div>
<div class="testChars">
    <canvas id="myChart" width="250" height="250"></canvas>
</div>
</div>
"""  # variables: (title, parameters, description)

    # ------------------------------------------------------------------------
    # Pie chart
    #

    ECHARTS_SCRIPT = """
    <script type="text/javascript">
var data = [
	{
		value: %(error)s,
		color: "#f44455",
		label: "Error",
		labelColor: 'white',
		labelFontSize: '16'
	},
	{
		value : %(fail)s,
		color : "#fcc100",
		label: "Fail",
		labelColor: 'white',
		labelFontSize: '16'
	},
	{
		value : %(Pass)s,
		color : "#5fc27e",
		label : "Pass",
		labelColor: 'white',
		labelFontSize: '16'
	},
    {
		value : %(skip)s,
		color : "#6c757d",
		label : "skip",
		labelColor: 'white',
		labelFontSize: '16'
	}
]
var newopts = {
     animationSteps: 100,
 		animationEasing: 'easeInOutQuart',
}
//Get the context of the canvas element we want to select
var ctx = document.getElementById("myChart").getContext("2d");
var myNewChart = new Chart(ctx).Pie(data,newopts);
</script>
	"""

    HEADING_ATTRIBUTE_TMPL = """<tr><td>%(name)s:</td><td class="text-right">%(value)s</td></tr>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """
<p id='show_detail_line' style="margin-left: 10px; margin-top: 30px;">
<a href='javascript:showCase(0, %(channel)s)' class="btn btn-dark btn-sm">Summary</a>
<a href='javascript:showCase(1, %(channel)s)' class="btn btn-success btn-sm">Pass</a>
<a href='javascript:showCase(2, %(channel)s)' class="btn btn-warning btn-sm">Failed</a>
<a href='javascript:showCase(3, %(channel)s)' class="btn btn-danger btn-sm">Error</a>
<a href='javascript:showCase(4, %(channel)s)' class="btn btn-light btn-sm">Skip</a>
<a href='javascript:showCase(5, %(channel)s)' class="btn btn-info btn-sm">All</a>
</p>
<table class="table mb-0">
<thead>
    <tr id='header_row'>
        <td>Test Group/Test case</td>
        <td>Count</td>
        <td>Pass</td>
        <td>Fail</td>
        <td>Error</td>
        <td>View</td>
        <td>Screenshots</td>
    </tr>
</thead>
%(test_list)s
<tr id='total_row'>
    <td>Total</td>
    <td>%(count)s</td>
    <td class="text text-success">%(Pass)s</td>
    <td class="text text-danger">%(fail)s</td>
    <td class="text text-warning">%(error)s</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
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
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
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
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
    <td>%(img)s</td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    IMG_TMPL = r"""
<a  onfocus='this.blur();' href="javacript:void(0);" onclick="show_img(this)">show</a>
<div align="center" class="screenshots"  style="display:none">
    <a onclick="hide_img(this)">
    <svg  style="float:right" t="1585994823858" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2765" width="16" height="16"><path d="M512 512m-512 0a512 512 0 1 0 1024 0 512 512 0 1 0-1024 0Z" fill="#F55300" p-id="2766"></path><path d="M258.56 358.912l434.432 434.432a51.2 51.2 0 0 0 72.3968-72.3968L330.9568 286.5152A51.2 51.2 0 1 0 258.56 358.912z" fill="#F9F9F9" p-id="2767"></path><path d="M258.56 712.192l434.432-434.432a51.2 51.2 0 0 1 72.448 72.3968l-434.4832 434.432A51.2 51.2 0 1 1 258.56 712.192z" fill="#F9F9F9" p-id="2768"></path></svg>
    </a>
    {imgs}
    <div class="imgyuan"></div>
</div>
"""
    # ------------------------------------------------------------------------
    # ENDING
    #

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1, rerun=0, save_last_run=False):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.skip_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error; 3: skip),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.rerun = rerun
        self.save_last_run = save_last_run
        self.status = 0
        self.runs = 0
        self.result = []

    def startTest(self, test):
        test.imgs = getattr(test, "imgs", [])
        # TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
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
        try:
            return self.outputBuffer.getvalue()
        except AttributeError:
            raise TestFixtureRunError("test setup/teardown run error.")

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
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
        
        if Seldom.driver is not None:
            try:
                test.imgs.append(Seldom.driver.get_screenshot_as_base64())
            except BaseException as msg:
                pass
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

        if Seldom.driver is not None:
            try:
                test.imgs.append(Seldom.driver.get_screenshot_as_base64())
            except BaseException:
                pass
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


class HTMLTestRunner(Template_mixin):
    """
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
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test, rerun, save_last_run):
        """Run the given test case or test suite."""
        result = _TestResult(self.verbosity, rerun=rerun,
                             save_last_run=save_last_run)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.run_times += 1
        self.generateReport(test, result)
        # print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
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

    def getReportAttributes(self, result):
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
        RunResult.Skiped = result.skip_count

        if result.success_count:
            status.append('Passed:%s' % result.success_count)
        if result.failure_count:
            status.append('Failed:%s' % result.failure_count)
        if result.error_count:
            status.append('Errors:%s' % result.error_count)
        if result.skip_count:
            status.append('Skiped:%s' % result.skip_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        result = {
            "pass": result.success_count,
            "fail": result.failure_count,
            "error": result.error_count,
            "skip": result.skip_count,
        }
        return [
            ('Start Time', startTime),
            ('Duration', duration),
            ('Status', status),
            ('Result', result),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        chart = self._generate_chart(result)
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
            chart_script=chart,
            channel=self.run_times,
        )
        self.stream.write(output.encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            result = {}
            if name == "Result":
                result = value
            else:
                line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),
                    value=saxutils.escape(value),
                )
                a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
            pass_count=saxutils.escape(str(result["pass"])),
            fail_count=saxutils.escape(str(result["fail"])),
            error_count=saxutils.escape(str(result["error"])),
            skip_count=saxutils.escape(str(result["skip"])),
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
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
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s.%s' % (self.run_times, cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count +
                      result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            skip=str(result.skip_count),
            total=str(result.success_count +
                      result.failure_count + result.error_count),
            channel=str(self.run_times),
        )
        return report

    def _generate_chart(self, result):
        chart = self.ECHARTS_SCRIPT % dict(
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
        desc = doc and ('%s: %s' % (name, doc)) or name
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

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )
        if getattr(t, 'imgs', []):
            # 判断截图列表，如果有则追加
            tmp = ""
            for i, img in enumerate(t.imgs):
                if i == 0:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: block;" class="img"/>\n""".format(
                        img)
                else:
                    tmp += """<img src="data:image/jpg;base64,{}" style="display: none;" class="img"/>\n""".format(
                        img)
            screenshots_html = self.IMG_TMPL.format(imgs=tmp)
        else:
            screenshots_html = """"""

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (
                n == 1 and 'failCase' or 'passCase'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
            img=screenshots_html
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
