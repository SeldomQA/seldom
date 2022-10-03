"""
appium laboratory
"""
from seldom.logging import log
from seldom.appium_lab.action import Action
from seldom.appium_lab.find import FindByText
from seldom.appium_lab.keyboard import KeyEvent


class AppiumLab(Action, FindByText, KeyEvent):
    """
    app state:
    【0】 is not installed.
    【1】 is not running.
    【2】 is running in background or suspended.
    【3】 is running in background.
    【4】 is running in foreground. (number)
    """

    def check_state(self, app_id: str) -> int:
        """
        check app state
        :param app_id:
        :return:
        """
        state = self.driver.query_app_state(app_id)
        if state == 0:
            log.info(f"{app_id} is not installed.")
        elif state == 1:
            log.info(f"{app_id} is not running.")
        elif state == 2:
            log.info(f"{app_id} is running in background or suspended.")
        elif state == 3:
            log.info(f"{app_id} is running in background.")
        elif state == 4:
            log.info(f"{app_id} is running in foreground.")
        else:
            log.info(f"{app_id} state of the unknown.")
        return state

    def launch_app(self, app_id: str) -> None:
        """launch app"""
        log.info(f"launch App {app_id}")
        self.switch_to_app()
        state = self.check_state(app_id)
        if state != 4:
            self.driver.launch_app()

    def close_app(self, app_id: str) -> None:
        """close app"""
        log.info(f"close App {app_id}")
        self.switch_to_app()
        self.driver.close_app()
        self.check_state(app_id)
