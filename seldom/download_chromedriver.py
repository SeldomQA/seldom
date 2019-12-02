import re
import ssl
import zipfile
import tarfile
import shutil
import platform
import os
from os import makedirs
from os.path import join, isfile, basename
from os.path import isdir, dirname, abspath
from urllib.request import urlopen


versions = sorted(['32', '64'], key=lambda v: not platform.machine().endswith(v))
os_opts = [('win', 'win', '.exe'), ('darwin', 'mac', ''), ('linux', 'linux', '')]

current_os = None
ext = ''
for o in os_opts:
    if o[0] in platform.system().lower():
        current_os = o[1]
        ext = o[2]

ssl._create_default_https_context = ssl._create_unverified_context


def chrome(version='latest', _os=None, os_bit=None):
    """
    chrome driver info
    :param version:
    :param _os:
    :param os_bit:
    :return:
    """
    _base_version = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    _base_download = 'https://chromedriver.storage.googleapis.com/%s/chromedriver_%s%s.zip'

    if version == 'latest':
        version = raw(_base_version)
        print("vvv", version)
    if not version:
        raise Exception("Unable to locate latest ChromeDriver version!")
    download = _base_download % (version, _os, os_bit)
    return 'chromedriver', download, version


def raw(url):
    try:
        resp = urlopen(url, timeout=15)
    except Exception:
        return False
    c_type = resp.headers.get_content_charset()
    c_type = c_type if c_type else 'utf-8'
    html = resp.read().decode(c_type, errors='ignore')
    return html


def install(browser=None, file_directory='./lib/', chmod=True, version='latest'):
    """
    Downloads the given browser driver, and returns the path it was saved to.

    :param browser: The Driver to download. Pass as `pyderman.chrome/firefox`. Default Chrome.
    :param file_directory: The directory to save the driver.
    :param chmod: If True, attempt to make the downloaded driver executable.
    :param version: The version to download. Default 'latest'.
    :return: The absolute path of the downloaded driver, or None if something failed.
    """
    if not current_os:
        raise Exception('Cannot determine OS version! [%s]' % platform.system())
    if not version:
        version = 'latest'
    if browser is None:
        browser = "chrome"

    for os_bit in versions:
        if browser == "chrome":
            data = chrome(version=version, _os=current_os, os_bit=os_bit)
        else:
            data = chrome(version=version, _os=current_os, os_bit=os_bit)
        driver_path, url, ver = data
        driver = basename(driver_path)
        exts = [e for e in ['.zip', '.tar.gz', '.tar.bz2'] if url.endswith(e)]
        if len(exts) != 1:
            raise Exception("Unable to locate file extension in URL: %s (%s)" % (url, ','.join(exts)))
        archive = exts[0]

        archive_path = join(abspath(file_directory), '%s_%s%s' % (driver, current_os, archive))
        file_path = join(abspath(file_directory), '%s%s' % (driver, ext))

        if isfile(file_path):
            print('%s is already installed.' % driver)
            return file_path

        if not _download(url, archive_path):
            print('Download for %s version failed; Trying alternates.' % os_bit)
            continue

        out = _extract(archive_path, driver_path, file_path)
        if out and chmod:
            mode = os.stat(out).st_mode
            mode |= (mode & 0o444) >> 2  # copy R bits to X
            os.chmod(out, mode)

        return out
    raise Exception('Unable to locate a valid Web Driver.')


def _download(url, path):
    print('\tDownloading from: ', url)
    print('\tTo: ', path)
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


def _extract(path, driver_pattern, out_file):
    """
    Extracts zip files, or tar.gz files.
    :param path: Path to the archive file, absolute.
    :param driver_pattern:
    :param out_file:
    :return:
    """
    print("path", path)
    print("driver_pattern", driver_pattern)
    print("out_file", out_file)
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


if __name__ == "__main__":
    install(browser="chrome")
