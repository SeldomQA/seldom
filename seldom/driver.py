"""
browser driver
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as fService
from selenium.webdriver.ie.service import Service as iService
from selenium.webdriver.edge.service import Service as eService
from selenium.webdriver.chrome.service import Service as cService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seldom.utils.webdriver_manager_extend import ChromeDriverManager

__all__ = ["ChromeConfig", "FirefoxConfig", "IEConfig", "EdgeConfig", "OperaConfig", "SafariConfig", "Browser"]

PHONE_LIST = [
    'iPhone 8', 'iPhone 8 Plus', 'iPhone SE', 'iPhone X', 'iPhone XR', 'iPhone 12 Pro',
    'Pixel 2', 'Pixel XL', 'Pixel 5', 'Samsung Galaxy S8+', 'Samsung Galaxy S20 Ultra'
]
PAD_LIST = ['iPad Air', 'iPad Pro', 'iPad Mini']


class ChromeConfig:
    headless = False
    options = None
    command_executor = ""


class FirefoxConfig:
    headless = False
    options = None
    command_executor = ""


class IEConfig:
    command_executor = ""


class EdgeConfig:
    headless = False
    options = None
    command_executor = ""


class OperaConfig:
    command_executor = ""


class SafariConfig:
    executable_path = "/usr/bin/safaridriver"
    command_executor = ""


class Browser:
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "internet explorer" or "ie".
    """

    def __new__(cls, name: str = None):

        if (name is None) or (name in ["chrome", "google chrome", "gc"]):
            return cls.chrome()
        if name in ["firefox", "ff"]:
            return cls.firefox()
        if name in ["internet explorer", "ie", "IE"]:
            return cls.ie()
        if name == "edge":
            return cls.edge()
        if name == "safari":
            return cls.safari()
        if name in PHONE_LIST:
            return cls.phone(name)
        if name in PAD_LIST:
            return cls.pad(name)

        raise NameError(f"Not found `{name}` browser, See the help doc: https://seldomqa.github.io/other/other.html.")

    @staticmethod
    def chrome():
        """Chrome browser driver"""
        if ChromeConfig.options is None:
            chrome_options = ChromeOptions()
        else:
            chrome_options = ChromeConfig.options

        if ChromeConfig.headless is True:
            chrome_options.add_argument('--headless')

        is_grid = False
        if ChromeConfig.command_executor == "":
            driver = webdriver.Chrome(options=chrome_options,
                                      service=cService(ChromeDriverManager().install()))
        elif ChromeConfig.command_executor[:4] == "http":
            is_grid = True
            driver = webdriver.Remote(options=chrome_options,
                                      command_executor=ChromeConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.CHROME.copy())
        else:
            driver = webdriver.Chrome(options=chrome_options,
                                      executable_path=ChromeConfig.command_executor)

        if is_grid is False:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })

        return driver

    @staticmethod
    def firefox():
        """firefox browser driver"""
        if FirefoxConfig.options is None:
            firefox_options = FirefoxOptions()
        else:
            firefox_options = FirefoxConfig.options

        if FirefoxConfig.headless is True:
            firefox_options.add_argument('-headless')

        if FirefoxConfig.command_executor == "":
            driver = webdriver.Firefox(options=firefox_options,
                                       service=fService(GeckoDriverManager().install()))
        elif FirefoxConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(options=firefox_options,
                                      command_executor=FirefoxConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        else:
            driver = webdriver.Firefox(options=firefox_options,
                                       executable_path=FirefoxConfig.command_executor)

        return driver

    @staticmethod
    def ie():
        """internet explorer browser driver"""
        if IEConfig.command_executor == "":
            driver = webdriver.Ie(service=iService(IEDriverManager().install()))
        elif IEConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(command_executor=IEConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        else:
            driver = webdriver.Ie(executable_path=IEConfig.command_executor)

        return driver

    @staticmethod
    def edge():
        """edge browser driver"""
        if EdgeConfig.options is None:
            edge_options = EdgeOptions()
        else:
            edge_options = EdgeConfig.options

        if EdgeConfig.headless is True:
            edge_options.headless = True

        if EdgeConfig.command_executor == "":
            driver = webdriver.Edge(options=edge_options,
                                    service=eService(EdgeChromiumDriverManager().install()))
        elif EdgeConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(options=edge_options,
                                      command_executor=EdgeConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.EDGE.copy())
        else:
            driver = webdriver.Edge(options=edge_options,
                                    executable_path=EdgeConfig.command_executor)

        return driver

    @staticmethod
    def safari():
        """safari browser driver"""
        if SafariConfig.command_executor != "" and SafariConfig.command_executor[:4] == "http":
            return webdriver.Remote(command_executor=SafariConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.SAFARI.copy())
        return webdriver.Safari(executable_path=SafariConfig.executable_path)

    @staticmethod
    def phone(name: str):
        """phone mode driver"""
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": name})

        if ChromeConfig.headless is True:
            chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options,
                                  service=cService(ChromeDriverManager().install()))
        driver.set_window_size(width=480, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
        })
        return driver

    @staticmethod
    def pad(name: str):
        """pad mode driver"""
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": name})

        if ChromeConfig.headless is True:
            chrome_options.add_argument('--headless')

        driver = webdriver.Chrome(options=chrome_options,
                                  service=cService(ChromeDriverManager().install()))
        driver.set_window_size(width=1100, height=900)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
        })
        return driver
