"""
seldom CLI
"""
import json
import os
import sys
from pathlib import Path

import typer

# Import only the absolute minimum at module level
app = typer.Typer(help="seldom CLI.")

# Current file and directory
current_file = Path(__file__).resolve()
current_dir = current_file.parent


# Functions for lazy importing common modules
def _import_seldom_core():
    """Lazy import of seldom core modules"""
    import ssl
    # Set ssl context
    ssl._create_default_https_context = ssl._create_unverified_context

    import seldom
    from seldom.running.config import Seldom
    from seldom import SeldomTestLoader, TestMainExtend
    from seldom.logging import log, log_cfg
    from seldom.utils import file, cache
    from seldom.running.loader_hook import loader

    return {
        'seldom': seldom,
        'Seldom': Seldom,
        'SeldomTestLoader': SeldomTestLoader,
        'TestMainExtend': TestMainExtend,
        'log': log,
        'log_cfg': log_cfg,
        'file': file,
        'cache': cache,
        'loader': loader
    }


def _import_har_parser():
    """Lazy import of HarParser"""
    from seldom.har2case.core import HarParser
    return HarParser


def _import_swagger_parser():
    """Lazy import of SwaggerParser"""
    from seldom.swagger2case.core import SwaggerParser
    return SwaggerParser


def _import_file_running_config():
    """Lazy import of FileRunningConfig"""
    from seldom.running.config import FileRunningConfig
    return FileRunningConfig


@app.command()
def main(
        version: bool = typer.Option(None, "-v", "--version", help="Show version."),
        project_api: str = typer.Option(None, "-api", "--project-api", help="Create a project of API type."),
        project_app: str = typer.Option(None, "-app", "--project-app", help="Create a project of App type"),
        project_web: str = typer.Option(None, "-web", "--project-web", help="Create a project of Web type"),
        clear_cache: bool = typer.Option(False, "-cc", "--clear-cache", help="Clear all caches of seldom."),
        log_level: str = typer.Option(None, "-ll", "--log-level",
                                      help="Set the log level [TRACE |DEBUG | INFO | SUCCESS | WARNING | ERROR].",
                                      case_sensitive=False, show_choices=True),
        mod: str = typer.Option(None, "-m", "--mod",
                                help="Run tests modules, classes or even individual test methods from the command line."),
        path: str = typer.Option(None, "-p", "--path", help="Run test case file path."),
        env: str = typer.Option(None, "-e", "--env", help="Set the Seldom run environment `Seldom.env`."),
        browser: str = typer.Option(None, "-b", "--browser",
                                    help="The browser that runs the Web UI automation tests [chrome | edge | firefox | chromium]. Need the --path."),
        base_url: str = typer.Option(None, "-u", "--base-url",
                                     help="The base-url that runs the HTTP automation tests. Need the --path."),
        debug: bool = typer.Option(False, "-d", "--debug", help="Debug mode. Need the --path/--mod."),
        rerun: int = typer.Option(0, "-rr", "--rerun",
                                  help="The number of times a use case failed to run again. Need the --path."),
        report: str = typer.Option(None, "-r", "--report", help="Set the test report for output. Need the --path."),
        collect: bool = typer.Option(False, "-c", "--collect", help="Collect project test cases. Need the --path."),
        level: str = typer.Option("data", "-l", "--level",
                                  help="Parse the level of use cases [data | case]. Need the --path."),
        case_json: str = typer.Option(None, "-j", "--case-json", help="Test case files. Need the --path."),
        har2case: str = typer.Option(None, "-h2c", "--har2case", help="HAR file converts an seldom test case."),
        swagger2case: str = typer.Option(None, "-s2c", "--swagger2case",
                                         help="Swagger file converts an seldom test case."),
        api_excel: str = typer.Option(None, help="Run the api test cases in the excel file."),
):
    """
    seldom CLI.
    """
    # For simple commands (like --help and --version), return directly without importing any modules
    if version:
        from seldom import __version__
        typer.echo(f"seldom version: {__version__}")
        return typer.Exit()

    # Check if this is a --help call or no arguments provided (will trigger help)
    if len(sys.argv) <= 2 or (len(sys.argv) == 3 and (sys.argv[2] in ['--help', '-h'])):
        # Return 0 to let Typer display help message without importing anything
        return 0

    # Import modules only when core functionality commands are needed
    core_commands = [project_api, project_app, project_web, clear_cache, log_level, path, mod, har2case, swagger2case,
                     api_excel]
    if any(core_commands):
        # Import core modules
        core = _import_seldom_core()
        log = core['log']
        log_cfg = core['log_cfg']
        cache = core['cache']
        file = core['file']
        loader = core['loader']
        seldom = core['seldom']
        Seldom = core['Seldom']
        SeldomTestLoader = core['SeldomTestLoader']
        TestMainExtend = core['TestMainExtend']
    else:
        # If no commands are specified, Typer will automatically display help information
        return 0

    if project_api:
        create_scaffold(project_api, "api", log)
        return 0
    if project_app:
        create_scaffold(project_app, "app", log)
        return 0
    if project_web:
        create_scaffold(project_web, "web", log)
        return 0

    if clear_cache:
        cache.clear()

    if log_level:
        allowed_levels = ["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR"]
        if log_level.upper() not in allowed_levels:
            typer.echo(f"Invalid log level: {log_level}. Choose from {allowed_levels}")
            raise typer.Exit(code=1)
        log_cfg.set_level(level=log_level.upper())

    # check hook function(confrun.py)
    if browser is None:
        browser = loader("browser") if loader("browser") is not None else browser
    if base_url is None:
        base_url = loader("base_url") if loader("base_url") is not None else base_url
    if debug is False:
        debug = loader("debug") if loader("debug") is not None else debug
    if rerun is None:
        rerun = loader("rerun") if loader("rerun") is not None else rerun
    if report is None:
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
            typer.echo(f"Collect use cases for the {path} directory.")

            if os.path.isdir(path) is True:
                typer.echo(f"Add Env Path: {os.path.dirname(path)}.")
                file.add_to_path(os.path.dirname(path))

            SeldomTestLoader.collectCaseInfo = True
            loader("start_run")
            main_extend = TestMainExtend(path=path)
            case_info = main_extend.collect_cases(json=True, level=level, warning=True)
            case_path = os.path.join(os.getcwd(), case_json)

            with open(case_path, "w", encoding="utf-8") as json_file:
                json_file.write(case_info)
            typer.echo(f"Save them to {case_path}")
            return 0

        if collect is False and case_json is not None:
            typer.echo(f"Read the {case_json} case file for execution in the {path} directory")

            if os.path.exists(case_json) is False:
                typer.echo(f"The run case file {case_json} does not exist.")
                return 0

            if os.path.isdir(path) is False:
                typer.echo(f"The run case path {path} does not exist.")
                return 0

            typer.echo(f"Add Env Path: {os.path.dirname(path)}.")
            file.add_to_path(os.path.dirname(path))

            # loader("start_run")
            with open(case_json, encoding="utf-8") as json_file:
                case = json.load(json_file)
                path, case = reset_case(path, case)
                main_extend = TestMainExtend(
                    path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
                    app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
                    description=description, rerun=rerun, language=language,
                    whitelist=whitelist, blacklist=blacklist, extensions=extensions)
                main_extend.run_cases(case)
            # loader("end_run")
            return 0

        # loader("start_run")
        seldom.main(
            path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
            app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language,
            whitelist=whitelist, blacklist=blacklist, extensions=extensions, failfast=failfast)
        # loader("end_run")
        return 0

    if mod:
        file_dir = os.getcwd()
        sys.path.insert(0, file_dir)
        # loader("start_run")
        seldom.main(
            case=mod, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
            app_server=app_server, app_info=app_info, report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language,
            whitelist=whitelist, blacklist=blacklist, extensions=extensions, failfast=failfast)
        # loader("end_run")
        return 0

    if har2case:
        HarParser = _import_har_parser()
        har_parser = HarParser(har2case)
        har_parser.gen_testcase()
        return 0

    if swagger2case:
        SwaggerParser = _import_swagger_parser()
        sp = SwaggerParser(swagger=swagger2case)
        sp.gen_testcase()
        return 0

    if api_excel:
        typer.echo(f"Run {api_excel} file.")
        if Path(api_excel).exists() is False:
            raise FileNotFoundError(f"{api_excel} file does not exist")

        FileRunningConfig = _import_file_running_config()
        FileRunningConfig.api_excel_file_name = api_excel
        script_path = file.join(file.dir, "file_runner", "api_excel.py")
        # loader("start_run")
        seldom.main(
            path=script_path, base_url=base_url, debug=debug, timeout=timeout,
            report=report, title=title, tester=tester,
            description=description, rerun=rerun, language=language, failfast=failfast)
        # loader("end_run")
        return 0

    return 0


