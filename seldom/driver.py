"""
browser driver
"""
import warnings
from selenium import webdriver
from seldom.logging.exceptions import BrowserTypeError
from seldom.running.config import BrowserConfig


__all__ = ["Browser"]


class Browser:
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "Internet Explorer" or "ie".
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

        raise BrowserTypeError(f"Not found `{name}` browser, See the help doc: https://seldomqa.github.io/web-testing/browser_driver.html.")

    @staticmethod
    def chrome():
        """
        Chrome browser driver
        """
        if BrowserConfig.executable_path != "":
            warnings.warn("selenium manager browser driver. Not need to set the `executable_path`",  stacklevel=2)
        is_grid = False
        if BrowserConfig.command_executor != "":
            is_grid = True
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor)
        else:
            driver = webdriver.Chrome(options=BrowserConfig.options)

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
        """
        firefox browser driver
        """
        if BrowserConfig.executable_path != "":
            warnings.warn("selenium manager browser driver. Not need to set the `executable_path`",  stacklevel=2)
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor)
        else:
            driver = webdriver.Firefox(options=BrowserConfig.options)

        return driver

    @staticmethod
    def ie():
        """
        internet explorer browser driver
        """
        if BrowserConfig.executable_path != "":
            warnings.warn("selenium manager browser driver. Not need to set the `executable_path`",  stacklevel=2)
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor)
        else:
            driver = webdriver.Ie(options=BrowserConfig.options)

        return driver

    @staticmethod
    def edge():
        """
        edge browser driver
        """
        if BrowserConfig.executable_path != "":
            warnings.warn("selenium manager browser driver. Not need to set the `executable_path`",  stacklevel=2)
        if BrowserConfig.command_executor != "":
            driver = webdriver.Remote(options=BrowserConfig.options,
                                      command_executor=BrowserConfig.command_executor)
        else:
            driver = webdriver.Edge(options=BrowserConfig.options)

        return driver

    @staticmethod
    def safari():
        """safari browser driver"""
        if BrowserConfig.command_executor != "":
            return webdriver.Remote(command_executor=BrowserConfig.command_executor)
        else:
            return webdriver.Safari()
