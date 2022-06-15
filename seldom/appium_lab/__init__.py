from seldom.logging import log
from seldom.appium_lab.action import Action
from seldom.appium_lab.find import FindByText


class AppiumLab(Action, FindByText):

    def close_app(self) -> None:
        """
        close app.
        """
        log.info("close App")
        self.driver.close_app()

    def launch_app(self):
        """
        launch app.
        """
        log.info("launch App")
        self.driver.launch_app()
