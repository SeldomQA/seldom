from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
    CHROMEDRIVER = "chromedriver"
    FIREFOXDRIVER = "geckodriver"
    IEDRIVER = "IEDriverServer.exe"
    OPERADRIVER ="operadriver"
    EDGEDRIVER = "MicrosoftWebDriver.exe"
    SAFAIRDRIVER = "/usr/bin/safaridriver"

    # Prevention of detection
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    if name is None:
        name = "chrome"

    if name in ["firefox", "ff"]:
        if driver_path is None:
            driver_path = FIREFOXDRIVER
        if grid_url is not None:
            return webdriver.Remote(command_executor=grid_url,
                                    desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        return webdriver.Firefox(executable_path=driver_path)

    elif name in ["chrome", "google chrome", "gc"]:
        if driver_path is None:
            driver_path = CHROMEDRIVER
        if grid_url is not None:
            return webdriver.Remote(command_executor=grid_url,
                                    desired_capabilities=DesiredCapabilities.CHROME.copy())
        driver = webdriver.Chrome(options=option, executable_path=driver_path)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return driver
    elif name == ["internet explorer", "ie", "IE"]:
        if driver_path is None:
            driver_path = IEDRIVER
        return webdriver.Ie(executable_path=driver_path)
    elif name == "opera":
        if driver_path is None:
            driver_path = OPERADRIVER
        return webdriver.Opera(executable_path=driver_path)

    elif name == "chrome_headless":
        if driver_path is None:
            driver_path = CHROMEDRIVER
        chrome_options = CH_Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options, options=option, executable_path=driver_path)
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
        if driver_path is None:
            driver_path = FIREFOXDRIVER
        return webdriver.Firefox(firefox_options=firefox_options, executable_path=driver_path)

    elif name == 'edge':
        if driver_path is None:
            driver_path = EDGEDRIVER
        return webdriver.Edge(executable_path=driver_path)

    elif name == 'safari':
        if driver_path is None:
            driver_path = SAFAIRDRIVER
        return webdriver.Safari(executable_path=driver_path)

    elif name in PHONE_LIST:
        if driver_path is None:
            driver_path = CHROMEDRIVER
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path, options=option)
        driver.set_window_size(width=480, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                    })"""
        })
        return driver

    elif name in PAD_LIST:
        if driver_path is None:
            driver_path = CHROMEDRIVER
        options = CH_Options()
        options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path, options=option)
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
