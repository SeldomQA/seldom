from appium.options.android import UiAutomator2Options
from appium.options.android import EspressoOptions
from appium.options.common.base import T
from typing import Any, Dict
from seldom.running.config import Seldom
from seldom.logging import log


class UiAutomator2Options(UiAutomator2Options):
    """
    Override UiAutomator2Options class methods
    """

    def load_capabilities(self: T, caps: Dict[str, Any]) -> T:
        """Sets multiple capabilities"""
        log.info(f"app info: {caps}")
        for name, value in caps.items():
            if name == "appPackage":
                Seldom.app_package = value
            self.set_capability(name, value)
        return self


class EspressoOptions(EspressoOptions):
    """
    Override EspressoOptions class methods
    """
    
    def load_capabilities(self: T, caps: Dict[str, Any]) -> T:
        """Sets multiple capabilities"""
        log.info(f"app info: {caps}")
        for name, value in caps.items():
            Seldom.app_package = value
            self.set_capability(name, value)
        return self