def create_scaffold(project_name: str, project_type: str, log) -> None:
    """
    create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        log.info(f"Folder {project_name} exists, please specify a new folder name.")
        return

    log.info(f"Start to create new test project: {project_name}")
    log.info(f"CWD: {os.getcwd()}\n")

    def create_folder(path):
        """Create folder"""
        os.makedirs(path)
        log.info(f"📁 Created folder: {path}")

    def create_file(path, file_content=""):
        """Create file"""
        with open(path, 'w', encoding="utf-8") as py_file:
            py_file.write(file_content)
        log.info(f"📄 Created file: {path}")

    data_path = current_dir / "project_temp" / "data.json"
    confrun_path = current_dir / "project_temp" / project_type / "confrun.py"
    run_path = current_dir / "project_temp" / project_type / "run.py"
    sample_path = current_dir / "project_temp" / project_type / "test_sample.py"

    test_data = data_path.read_text(encoding='utf-8')
    confrun_test = confrun_path.read_text(encoding='utf-8')
    run_test = run_path.read_text(encoding='utf-8')
    test_web_sample = sample_path.read_text(encoding='utf-8')

    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_folder(os.path.join(project_name, "test_data"))
    create_file(os.path.join(project_name, "test_data", "data.json"), test_data)
    create_file(os.path.join(project_name, "test_dir", "__init__.py"))
    create_file(os.path.join(project_name, "test_dir", "test_sample.py"), test_web_sample)
    create_file(os.path.join(project_name, "confrun.py"), confrun_test)
    create_file(os.path.join(project_name, "run.py"), run_test)
    log.info(f"🎉 Project '{project_name}' created successfully.")
    log.info(f"👉 Go to the project folder and run 'python run.py' to start testing.")


def reset_case(path: str, cases: list) -> tuple[str, list]:
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


if __name__ == "__main__":
    app()
