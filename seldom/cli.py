"""
seldom CLI
"""
import os
import sys
import ssl
import json
import click
import seldom
from seldom import Seldom
from seldom import SeldomTestLoader
from seldom import TestMainExtend
from seldom.logging import log, log_cfg
from seldom.utils import file
from seldom.utils import cache
from seldom.har2case.core import HarParser
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seldom.utils.webdriver_manager_extend import ChromeDriverManager
from seldom.running.loader_hook import loader
from seldom import __version__

PY3 = sys.version_info[0] == 3

ssl._create_default_https_context = ssl._create_unverified_context


@click.command()
@click.version_option(version=__version__, help="Show version.")
@click.option("-P", "--project", help="Create an Seldom automation test project.")
@click.option('-cc', "--clear-cache", default=False, help="Clear all caches of seldom.")
@click.option("-p", "--path", help="Run test case file path.")
@click.option("-c/-nc", "--collect/--no-collect", default=False, help="Collect project test cases. Need the `--path`.")
@click.option("-l", "--level", default="data",
              type=click.Choice(['data', 'method']),
              help="Parse the level of use cases. Need the --path.")
@click.option("-j", "--case-json", default=None, help="Test case files. Need the `--path`.")
@click.option("-e", "--env", default=None, help="Set the Seldom run environment `Seldom.env`.")
@click.option("-b", "--browser", default=None,
              type=click.Choice(['chrome', 'firefox', 'ie', 'edge', 'safari']),
              help="The browser that runs the Web UI automation tests. Need the `--path`.")
@click.option("-u", "--base-url", default=None,
              help="The base-url that runs the HTTP automation tests. Need the `--path`.")
@click.option("-d/-nd", "--debug/--no-debug", default=False, help="Debug mode. Need the `--path`.")
@click.option("-rr", "--rerun", default=0, type=int,
              help="The number of times a use case failed to run again. Need the `--path`.")
@click.option("-r", "--report", default=None, help="Set the test report for output. Need the `--path`.")
@click.option("-m", "--mod", help="Run tests modules, classes or even individual test methods from the command line.")
@click.option("-i", "--install",
              type=click.Choice(['chrome', 'firefox', 'ie', 'edge']),
              help="Install the browser driver.")
@click.option("-ll", "--log-level",
              type=click.Choice(['TRACE', 'DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR']),
              help="Set the log level.")
@click.option("-h2c", "--har2case", help="HAR file converts an interface test case.")
def main(project, clear_cache, path, collect, level, case_json, env, debug, browser, base_url, rerun, report, mod,
         install, log_level, har2case):
    """
    seldom CLI.
    """

    if project:
        create_scaffold(project)
        return 0

    if clear_cache:
        cache.clear()

    if log_level:
        log_cfg.set_level(level=log_level)

    # check hook function(confrun.py)
    browser = loader("browser") if loader("browser") is not None else browser
    base_url = loader("base_url") if loader("base_url") is not None else base_url
    debug = loader("debug") if loader("debug") is not None else debug
    rerun = loader("rerun") if loader("rerun") is not None else rerun
    report = loader("report") if loader("report") is not None else report
    timeout = loader("timeout") if loader("timeout") is not None else 10
    app_server = loader("app_server") if loader("app_server") is not None else None
    app_info = loader("app_info") if loader("app_info") is not None else None
    title = loader("title") if loader("title") is not None else "Seldom Test Report"
    tester = loader("tester") if loader("tester") is not None else "Anonymous"
    description = loader("description") if loader("description") is not None else "Test case execution"
    language = loader("language") if loader("language") is not None else "en"
    whitelist = loader("whitelist") if loader("whitelist") is not None else []
    blacklist = loader("blacklist") if loader("blacklist") is not None else []

    if path:
        Seldom.env = env
        if collect is True and case_json is not None:
            click.echo(f"Collect use cases for the {path} directory.")

            if os.path.isdir(path) is True:
                click.echo(f"add env Path: {os.path.dirname(path)}.")
                file.add_to_path(os.path.dirname(path))

            SeldomTestLoader.collectCaseInfo = True
            loader("start_run")
            main_extend = TestMainExtend(path=path)
            case_info = main_extend.collect_cases(json=True, level=level, warning=True)
            case_path = os.path.join(os.getcwd(), case_json)

            with open(case_path, "w", encoding="utf-8") as json_file:
                json_file.write(case_info)
            click.echo(f"save them to {case_path}")
            return 0

        if collect is False and case_json is not None:
            click.echo(f"Read the {case_json} case file to the {path} directory for execution")

            if os.path.exists(case_json) is False:
                click.echo(f"The run case file {case_json} does not exist.")
                return 0

            if os.path.isdir(path) is False:
                click.echo(f"The run cae path {case_json} does not exist.")
                return 0

            click.echo(f"add env Path: {os.path.dirname(path)}.")
            file.add_to_path(os.path.dirname(path))

            loader("start_run")
            with open(case_json, encoding="utf-8") as json_file:
                case = json.load(json_file)
                path, case = reset_case(path, case)
                main_extend = TestMainExtend(
                    path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
                    app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
                    description=description, rerun=rerun, language=language,
                    whitelist=whitelist, blacklist=blacklist)
                main_extend.run_cases(case)
            loader("end_run")
            return 0

        loader("start_run")
        seldom.main(
            path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
            app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language,
            whitelist=whitelist, blacklist=blacklist)
        loader("end_run")
        return 0

    if mod:
        file_dir = os.getcwd()
        sys.path.insert(0, file_dir)
        loader("start_run")
        seldom.main(
            case=mod, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
            app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language,
            whitelist=whitelist, blacklist=blacklist)
        loader("end_run")
        return 0

    if install:
        install_driver(install)
        return 0

    if har2case:
        har_parser = HarParser(har2case)
        har_parser.gen_testcase()
        return 0


