"""
appium action
"""
from time import sleep
from seldom.logging import log
from seldom.appium_lab.switch import Switch
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


class Action(Switch):
    """
    Encapsulate basic actions: swipe, tap, etc
    """

    def __init__(self, driver):
        Switch.__init__(self, driver)
        self.switch_to_app()
        self._size = self.driver.get_window_size()
        self.width = self._size.get("width")     # {'width': 1080, 'height': 2028}
        self.height = self._size.get("height")   # {'width': 1080, 'height': 2028}

    def size(self) -> dict:
        """
        return screen resolution.
        """
        log.info(f"screen resolution: {self._size}")
        return self._size

    def tap(self, x: int, y: int) -> None:
        """
        Tap on the coordinates
        :param x: x coordinates
        :param y: y coordinates
        :return:
        """
        self.switch_to_app()
        log.info(f"top x={x},y={y}.")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        sleep(2)

    def swipe_up(self, times: int = 1, upper: bool = False):
        """
        swipe up
        :param times: swipe times
        :param upper: Keyboard screen occlusion, swipe only the upper half of the area.
        :return:
        """
        self.switch_to_app()
        log.info(f"swipe up {times} times")
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

        if upper is True:
            self.height = (self.height / 2)

        y_start = int((self.height / 3) * 2)
        y_end = int((self.height / 3) * 1)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            sleep(1)

    def swipe_down(self, times: int = 1, upper: bool = False) -> None:
        """
        swipe down
        :param times: swipe times
        :param upper: Keyboard screen occlusion, swipe only the upper half of the area.
        :return:
        """
        self.switch_to_app()
        log.info(f"swipe down {times} times")
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

        if upper is True:
            self.height = (self.height / 2)

        y_start = int((self.height / 3) * 1)
        y_end = int((self.height / 3) * 2)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            sleep(1)
