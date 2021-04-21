from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

__all__ = [
    "ChromeConfig", "FirefoxConfig", "IEConfig", "EdgeConfig", "OperaConfig", "SafariConfig", "Browser"
]

PHONE_LIST = [
    'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8', 'iPhone 8 Plus',
    'iPhone X', 'Pixel 2', 'Pixel XL', "Galaxy S5"
]
PAD_LIST = ['iPad', 'iPad Pro']


class ChromeConfig:
    headless = False
    executable_path = "chromedriver"
    options = None
    command_executor = ""


class FirefoxConfig:
    headless = False
    executable_path = "geckodriver"
    options = None
    command_executor = ""


class IEConfig:
    executable_path = "IEDriverServer.exe"
    command_executor = ""


class EdgeConfig:
    executable_path = "MicrosoftWebDriver.exe"
    command_executor = ""


class OperaConfig:
    executable_path = "operadriver"
    command_executor = ""


class SafariConfig:
    executable_path = "/usr/bin/safaridriver"
    command_executor = ""


class Browser(object):
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "internet explorer" or "ie".
    :param name: Browser name
    :return:
    """

    def __new__(cls, name=None):
        cls.name = name

        if (cls.name is None) or (cls.name in ["chrome", "google chrome", "gc"]):
            return cls.chrome()
        elif cls.name in ["firefox", "ff"]:
            return cls.firefox()
        elif cls.name in ["internet explorer", "ie", "IE"]:
            return cls.ie()
        elif cls.name == "edge":
            return cls.edge()
        elif cls.name == "opera":
            return cls.opera()
        elif cls.name == "safari":
            return cls.safari()
        elif cls.name in PHONE_LIST:
            return cls.phone(name)
        elif cls.name in PAD_LIST:
            return cls.pad(name)
        raise NameError(
            "Not found '{}' browser, See the help doc: https://github.com/SeldomQA/seldom/blob/master/docs/driver.md'.".format(cls.name))

    @staticmethod
    def chrome():
        if ChromeConfig.command_executor != "":
            return webdriver.Remote(command_executor=ChromeConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.CHROME.copy())

        if ChromeConfig.options is None:
            chrome_options = ChromeOptions()
            if ChromeConfig.headless is True:
                chrome_options.add_argument('--headless')
        else:
            chrome_options = ChromeConfig.options
            if ChromeConfig.headless is True:
                chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=ChromeConfig.executable_path)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })"""
        })
        return driver

    @staticmethod
    def firefox():
        if FirefoxConfig.command_executor != "":
            return webdriver.Remote(command_executor=FirefoxConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.FIREFOX.copy())

        if FirefoxConfig.options is None:
            firefox_options = FirefoxOptions()
            if FirefoxConfig.headless is True:
                firefox_options.headless = True
        else:
            firefox_options = FirefoxConfig.options
            if FirefoxConfig.headless is True:
                firefox_options.headless = True

        driver = webdriver.Firefox(options=firefox_options,
                                   executable_path=FirefoxConfig.executable_path)
        return driver

    @staticmethod
    def ie():
        if IEConfig.command_executor != "":
            return webdriver.Remote(command_executor=IEConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        return webdriver.Ie(executable_path=IEConfig.executable_path)

    @staticmethod
    def edge():
        if EdgeConfig.command_executor != "":
            return webdriver.Remote(command_executor=EdgeConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.EDGE.copy())
        return webdriver.Edge(executable_path=EdgeConfig.executable_path)

    @staticmethod
    def opera():
        if OperaConfig.command_executor != "":
            return webdriver.Remote(command_executor=OperaConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.OPERA.copy())
        return webdriver.Opera(executable_path=OperaConfig.executable_path)

    @staticmethod
    def safari():
        if SafariConfig.command_executor != "":
            return webdriver.Remote(command_executor=SafariConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.SAFARI.copy())
        return webdriver.Safari(executable_path=SafariConfig.executable_path)

    @staticmethod
    def phone(name):
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=ChromeConfig.executable_path,
                                  options=ChromeConfig.options)
        driver.set_window_size(width=480, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
        })
        return driver

    @staticmethod
    def pad(name):
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": name})
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=ChromeConfig.executable_path,
                                  options=ChromeConfig.options)
        driver.set_window_size(width=1100, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
        })
        return driver
