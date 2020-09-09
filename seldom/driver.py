from selenium import webdriver as selenium
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from appium import webdriver as appium


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
            return selenium.Firefox(executable_path=driver_path)
        if grid_url is not None:
            return selenium.Remote(command_executor=grid_url,
                                    desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        return selenium.Firefox()
    elif name in ["chrome", "google chrome", "gc"]:
        if driver_path is not None:
            driver = selenium.Chrome(executable_path=driver_path, options=option)
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })
            return driver
        if grid_url is not None:
            return selenium.Remote(command_executor=grid_url,
                                   desired_capabilities=DesiredCapabilities.CHROME.copy())
        driver = selenium.Chrome(options=option)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return driver
    elif name == ["internet explorer", "ie", "IE"]:
        return selenium.Ie()
    elif name == "opera":
        return selenium.Opera()
    elif name == "chrome_headless":
        chrome_options = CH_Options()
        chrome_options.add_argument('--headless')
        if driver_path is not None:
            driver = selenium.Chrome(chrome_options=chrome_options, options=option)
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })
            return driver
        driver = selenium.Chrome(options=option)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return driver
    elif name == "firefox_headless":
        firefox_options = FF_Options()
        firefox_options.headless = True
        if driver_path is not None:
            return selenium.Firefox(firefox_options=firefox_options, executable_path=driver_path)
        return selenium.Firefox(firefox_options=firefox_options)
    elif name == 'edge':
        return selenium.Edge()
    elif name == 'safari':
        return selenium.Safari()
    elif name in PHONE_LIST:
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = selenium.Chrome(chrome_options=options, executable_path=driver_path, options=option)
        driver.set_window_size(width=480, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                    })"""
        })
        return driver
    elif name in PAD_LIST:
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = selenium.Chrome(chrome_options=options, executable_path=driver_path, options=option)

        driver.set_window_size(width=1100, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                    })"""
        })
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
    return appium.Remote(command_executor, desired_capabilities=desired_capabilities)
