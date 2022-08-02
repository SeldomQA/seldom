import os
import sys
import ssl
import argparse
from seldom.logging import log
from seldom.har2case.core import HarParser
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seldom.utils.webdriver_manager_extend import ChromeDriverManager


from seldom import __description__, __version__

PY3 = sys.version_info[0] == 3

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    """
    API test: parse command line options and run commands.
    """

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        '-v', '--version', dest='version', action='store_true',
        help="show version")

    parser.add_argument(
        '-project',
        help="Create an Seldom automation test project.")

    parser.add_argument(
        '-h2c',
        help="HAR file converts an interface test case.")

    parser.add_argument(
        '-r',
        help="run test case")

    parser.add_argument(
        '-m',
        help="run tests modules, classes or even individual test methods from the command line ")

    parser.add_argument(
        '-install',
        help="Install the browser driver, For example, 'chrome', 'firefox', 'ie', 'edge', 'opera'. ")

    args = parser.parse_args()

    if args.version:
        print("seldom {}".format(__version__))
        return 0

    project_name = args.project
    if project_name:
        create_scaffold(project_name)
        return 0

    har_file = args.h2c
    if har_file:
        hp = HarParser(har_file)
        hp.gen_testcase()
        return 0

    run_file = args.r
    if run_file:
        print("Runtime environment:")
        print("---------------------")
        if PY3:
            ret = os.system("python3 -V")
            os.system("seldom -v")
            print("---------------------")
            if ret == 0:
                command = "python3 " + run_file
            else:
                command = "python " + run_file
        else:
            raise NameError("Does not support python2")
        os.system(command)
        return 0

    run_case = args.m
    if run_case:
        print("Runtime environment:")
        print("---------------------")
        print("Note: This mode is suitable for debugging single test classes and methods.")
        if PY3:
            ret = os.system("python3 -V")
            os.system("seldom -v")
            print("Browser: Chrome(default)")
            print("---------------------")
            if ret == 0:
                command = "python3 -m unittest " + run_case
            else:
                command = "python -m unittest " + run_case
        else:
            raise NameError("Does not support python2")
        os.system(command)
        return 0

    driver_name = args.install
    if driver_name:
        install_driver(driver_name)
        return 0


def create_scaffold(project_name):
    """
    create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        log.info(u"Folder {} exists, please specify a new folder name.".format(project_name))
        return

    log.info("Start to create new test project: {}".format(project_name))
    log.info("CWD: {}\n".format(os.getcwd()))

    def create_folder(path):
        os.makedirs(path)
        msg = "created folder: {}".format(path)
        log.info(msg)

    def create_file(path, file_content=""):
        with open(path, 'w') as f:
            f.write(file_content)
        msg = "created file: {}".format(path)
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
    
    def start(self):
        self.base_url = "http://httpbin.org"
    
    def test_put_method(self):
        self.put(f'{self.base_url}/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post(f'{self.base_url}/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get(f'{self.base_url}/get', params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete(f'{self.base_url}/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main()

    '''

    run_test = """import seldom


if __name__ == '__main__':
    # run test file
    # seldom.main("./test_dir/test_web_sample.py")
    # run test dir
    seldom.main("./test_dir/")

"""
    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_folder(os.path.join(project_name, "test_data"))
    create_file(os.path.join(project_name, "test_data", "data.json"), test_data)
    create_file(os.path.join(project_name, "test_dir", "test_web_sample.py"), test_web_sample)
    create_file(os.path.join(project_name, "test_dir", "test_api_sample.py"), test_api_sample)
    create_file(os.path.join(project_name, "run.py"), run_test)


def install_driver(browser=None):
    """
    Download and install the browser driver

    :param browser: The Driver to download. Pass as `chrome/firefox/ie/edge/opera`. Default Chrome.
    :return:
    """

    if browser is None:
        browser = "chrome"

    if browser == "chrome":
        ChromeDriverManager().install()
    elif browser == "firefox":
        GeckoDriverManager().install()
    elif browser == "ie":
        IEDriverManager().install()
    elif browser == "edge":
        EdgeChromiumDriverManager().install()
    else:
        raise NameError(f"Not found '{browser}' browser driver.")
