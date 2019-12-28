import os
import re
import sys
import ssl
import shutil
import zipfile
import tarfile
import argparse
import platform
from os import makedirs
from os.path import join, isfile, basename
from os.path import isdir, dirname, abspath
from urllib.request import urlopen
from .logging import log

from seldom import __description__, __version__

PY3 = sys.version_info[0] == 3

versions = sorted(['32', '64'], key=lambda v: not platform.machine().endswith(v))
os_opts = [('win', 'win', '.exe'), ('darwin', 'mac', ''), ('linux', 'linux', '')]

current_os = None
ext = ''
for o in os_opts:
    if o[0] in platform.system().lower():
        current_os = o[1]
        ext = o[2]

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
        '--project',
        help="Create an Seldom automation test project.")

    parser.add_argument(
        '-r',
        help="run test case")

    parser.add_argument(
        '-install',
        help="Install the browser driver, For example, 'chrome', 'firefox'. ")

    args = parser.parse_args()

    if args.version:
        log.info("version {}".format(__version__))
        return 0

    project_name = args.project
    if project_name:
        create_scaffold(project_name)
        return 0

    run_file = args.r
    if run_file:
        log.info("Run the python version:")
        if PY3:
            ret = os.system("python -V")
            if ret != 0:
                os.system("python3 -V")
                command = "python3 " + run_file
            else:
                command = "python " + run_file
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

    test_sample = '''import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su")
        self.assertInTitle("seldom")


if __name__ == '__main__':
    seldom.main("test_sample.py")

'''
    run_test = """import seldom


if __name__ == '__main__':
    # run test
    # seldom.main("./test_dir/")
    seldom.main("./test_dir/test_sample.py")

"""
    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_file(os.path.join(project_name, "test_dir", "test_sample.py"), test_sample)
    create_file(os.path.join(project_name, "run.py"), run_test)


def firefox(_os=None, os_bit=None):
    """
    chrome driver info
    :param _os: system
    :param os_bit: system bit
    :return:
    """
    base_url = 'https://github.com/mozilla/geckodriver/releases/latest'
    try:
        resp = urlopen(base_url, timeout=15)
    except Exception:
        return False
    c_type = resp.headers.get_content_charset()
    c_type = c_type if c_type else 'utf-8'
    html = resp.read().decode(c_type, errors='ignore')
    if not html:
        raise Exception("Unable to download geckodriver version: latest")

    urls = ['https://github.com%s' % u for u in re.findall(r'\"(.+?/download.+?)\"', html)]
    for u in urls:
        target = '%s%s' % (_os, os_bit) if _os is not 'mac' else 'macos'
        if target in u:
            ver = re.search(r'v(\d{1,2}\.\d{1,2}\.\d{1,2})', u).group(1)
            return 'geckodriver', u, ver


def chrome(_os=None, os_bit=None):
    """
    chrome driver info
    :param _os: system
    :param os_bit: system bit
    :return:
    """
    latest_version = '79.0.3945.36'
    base_download = "https://cdn.npm.taobao.org/dist/chromedriver/%s/chromedriver_%s%s.zip"
    download = base_download % (latest_version, _os, os_bit)
    return 'chromedriver', download, latest_version


def install_driver(browser=None, file_directory='./lib/'):
    """
    Download and install the browser driver

    :param browser: The Driver to download. Pass as `chrome/firefox`. Default Chrome.
    :param file_directory: The directory to save the driver.
    :return: The absolute path of the downloaded driver, or None if something failed.
    """
    if not current_os:
        raise Exception('Cannot determine OS version! [%s]' % platform.system())

    if browser is None:
        browser = "chrome"

    for os_bit in versions:
        if browser == "chrome":
            data = chrome(_os=current_os, os_bit=os_bit)
        elif browser == "firefox":
            data = firefox(_os=current_os, os_bit=os_bit)
        else:
            raise NameError("Currently only 'chrome/firefox' browser drivers are supported")
        driver_path, url, ver = data
        driver = basename(driver_path)
        exts = [e for e in ['.zip', '.tar.gz', '.tar.bz2'] if url.endswith(e)]
        if len(exts) != 1:
            raise Exception("Unable to locate file extension in URL: %s (%s)" % (url, ','.join(exts)))
        archive = exts[0]

        archive_path = join(abspath(file_directory), '%s_%s%s%s' % (driver, current_os, os_bit, archive))
        file_path = join(abspath(file_directory), '%s%s' % (driver, ext))

        if isfile(file_path):
            log.info('{} is already installed.'.format(driver))
            return file_path

        if not download(url, archive_path):
            log.info('Download for {} version failed; Trying alternates.'.format(os_bit))
            continue

        out = extract(archive_path, driver_path, file_path)
        if out:
            mode = os.stat(out).st_mode
            mode |= (mode & 0o444) >> 2  # copy R bits to X
            os.chmod(out, mode)

        return out
    raise Exception('Unable to locate a valid Web Driver.')


def download(url, path):
    """
    download driver file
    :param url:
    :param path:
    :return:
    """
    log.info('\tDownloading from: {}'.format(url))
    log.info('\tTo: {}'.format(path))
    file = abspath(path)
    if not isdir(dirname(file)):
        makedirs(dirname(file), exist_ok=True)
    try:
        req = urlopen(url, timeout=15)
    except Exception:
        return False
    with open(file, 'wb') as fp:
        shutil.copyfileobj(req, fp, 16 * 1024)
    return True


def extract(path, driver_pattern, out_file):
    """
    Extracts zip files, or tar.gz files.
    :param path: Path to the archive file, absolute.
    :param driver_pattern:
    :param out_file:
    :return:
    """
    path = abspath(path)
    out_file = abspath(out_file)
    if not isfile(path):
        return None
    tmp_path = join(dirname(out_file), 'tmp_dl_dir_%s' % basename(path))
    zip_ref, namelist = None, None
    if path.endswith('.zip'):
        zip_ref = zipfile.ZipFile(path, "r")
        namelist = zip_ref.namelist()
    elif path.endswith('.tar.gz'):
        zip_ref = tarfile.open(path, "r:gz")
        namelist = zip_ref.getnames()
    elif path.endswith('.tar.bz2'):
        zip_ref = tarfile.open(path, "r:bz2")
        namelist = zip_ref.getnames()
    if not zip_ref:
        return None
    ret = None
    for n in namelist:
        if re.match(driver_pattern, n):
            zip_ref.extract(n, tmp_path)
            ret = join(tmp_path, n)
    zip_ref.close()
    if ret:
        if isfile(out_file):
            os.remove(out_file)
        os.rename(ret, out_file)
        shutil.rmtree(tmp_path)
        ret = out_file
    os.remove(path)
    return ret
