from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser(name=None):
    """
    Run class initialization method, the default is proper
    to drive the Firefox browser. Of course, you can also
    pass parameter for other browser, Chrome browser for the "Chrome",
    the Internet Explorer browser for "internet explorer" or "ie".
    :param name: Browser name
    :return:
    """
    if name is None:
        name = "chrome"

    if name == "firefox" or name == "ff":
        return webdriver.Firefox()
    elif name == "chrome":
        return webdriver.Chrome()
    elif name == "internet explorer" or name == "ie":
        return webdriver.Ie()
    elif name == "opera":
        return webdriver.Opera()
    elif name == "chrome_headless":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(chrome_options=chrome_options)
    elif name == 'edge':
        return webdriver.Edge()
    else:
        raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)
