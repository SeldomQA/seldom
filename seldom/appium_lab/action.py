"""
appium action
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from seldom.appium_lab.switch import Switch
from seldom.logging import log


class Action(Switch):
    """
    Encapsulate basic actions: swipe, tap, etc
    """

    def __init__(self, driver=None):
        Switch.__init__(self, driver)
        self.switch_to_app()
        self._size = self.driver.get_window_size()
        self.width = self._size.get("width")  # {'width': 1080, 'height': 2028}
        self.height = self._size.get("height")  # {'width': 1080, 'height': 2028}

    def size(self) -> dict:
        """
        return screen resolution.
        """
        log.info(f"screen resolution: {self._size}")
        return self._size

    def tap(self, x: int, y: int, pause: float = 0.1, sleep: float = 2) -> None:
        """
        Tap on the coordinates
        :param x: x coordinates
        :param y: y coordinates
        :param pause: pause time
        :param sleep: sleep time
        :return:
        """
        self.switch_to_app()
        log.info(f"top x={x},y={y}.")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(pause)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.sleep(sleep)

    def swipe_up(self, times: int = 1, upper: bool = False, interval_time: float = 1):
        """
        swipe up
        :param times: swipe times
        :param upper: Keyboard screen occlusion, swipe only the upper half of the area.
        :param interval_time: interval time
        :return:
        """
        self.switch_to_app()
        log.info(f"⬆️ swipe up {times} times")
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
            self.sleep(interval_time)

    def swipe_down(self, times: int = 1, upper: bool = False, interval_time: float = 1) -> None:
        """
        swipe down
        :param times: swipe times
        :param upper: Keyboard screen occlusion, swipe only the upper half of the area.
        :param interval_time: interval time
        :return:
        """
        self.switch_to_app()
        log.info(f"⬇️ swipe down {times} times")
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
            self.sleep(interval_time)

    def swipe_left(self, times: int = 1, width_percentage: float = 0.8, interval_time: float = 1):
        """
        Swipe left
        :param times: swipe times
        :param width_percentage: Percentage of the screen width to swipe (default 80%)
        :param interval_time: interval time
        :return:
        """
        self.switch_to_app()
        log.info(f"⬅️ swipe left {times} times")

        x_start = int(self.width * (1 - width_percentage / 2))
        x_end = int(self.width * width_percentage / 2)
        y_start = int(self.height / 2)
        y_end = int(self.height / 2)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            self.sleep(interval_time)

    def swipe_right(self, times: int = 1, width_percentage: float = 0.8, interval_time: float = 1):
        """
        Swipe right
        :param times: swipe times
        :param width_percentage: Percentage of the screen width to swipe (default 80%)
        :param interval_time: interval time
        :return:
        """
        self.switch_to_app()
        log.info(f"➡️ swipe right {times} times")

        x_start = int(self.width * width_percentage / 2)
        x_end = int(self.width * (1 - width_percentage / 2))
        y_start = int(self.height / 2)
        y_end = int(self.height / 2)

        for _ in range(times):
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_start, y_start)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_end, y_end)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            self.sleep(interval_time)
