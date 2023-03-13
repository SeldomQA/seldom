"""
browser driver
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as fService
from selenium.webdriver.ie.service import Service as iService
from selenium.webdriver.edge.service import Service as eService
from selenium.webdriver.chrome.service import Service as cService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from seldom.utils.webdriver_manager_extend import ChromeDriverManager
from seldom.logging.exceptions import BrowserTypeError
from seldom.running.config import BrowserConfig


__all__ = ["Browser"]


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

        raise BrowserTypeError(f"Not found `{name}` browser, See the help doc: https://seldomqa.github.io/other/other.html.")

    @staticmethod
    def chrome():
        """Chrome browser driver"""
        is_grid = False
        if BrowserConfig.command_executor != "":
            is_grid = True
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.CHROME.copy())
        elif BrowserConfig.executable_path != "":
            driver = webdriver.Chrome(options=BrowserConfig.options,
                                      executable_path=BrowserConfig.executable_path)
        else:
            driver = webdriver.Chrome(options=BrowserConfig.options,
                                      service=cService(ChromeDriverManager().install()))

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
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        elif BrowserConfig.executable_path != "":
            driver = webdriver.Firefox(options=BrowserConfig.options,
                                       executable_path=BrowserConfig.executable_path)
        else:
            driver = webdriver.Firefox(options=BrowserConfig.options,
                                       service=fService(GeckoDriverManager().install()))

        return driver

    @staticmethod
    def ie():
        """internet explorer browser driver"""
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        elif BrowserConfig.executable_path != "":
            driver = webdriver.Ie(options=BrowserConfig.options,
                                  executable_path=BrowserConfig.executable_path)
        else:
            driver = webdriver.Ie(options=BrowserConfig.options,
                                  service=iService(IEDriverManager().install()))

        return driver

    @staticmethod
    def edge():
        """edge browser driver"""
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.EDGE.copy())
        elif BrowserConfig.executable_path != "":
            driver = webdriver.Edge(options=BrowserConfig.options,
                                    executable_path=BrowserConfig.executable_path)
        else:
            driver = webdriver.Edge(options=BrowserConfig.options,
                                    service=eService(EdgeChromiumDriverManager().install()))

        return driver

    @staticmethod
    def safari():
        """safari browser driver"""
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.SAFARI.copy())
        elif BrowserConfig.executable_path != "":
            return webdriver.Safari(executable_path=BrowserConfig.executable_path)
        else:
            return webdriver.Safari()
