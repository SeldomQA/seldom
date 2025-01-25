"""
browser driver
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.safari.service import Service as SafariService

from seldom.logging.exceptions import BrowserTypeError

__all__ = ["Browser"]


class Browser:
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "Internet Explorer" or "ie".
    """

    def __new__(cls, name: str = None, executable_path=None, options=None, command_executor=""):
        """
        new browser driver
        :param name: browser name.
        :param executable_path: browser driver path.
        :param options:
        :param command_executor:
        """

        if (name is None) or (name in ["chrome", "google chrome", "gc"]):
            return cls.chrome(executable_path, options, command_executor)
        if name in ["firefox", "ff"]:
            return cls.firefox(executable_path, options, command_executor)
        if name in ["internet explorer", "ie", "IE"]:
            return cls.ie(executable_path, options, command_executor)
        if name == "edge":
            return cls.edge(executable_path, options, command_executor)
        if name == "chromium":
            return cls.edge(executable_path, options, command_executor)
        if name == "safari":
            return cls.safari(executable_path, options, command_executor)

        raise BrowserTypeError(
            f"Not found `{name}` browser, See the help doc: https://seldomqa.github.io/web-testing/browser_driver.html.")

    @staticmethod
    def chrome(executable_path, options, command_executor):
        """
        Chrome browser driver
        """
        is_grid = False
        if command_executor != "":
            is_grid = True
            driver = webdriver.Remote(options=options, command_executor=command_executor)
        else:
            driver = webdriver.Chrome(options=options, service=ChromeService(executable_path=executable_path))

        if is_grid is False:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })"""
            })

        return driver

    @staticmethod
    def firefox(executable_path, options, command_executor):
        """
        firefox browser driver
        """
        if command_executor != "":
            driver = webdriver.Remote(options=options, command_executor=command_executor)
        else:
            driver = webdriver.Firefox(options=options, service=FireFoxService(executable_path=executable_path))

        return driver

    @staticmethod
    def ie(executable_path, options, command_executor):
        """
        internet explorer browser driver
        """
        if command_executor != "":
            driver = webdriver.Remote(options=options, command_executor=command_executor)
        else:
            driver = webdriver.Ie(options=options, service=IEService(executable_path=executable_path))

        return driver

    @staticmethod
    def edge(executable_path, options, command_executor):
        """
        edge browser driver
        """
        if command_executor != "":
            driver = webdriver.Remote(options=options, command_executor=command_executor)
        else:
            driver = webdriver.Edge(options=options, service=EdgeService(executable_path=executable_path))

        return driver

    @staticmethod
    def safari(executable_path, options, command_executor):
        """
        safari browser driver
        """
        if command_executor != "":
            return webdriver.Remote(options=options, command_executor=command_executor)
        else:
            return webdriver.Safari(options=options, service=SafariService(executable_path=executable_path))
