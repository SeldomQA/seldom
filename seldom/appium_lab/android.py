from appium.options.android import UiAutomator2Options
from appium.options.common.base import T
from typing import Any, Dict
from seldom.running.config import Seldom


class UiAutomator2Options(UiAutomator2Options):
    """
    Override UiAutomator2Options class methods
    """

    def load_capabilities(self: T, caps: Dict[str, Any]) -> T:
        """Sets multiple capabilities"""
        for name, value in caps.items():
            if name == "appPackage":
                Seldom.app_package = value
            self.set_capability(name, value)
        return self