def create_scaffold(project_name: str) -> None:
    """
    create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        log.info(f"Folder {project_name} exists, please specify a new folder name.")
        return

    log.info(f"Start to create new test project: {project_name}")
    log.info(f"CWD: {os.getcwd()}\n")

    def create_folder(path):
        os.makedirs(path)
        log.info(f"created folder: {path}")

    def create_file(path, file_content=""):
        with open(path, 'w', encoding="utf-8") as py_file:
            py_file.write(file_content)
        msg = f"created file: {path}"
        log.info(msg)

    test_data = '''{
 "bing":  [
    ["case1", "seldom"],
    ["case2", "poium"],
    ["case3", "XTestRunner"]
 ]
}

'''
    test_web_sample = '''import seldom
from seldom import file_data


class SampleTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("http://www.itest.info")
        self.assertInUrl("itest.info")


class DDTTest(seldom.TestCase):

    @file_data(file="data.json", key="bing")
    def test_data_driver(self, _, keyword):
        """ data driver case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=keyword, enter=True)
        self.assertInTitle(keyword)


if __name__ == '__main__':
    seldom.main(debug=True)

'''
    test_api_sample = '''import seldom


class TestRequest(seldom.TestCase):
    """api test case"""

    def test_put_method(self):
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get('/get', params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete('/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org")

    '''

    run_test = '''"""
seldom confrun.py hooks function
"""


def browser():
    """
    web UI test:
    browser: gc(google chrome)/ff(firefox)/edge/ie/safari
    """
    return "gc"


def base_url():
    """
    http test
    api base url
    """
    return "http://httpbin.org"


def debug():
    """
    debug mod
    """
    return False


def rerun():
    """
    error/failure rerun times
    """
    return 0


def report():
    """
    setting report path
    Used:
    return "d://mypro/result.html"
    return "d://mypro/result.xml"
    """
    return None


def timeout():
    """
    setting timeout
    """
    return 10


def title():
    """
    setting report title
    """
    return "seldom test report"


def tester():
    """
    setting report tester
    """
    return "bugmaster"


def description():
    """
    setting report description
    """
    return ["windows", "jenkins"]


def language():
    """
    setting report language
    return "en"
    return "zh-CN"
    """
    return "en"


def whitelist():
    """test label white list"""
    return []


def blacklist():
    """test label black list"""
    return []
'''
    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_folder(os.path.join(project_name, "test_data"))
    create_file(os.path.join(project_name, "test_data", "data.json"), test_data)
    create_file(os.path.join(project_name, "test_dir", "__init__.py"))
    create_file(os.path.join(project_name, "test_dir", "test_web_sample.py"), test_web_sample)
    create_file(os.path.join(project_name, "test_dir", "test_api_sample.py"), test_api_sample)
    create_file(os.path.join(project_name, "confrun.py"), run_test)


def install_driver(browser: str) -> None:
    """
    Download and install the browser driver

    :param browser: The Driver to download. Pass as `chrome/firefox/ie/edge`. Default Chrome.
    :return:
    """

    if browser == "chrome":
        driver_path = ChromeDriverManager().install()
        log.info(f"Chrome Driver[==>] {driver_path}")
    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
        log.info(f"Firefox Driver[==>] {driver_path}")
    elif browser == "ie":
        driver_path = IEDriverManager().install()
        log.info(f"IE Driver[==>] {driver_path}")
    elif browser == "edge":
        driver_path = EdgeChromiumDriverManager().install()
        log.info(f"Edge Driver[==>] {driver_path}")
    else:
        raise NameError(f"Not found '{browser}' browser driver.")


def reset_case(path: str, cases: list) -> [str, list]:
    """
    Reset the use case data
    :param path: case base path
    :param cases: case data
    """
    if len(cases) == 0:
        return path, cases

    for case in cases:
        if "." not in case["file"]:
            return path, cases

    case_start = cases[0]["file"].split(".")[0]
    for case in cases:
        if case["file"].startswith(f"{case_start}.") is False:
            break
    else:
        path = os.path.join(path, case_start)
        for case in cases:
            case["file"] = case["file"][len(case_start)+1:]
        return path, cases

    return path, cases


if __name__ == '__main__':
    main()
