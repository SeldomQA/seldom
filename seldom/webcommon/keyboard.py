import platform

from selenium.webdriver.common.keys import Keys

from seldom.logging import log
from seldom.webcommon.find_elems import WebElement


class KeysClass:
    """
    Achieve keyboard shortcuts

    Usage:
        self.Keys(id_="kw").enter()
    """

    def __init__(self, browser, selector: str = None, index: int = 0, **kwargs) -> None:
        self.browser = browser
        self.web_elem = WebElement(self.browser, selector=selector, **kwargs)
        self.elem = self.web_elem.find(index, highlight=True)

    def input(self, text=""):
        """
        input text
        :param text:
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, input '{text}'.")
        self.elem.send_keys(text)
        return self

    def enter(self):
        """
        enter.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, enter.")
        self.elem.send_keys(Keys.ENTER)
        return self

    def select_all(self):
        """
        select all.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, ctrl+a.")
        if platform.system().lower() == "darwin":
            self.elem.send_keys(Keys.COMMAND, "a")
        else:
            self.elem.send_keys(Keys.CONTROL, "a")
        return self

    def cut(self):
        """
        cut.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, ctrl+x.")
        if platform.system().lower() == "darwin":
            self.elem.send_keys(Keys.COMMAND, "x")
        else:
            self.elem.send_keys(Keys.CONTROL, "x")
        return self

    def copy(self):
        """
        copy.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, ctrl+c.")
        if platform.system().lower() == "darwin":
            self.elem.send_keys(Keys.COMMAND, "c")
        else:
            self.elem.send_keys(Keys.CONTROL, "c")
        return self

    def paste(self):
        """
        paste.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, ctrl+v.")
        if platform.system().lower() == "darwin":
            self.elem.send_keys(Keys.COMMAND, "v")
        else:
            self.elem.send_keys(Keys.CONTROL, "v")
        return self

    def backspace(self):
        """
        Backspace key.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, backspace.")
        self.elem.send_keys(Keys.BACKSPACE)
        return self

    def delete(self):
        """
        Delete key.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, delete.")
        self.elem.send_keys(Keys.DELETE)
        return self

    def tab(self):
        """
        Tab key.
        """
        log.info(f"✅ {self.web_elem.info}, tab.")
        self.elem.send_keys(Keys.TAB)

    def space(self):
        """
        Space key.
        :return:
        """
        log.info(f"✅ {self.web_elem.info}, space.")
        self.elem.send_keys(Keys.SPACE)
        return self
