from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def browser(name=None, driver_path=None, grid_url=None):
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "internet explorer" or "ie".
    :param name: Browser name
    :param driver_path: Browser driver path
    :param grid_url: Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object.
    :return:
    """
    if name is None:
        name = "chrome"

    if name == "firefox" or name == "ff":
        if driver_path is not None:
            return webdriver.Firefox(executable_path=driver_path)
        if grid_url is not None:
            webdriver.Remote(command_executor=grid_url,
                             desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        return webdriver.Firefox()
    elif name == "chrome":
        if driver_path is not None:
            return webdriver.Chrome(executable_path=driver_path)
        if grid_url is not None:
            webdriver.Remote(command_executor=grid_url,
                             desired_capabilities=DesiredCapabilities.CHROME.copy())
        return webdriver.Chrome()
    elif name == "internet explorer" or name == "ie":
        return webdriver.Ie()
    elif name == "opera":
        return webdriver.Opera()
    elif name == "chrome_headless":
        chrome_options = CH_Options()
        chrome_options.add_argument('--headless')
        if driver_path is not None:
            return webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
        return webdriver.Chrome(chrome_options=chrome_options)
    elif name == "firefox_headless":
        firefox_options = FF_Options()
        firefox_options.headless = True
        if driver_path is not None:
            return webdriver.Firefox(firefox_options=firefox_options, executable_path=driver_path)
        return webdriver.Firefox(firefox_options=firefox_options)
    elif name == 'edge':
        return webdriver.Edge()
    elif name == 'safari':
        return webdriver.Safari()
    else:
        raise NameError(
                "Not found {} browser, You can enter 'ie', 'ff', 'opera', 'edge', 'chrome'.".format(name))
