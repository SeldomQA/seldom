from appium.webdriver.common.appiumby import AppiumBy
from seldom.logging import log
from seldom.appium_lab.switch import Switch


class FindByText(Switch):
    """
    查找元素
    """

    def __find(self, class_name: str, attribute: str, text: str):
        """
        find element
        :param class_name: class name
        :param attribute: attribute
        :param text: text
        :return:
        """
        elems = self.driver.find_elements(AppiumBy.CLASS_NAME, class_name)
        for _ in range(3):
            if len(elems) > 0:
                break
            else:
                self.sleep(1)

        for elem in elems:
            if elem.get_attribute(attribute) is None:
                continue
            if text in elem.get_attribute(attribute):
                log.info(f'find -> {elem.get_attribute(attribute)}')
                return elem
        else:
            return None

    def find_view(self, text):
        """
        查找view
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.view.View", attribute="content-desc", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_edit_text(self, text):
        """
        查找editText
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.EditText", attribute="text", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_button(self, text):
        """
        查找button
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.Button", attribute="text", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_text_view(self, text):
        """
        查找TextView
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.TextView", attribute="text", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_image_view(self, text):
        """
        查找ImageView
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.ImageView", attribute="content-desc", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem

    def find_check_box(self, text):
        """
        查找CheckBox
        :param text: 匹配文本
        :return:
        """
        self.switch_to_app()
        for _ in range(3):
            elem = self.__find(class_name="android.widget.CheckBox", attribute="text", text=text)
            if elem is not None:
                break
            else:
                self.sleep(1)
        else:
            raise ValueError(f"Unable to find -> {text}")

        return elem
