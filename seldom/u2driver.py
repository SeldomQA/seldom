"""
uiautomator2 driver API
"""
import os
import time
from seldom.logging import log
from seldom.running.config import Seldom, AppConfig
from seldom.logging.exceptions import NotFindElementError

__all__ = ["U2Driver", "U2Element"]

keycodes = {
    'HOME': 'home',
    'BACK': 'back',
    'LEFT': 'left',
    'ENTER': 'enter',
}

LOCATOR_LIST = {
    'id_': "resourceId",
    'name': "name",
    'xpath': "xpath",
    'text': 'text',
    'class_name': "className",
}


class U2Element:
    """uiautomator2 element API"""

    def __init__(self, **kwargs) -> None:
        self.driver = Seldom.driver
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        by, self.value = next(iter(kwargs.items()))
        if 'text' in kwargs:
            self.text = kwargs['text']
        else:
            self.text = None
        self.by = LOCATOR_LIST.get(by)
        if self.by is None:
            raise ValueError(f"The find element is not supported: {by}. ")
        self.find_elem_info = None
        self.find_elem_warn = None

    def get_elements(self, index: int = None, empty=False):
        try:
            if self.by == 'resourceId':
                if self.text:
                    elems = self.driver(resourceId=self.value, text=self.text)
                else:
                    elems = self.driver(resourceId=self.value)
            elif self.by == 'className':
                elems = self.driver(className=self.value)
            elif self.by == 'xpath':
                elems = self.driver.xpath(self.value).all()
            elif self.by == 'text':
                elems = self.driver(text=self.value)
            else:
                raise TypeError
        except TypeError:
            raise TypeError(f"❌ 请使用uiautomator2支持的定位方式: {self.by}={self.value}")
        except Exception as e:
            if empty is False:
                raise NotFindElementError(f"❌ Find element error: {self.by}={self.value} ---> {e}")
            else:
                return []

        if len(elems) >= 1:
            self.find_elem_info = f"Find {len(elems)} element: {self.by}={self.value} "

        if index is None:
            return elems

        return elems[index]

    @property
    def info(self):
        """return element info"""
        return self.find_elem_info

    @property
    def warn(self):
        """return element warn"""
        return self.find_elem_warn


