"""
seldom CLI
"""
import os
import sys
import ssl
import json
import click
from pathlib import Path
import seldom
from seldom import Seldom
from seldom import SeldomTestLoader
from seldom import TestMainExtend
from seldom.logging import log, log_cfg
from seldom.utils import file
from seldom.utils import cache
from seldom.har2case.core import HarParser
from seldom.swagger2case.core import SwaggerParser
from seldom.running.loader_hook import loader
from seldom.running.config import FileRunningConfig
from seldom import __version__

PY3 = sys.version_info[0] == 3

ssl._create_default_https_context = ssl._create_unverified_context

# Current file and directory
current_file = Path(__file__).resolve()
current_dir = current_file.parent


@click.command()
@click.version_option(version=__version__, help="Show version.")
@click.option("--project-api", help="Create an API automation test project.")
@click.option("--project-app", help="Create an App automation test project.")
@click.option("--project-web", help="Create an Web automation test project.")
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
@click.option("-ll", "--log-level",
              type=click.Choice(['TRACE', 'DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR']),
              help="Set the log level.")
@click.option("-h2c", "--har2case", help="HAR file converts an seldom test case.")
@click.option("-s2c", "--swagger2case", help="Swagger file converts an seldom test case.")
@click.option("--api-excel", help="Run the api test cases in the excel file.")
def main(project_api, project_app, project_web, clear_cache, path, collect, level, case_json, env, debug, browser,
         base_url, rerun, report, mod, log_level, har2case, swagger2case, api_excel):
    """
    seldom CLI.
    """

    if project_api:
        create_scaffold(project_api, "api")
        return 0
    if project_app:
        create_scaffold(project_app, "app")
        return 0
    if project_web:
        create_scaffold(project_web, "web")
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
    extensions = loader("extensions") if loader("extensions") is not None else None
    failfast = loader("failfast") if loader("failfast") is not None else False

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
                    whitelist=whitelist, blacklist=blacklist, extensions=extensions)
                main_extend.run_cases(case)
            loader("end_run")
            return 0

        loader("start_run")
        seldom.main(
            path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
            app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language,
            whitelist=whitelist, blacklist=blacklist, extensions=extensions, failfast=failfast)
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
            whitelist=whitelist, blacklist=blacklist, extensions=extensions, failfast=failfast)
        loader("end_run")
        return 0

    if har2case:
        har_parser = HarParser(har2case)
        har_parser.gen_testcase()
        return 0

    if swagger2case:
        sp = SwaggerParser(swagger=swagger2case)
        sp.gen_testcase()
        return 0

    if api_excel:
        click.echo(f"run {api_excel} file.")
        if Path(api_excel).exists() is False:
            raise FileNotFoundError(f"{api_excel} file does not exist")

        FileRunningConfig.api_excel_file_name = api_excel
        script_path = file.join(file.dir, "file_runner", "api_excel.py")
        loader("start_run")
        seldom.main(
            path=script_path, base_url=base_url, debug=debug, timeout=timeout,
            report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language, failfast=failfast)
        loader("end_run")
        return 0


def create_scaffold(project_name: str, project_type: str) -> None:
    """
    create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        log.info(f"Folder {project_name} exists, please specify a new folder name.")
        return

    log.info(f"Start to create new test project: {project_name}")
    log.info(f"CWD: {os.getcwd()}\n")

    def create_folder(path):
        """create folder"""
        os.makedirs(path)
        log.info(f"created folder: {path}")

    def create_file(path, file_content=""):
        """create file"""
        with open(path, 'w', encoding="utf-8") as py_file:
            py_file.write(file_content)
        msg = f"created file: {path}"
        log.info(msg)

    data_path = current_dir / "project_temp" / "data.json"

    confrun_path = current_dir / "project_temp" / "confrun_web.py"
    sample_path = current_dir / "project_temp" / "test_web_sample.py"
    if project_type == "api":
        confrun_path = current_dir / "project_temp" / "confrun_api.py"
        sample_path = current_dir / "project_temp" / "test_api_sample.py"
    elif project_type == "app":
        confrun_path = current_dir / "project_temp" / "confrun_app.py"
        sample_path = current_dir / "project_temp" / "test_app_sample.py"

    test_data = data_path.read_text(encoding='utf-8')
    run_test = confrun_path.read_text(encoding='utf-8')
    test_web_sample = sample_path.read_text(encoding='utf-8')

    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_folder(os.path.join(project_name, "test_data"))
    create_file(os.path.join(project_name, "test_data", "data.json"), test_data)
    create_file(os.path.join(project_name, "test_dir", "__init__.py"))
    create_file(os.path.join(project_name, "test_dir", "test_sample.py"), test_web_sample)
    create_file(os.path.join(project_name, "confrun.py"), run_test)


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
            case["file"] = case["file"][len(case_start) + 1:]
        return path, cases

    return path, cases


if __name__ == '__main__':
    main()
