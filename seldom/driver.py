from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver import Remote
from selenium.webdriver import ChromeOptions


PHONE_LIST = [
    'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8', 'iPhone 8 Plus',
    'iPhone X', 'Pixel 2', 'Pixel XL', "Galaxy S5"
]
PAD_LIST = ['iPad', 'iPad Pro']


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
    # Prevention of detection
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    if name is None:
        name = "chrome"

    if name in ["firefox", "ff"]:
        if driver_path is not None:
            return webdriver.Firefox(executable_path=driver_path)
        if grid_url is not None:
            return webdriver.Remote(command_executor=grid_url,
                                    desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        return webdriver.Firefox()
    elif name in ["chrome", "google chrome", "gc"]:
        if driver_path is not None:
            chromedriver = webdriver.Chrome(executable_path=driver_path, options=option)
            chromedriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })
            return chromedriver
        if grid_url is not None:
            return webdriver.Remote(command_executor=grid_url,
                                    desired_capabilities=DesiredCapabilities.CHROME.copy())
        chromedriver = webdriver.Chrome(options=option)
        chromedriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return chromedriver
    elif name == ["internet explorer", "ie", "IE"]:
        return webdriver.Ie()
    elif name == "opera":
        return webdriver.Opera()
    elif name == "chrome_headless":
        chrome_options = CH_Options()
        chrome_options.add_argument('--headless')
        if driver_path is not None:
            chromedriver = webdriver.Chrome(chrome_options=chrome_options, options=option)
            chromedriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })
            return chromedriver
        chromedriver = webdriver.Chrome(options=option)
        chromedriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return chromedriver
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
    elif name in PHONE_LIST:
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
        driver.set_window_size(width=480, height=900)
        return driver
    elif name in PAD_LIST:
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
        driver.set_window_size(width=1100, height=900)
        return driver
    else:
        raise NameError(
            "Not found '{}' browser, See the help doc: https://github.com/SeldomQA/seldom/blob/master/docs/driver.md'.".format(name))


def app(command_executor, desired_capabilities):
    """
    Run class initialization method, Get App driver.
    :param command_executor: appium desktop url
    :param desired_capabilities: app info.
    :return:
    """
    return Remote(command_executor=command_executor, desired_capabilities=desired_capabilities)