class U2Driver:

    # def __init__(self):
    #     self.driver = Seldom.driver
    #     # self.driver.implicitly_wait(Seldom.timeout)

    # def background_app(self, seconds: int):

    #     """
    #     Puts the application in the background on the device for a certain duration.
    #
    #     Args:
    #         seconds: the duration for the application to remain in the background
    #     """
    #     Seldom.driver.background_app(seconds=seconds)
    #     return self

    # @staticmethod
    # def is_app_installed(bundle_id: str) -> bool:
    #     """Checks whether the application specified by `bundle_id` is installed on the device.
    #
    #     Args:
    #         bundle_id: the id of the application to query
    #
    #     Returns:
    #         `True` if app is installed
    #     """
    #     return Seldom.driver.is_app_installed(bundle_id=bundle_id)
    @staticmethod
    def implicitly_wait(timeout=Seldom.timeout):
        """set uiautomator2 implicitly wait"""
        Seldom.driver.implicitly_wait(timeout)

    def install_app_u2(self, app_path: str):
        """Install the application found at `app_path` on the device.

        Args:
            app_path: the local or remote path to the application to install

        """
        os.system(f'adb install -g {app_path}')
        return self

    def remove_app_u2(self, app_id: str = None):
        """Remove the specified application from the device.

        Args:
            app_id: the application id to be removed

        """
        if not app_id:
            app_id = Seldom.app_info.get('appPackage')
        Seldom.driver.app_uninstall(app_id)
        return self

    def launch_app_u2(self, stop: bool = False):
        """Start on the device the application specified in the desired capabilities.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.app_start(package_name=Seldom.app_info.get('appPackage'), stop=stop)
        log.info(f'启动APP：{Seldom.app_info.get("appPackage")}')
        return self

    def close_app_u2(self):
        """Stop the running application, specified in the desired capabilities, on
        the device.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        Seldom.driver.app_stop(Seldom.app_info.get('appPackage'))
        return self

    def clear_app_u2(self):
        """Resets the current application on the device.

        """
        Seldom.driver.app_clear(Seldom.app_info.get('appPackage'))
        return self

    @staticmethod
    def wait_app_u2():
        pid = Seldom.driver.app_wait(Seldom.app_info.get('appPackage'))
        return pid

    def set_text_u2(self, text: str, clear: bool = False, enter: bool = False, click: bool = False, index: int = 0,
                    **kwargs) -> None:
        """
        Operation input box.

        Usage:
            self.type(css="#el", text="selenium")
        """
        if clear is True:
            self.clear_text(index, **kwargs)
        if click is True:
            self.click_u2(index, **kwargs)
            time.sleep(0.5)
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index)
        log.info(f"✅ {u2_elem.info} -> input '{text}'.")
        elem.set_text(text)
        if enter is True:
            elem.press('enter')

    @staticmethod
    def clear_text_u2(index: int = 0, **kwargs) -> None:
        """
        Clear the contents of the input box.

        Usage:
            self.clear(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index)
        log.info(f"✅ {u2_elem.info} -> clear input.")
        elem.clear_text()

    @staticmethod
    def click_u2(index: int = 0, **kwargs) -> None:
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
            self.click(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index)
        log.info(f"✅ {u2_elem.info} -> click.")
        elem.click()

    @staticmethod
    def click_text_u2(text: str, index: int = 0) -> None:
        """
        Click the element by the link text

        Usage:
            self.click_text("新闻")
        """
        u2_elem = U2Element(text=text)
        elem = u2_elem.get_elements(index)
        log.info(f"✅ {u2_elem.info} -> click link.")
        elem.click()

    @staticmethod
    def get_text_u2(index: int = 0, **kwargs) -> str:
        """
        Get element text information.

        Usage:
            self.get_text(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index)
        text = elem.get_text()
        log.info(f"✅ {u2_elem.info} -> get text: {text}.")
        return text

    @staticmethod
    def get_display_u2(index: int = 0, **kwargs) -> bool:
        """
        Gets the element to display,The return result is true or false.

        Usage:
            self.get_display(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index)
        result = elem.exists
        log.info(f"✅ {u2_elem.info} -> element is display: {result}.")
        return result

    @staticmethod
    def wait_u2(timeout: int = Seldom.timeout, index: int = 0, **kwargs) -> None:
        """
        Implicitly wait element on the page.
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index)
        log.info(f"⌛️ implicitly wait: {timeout}s.")
        elem.wait(timeout=timeout)

    @staticmethod
    def start_recording_u2(output: str = 'record.mp4'):
        log.info(f"📷️  start_recording -> ({output}).")
        Seldom.driver.screenrecord(output, fps=AppConfig.fps)

    @staticmethod
    def stop_recording_u2():
        log.info(f"📷️  record down.")
        Seldom.driver.screenrecord.stop()

    # @staticmethod
    # def save_screenshot(file_path: str = None, index: int = 0, **kwargs) -> None:
    #     """
    #     Saves a screenshots of the current window to a PNG image file.
    #
    #     Usage:
    #         self.save_screenshot()
    #         self.save_screenshot('/Screenshots/foo.png')
    #         self.save_screenshot(id_="bLogo", index=0)
    #     """
    #
    #     if file_path is None:
    #         img_dir = os.path.join(os.getcwd(), "reports", "images")
    #         if os.path.exists(img_dir) is False:
    #             os.mkdir(img_dir)
    #         file_path = os.path.join(img_dir, get_timestamp() + ".png")
    #
    #     if len(kwargs) == 0:
    #         log.info(f"📷️  screenshot -> ({file_path}).")
    #         Seldom.driver.save_screenshot(file_path)
    #     else:
    #         log.info(f"📷️  element screenshot -> ({file_path}).")
    #         u2_elem = U2Element(**kwargs)
    #         elem = u2_elem.get_elements(index)
    #         elem.screenshot(file_path)
    #
    # def screenshots(self) -> None:
    #     """
    #     Saves a screenshots of the current window to HTML report.
    #
    #     Usage:
    #         self.screenshots()
    #     """
    #     image = self.d.screenshot()
    #     if Seldom.debug is True:
    #         img_dir = os.path.join(os.getcwd(), "reports", "images")
    #         if os.path.exists(img_dir) is False:
    #             os.mkdir(img_dir)
    #         file_path = os.path.join(img_dir, get_timestamp() + ".png")
    #         log.info(f"📷️  screenshot -> ({file_path}).")
    #         Seldom.driver.save_screenshot(file_path)
    #     else:
    #         log.info("📷️  screenshot -> HTML report.")
    #         self.images.append(Seldom.driver.get_screenshot_as_base64())
    @staticmethod
    def save_img_report(image_as_base64):
        AppConfig.REPORT_IMAGE.extend(image_as_base64)

    @staticmethod
    def write_log_u2(path):
        """把Android日志写入本地"""
        if not os.path.exists(path):
            open(path, "w").close()
        Seldom.driver.shell('logcat -c')
        cmd = Seldom.driver.shell(f"logcat", stream=True)
        log_list = []
        for line in cmd.iter_lines():
            try:
                log_list.append(line.decode('utf-8'))
            except Exception as e:
                log.error(f'Error in write_log: {e}')
            if not AppConfig.log:
                break
        if not AppConfig.log:
            cmd.close()
        with open(path, "w") as f:
            for item in log_list:
                try:
                    f.write(item + "\n")
                except Exception as e:
                    log.error(f'Error in write_log：{e}')

    @staticmethod
    def get_elements_u2(**kwargs):
        """
        Get a set of elements

        Usage:
        ret = self.get_elements(css="#el")
        print(len(ret))
        """
        u2_elem = U2Element(**kwargs)
        elems = u2_elem.get_elements(empty=True)
        if len(elems) == 0:
            log.warning(f"{u2_elem.warn}.")
        else:
            log.info(f"✅ {u2_elem.info}.")
        return elems

    @staticmethod
    def get_element_u2(index: int = 0, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index)
        log.info(f"✅ {u2_elem.info}.")
        return elem

    def press(self, key: str):
        """
        keyboard
        :param key: keyword name
        press_key("HOME")
        """
        log.info(f'press key "{key}"')
        keycode = keycodes.get(key)
        Seldom.driver.press(keycode)
        return self

    def back(self):
        """go back"""
        log.info("go back")
        Seldom.driver.press(keycodes.get('back'))
        return self

    def home(self):
        """press home"""
        log.info("press home")
        Seldom.driver.press(keycodes.get('home'))
        return self

    def size(self) -> dict:
        """
        return screen resolution.
        """
        size = Seldom.driver.window_size()
        log.info(f"screen resolution: {size}")
        return size

    def tap(self, x: int, y: int) -> None:
        """
        Tap on the coordinates
        :param x: x coordinates
        :param y: y coordinates
        :return:
        """
        log.info(f"top x={x},y={y}.")
        Seldom.driver.click(x=x, y=y)

    def swipe_up(self, times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.9,
                 end: float = 0.1) -> None:
        """
        swipe up
        """
        log.info(f"swipe up {times} times")

        if upper is True:
            start = (start / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end)
            time.sleep(1)

    # def swipe_up_find(self):
    #     swipe_times = 0
    #     while self.wait(element, timeout=1.0) is False:
    #         self.d.swipe_ext(direction, scale=0.9)
    #         swipe_times += 1
    #         if swipe_times > 15:
    #             log.error(f'❗未找到元素：{element["element"]}')
    #             raise ValueError(f'❗未找到元素：{element["element"]}')
    #     log.info(f'✅{direction}滑动屏幕寻找元素')

    def swipe_down(self, times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.1,
                   end: float = 0.9) -> None:
        """
        swipe down
        """
        log.info(f"swipe down {times} times")

        if upper is True:
            end = (end / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end)
            time.sleep(1)


u2 = U2Driver()
