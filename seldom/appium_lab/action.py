from seldom.appium_lab.switch import Switch
from seldom.logging import log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


class Action(Switch):
    """
    封装基本动作：滑动、点击等
    """

    def __init__(self, driver):
        Switch.__init__(self, driver)
        self.switch_to_app()
        size = self.driver.get_window_size()
        self.width = size.get("width")     # {'width': 1080, 'height': 2028}
        self.height = size.get("height")   # {'width': 1080, 'height': 2028}

    def tap(self, x, y):
        """
        坐标为位点击
        :param x: 横向坐标
        :param y: 纵向坐标
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
        self.sleep(2)

    def swipe_up(self, times=1, up=False):
        """
        向上滑动
        :param times: 滑动次数
        :param up: 因为屏幕键盘遮挡，只滑动上半个区域
        :return:
        """
        self.switch_to_app()
        log.info(f"swipe up {times} times")
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

        if up is True:
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
            self.sleep(1)

    def swipe_down(self, times=1):
        """
        向下滑动
        :param times: 滑动次数
        :return:
        """
        self.switch_to_app()
        x_start = int(self.width / 2)
        x_end = int(self.width / 2)

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
            self.sleep(1)
