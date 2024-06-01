"""
switch app context
"""
import time

from seldom.logging import log
from seldom import Seldom


class Switch:
    """
    switch context by appium
    """

    def __init__(self, driver=None):
        self.driver = Seldom.driver
        if driver is not None:
            self.driver = driver

    def context(self):
        """
        Returns the current context of the current session.
        """
        current_context = self.driver.current_context
        all_context = self.driver.contexts
        log.info(f"current context: {current_context}.")
        log.info(f"all context: {all_context}.")
        return current_context

    def switch_to_app(self) -> None:
        """
        Switch to native app.
        """
        current_context = self.driver.current_context
        if current_context != "NATIVE_APP":
            log.info("🔀 switch to native app.")
            self.driver.switch_to.context('NATIVE_APP')

    def switch_to_web(self, context_name: str = None) -> None:
        """
        Switch to web view.
        """
        log.info("🔀 switch to webview.")
        if context_name is not None:
            self.driver.switch_to.context(context_name)
        else:
            all_context = self.driver.contexts
            for context in all_context:
                if "WEBVIEW" in context:
                    self.driver.switch_to.context(context)
                    break
            else:
                raise NameError("No WebView found.")

    def switch_to_flutter(self) -> None:
        """
        Switch to flutter app.
        """
        current_context = self.driver.current_context
        if current_context != "FLUTTER":
            log.info("🔀 switch to flutter.")
            self.driver.switch_to.context('FLUTTER')

    def switch_to_ocr(self) -> None:
        """
        Switch to OCR app.
        help: https://github.com/jlipps/appium-ocr-plugin
        """
        log.info("🔀 switch to OCR.")
        self.driver.switch_to.context('OCR')

    @staticmethod
    def sleep(sec):
        """
        python time.sleep()
        :param sec:
        """
        time.sleep(sec)
