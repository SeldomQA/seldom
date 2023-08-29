"""
uiautomator2 driver API
"""
import base64
import os
import time
from typing import Tuple
from seldom.testdata import get_word, get_now_datetime
from seldom.logging import log
from seldom.running.config import Seldom, AppConfig
from seldom.logging.exceptions import NotFindElementError

__all__ = ["U2Driver", "U2Element", "u2"]

keycodes = {
    'HOME': 'home',
    'BACK': 'back',
    'LEFT': 'left',
    'ENTER': 'enter',
}

LOCATOR_LIST = {
    'resourceId': "resourceId",
    'name': "name",
    'xpath': "xpath",
    'text': 'text',
    'className': "className",
}


class U2Element:
    """uiautomator2 element API"""

    def __init__(self, **kwargs) -> None:
        if not kwargs:
            raise ValueError("Please specify a locator.")
        self.desc = None
        self.kwargs = kwargs
        for by, value in list(self.kwargs.items()):
            if LOCATOR_LIST.get(by) is None:
                setattr(self, by, value)
                del self.kwargs[by]
        self.find_elem_info = None
        self.find_elem_warn = None
        self.find_elem_warn = None

    def get_elements(self, index: int = None, empty: bool = False, timeout: float = None):
        try:
            if self.desc:
                self.desc = f'desc={self.desc}'
            else:
                self.desc = ', '.join([f"{k}={v}" for k, v in self.kwargs.items()])
            if timeout:
                u2.implicitly_wait(timeout=timeout, noLog=True)
            if index:
                if 'xpath' in self.kwargs:
                    elems = Seldom.driver.xpath(**self.kwargs).all()[index]
                else:
                    elems = Seldom.driver(**self.kwargs)[index]
            else:
                if 'xpath' in self.kwargs:
                    elems = Seldom.driver.xpath(**self.kwargs)
                else:
                    elems = Seldom.driver(**self.kwargs)
            if timeout:
                u2.implicitly_wait(timeout=Seldom.timeout, noLog=True)
        except Exception as e:
            if empty is False:
                raise NotFindElementError(f"❌ Find error: {self.desc} -> {e}.")
            else:
                return []
        self.find_elem_info = f"Find element: {self.desc}."
        return elems

    @property
    def info(self):
        """return element info"""
        return self.find_elem_info

    @property
    def warn(self):
        """return element warn"""
        return self.find_elem_warn


class U2Driver:
    """uiautomator2 driver"""

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
    def implicitly_wait(timeout: float = None, noLog: bool = False) -> None:
        """set uiautomator2 Driver implicitly wait"""
        if not timeout:
            timeout = Seldom.timeout
        Seldom.driver.implicitly_wait(timeout)
        if not noLog:
            log.info(f'✅ Set implicitly wait -> {timeout}s.')

    @staticmethod
    def install_app_u2(app_path: str):
        """Install the application found at `app_path` on the device.

        Args:
            app_path: the local or remote path to the application to install

        """
        os.system(f'adb install -g {app_path}')
        log.info(f'✅ {app_path} -> Install APP.')

    @staticmethod
    def remove_app_u2(package_name: str = None):
        """Remove the specified application from the device.

        Args:
            package_name: the application id to be removed

        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        Seldom.driver.app_uninstall(package_name)
        log.info(f'✅ {package_name} -> Remove APP.')

    @staticmethod
    def launch_app_u2(package_name: str = None, stop: bool = False):
        """Start on the device the application specified in the desired capabilities.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        log.info(f'✅ {package_name} -> Launch APP, STOP={stop}.')
        Seldom.driver.app_start(package_name=package_name, stop=stop)

    @staticmethod
    def close_app_u2(package_name: str = None):
        """Stop the running application, specified in the desired capabilities, on
        the device.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        log.info(f'✅ {package_name} -> Close APP.')
        Seldom.driver.app_stop(package_name)

    @staticmethod
    def close_app_all_u2():
        Seldom.driver.app_stop_all()
        log.info('✅ Close all APP.')

    @staticmethod
    def clear_app_u2(package_name: str = None) -> None:
        """Resets the current application on the device.

        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        Seldom.driver.app_clear(package_name)
        log.info(f'✅ {package_name} -> Clear APP.')

    @staticmethod
    def wait_app_u2(package_name: str = None) -> int:
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        log.info(f'✅ {package_name} -> wait APP run.')
        pid = Seldom.driver.app_wait(package_name)
        return pid

    def set_text_u2(self, text: str, clear: bool = False, enter: bool = False, click: bool = False, index: int = None,
                    **kwargs) -> None:
        """
        Operation input box.

        Usage:
            self.set_text_u2(css="#el", text="selenium")
        """
        if clear is True:
            self.clear_text_u2(index, **kwargs)
        if click is True:
            self.click_u2(index, **kwargs)
            time.sleep(0.5)
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index)
        log.info(f"✅ {u2_elem.info} -> input [{text}].")
        elem.set_text(text)
        if enter is True:
            elem.press('enter')

    @staticmethod
    def clear_text_u2(index: int = None, **kwargs) -> None:
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
    def click_u2(index: int = None, **kwargs) -> None:
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
    def click_text_u2(text: str, index: int = None) -> None:
        """
        Click the element by the link text

        Usage:
            self.click_text("新闻")
        """
        u2_elem = U2Element(text=text)
        elem = u2_elem.get_elements(index=index)
        log.info(f"✅ {u2_elem.info} -> click text.")
        elem.click()

    @staticmethod
    def get_text_u2(index: int = None, **kwargs) -> str:
        """
        Get element text information.

        Usage:
            self.get_text(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index)
        text = elem.get_text()
        log.info(f"✅ {u2_elem.info} -> text: {text}.")
        return text

    @staticmethod
    def get_display_u2(index: int = None, timeout: float = 1.0, **kwargs) -> bool:
        """
        Gets the element to display,The return result is true or false.

        Usage:
            self.get_display_u2(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index, empty=True, timeout=timeout)
        if not elem:
            return False
        else:
            result = elem.exists
            log.info(f"✅ {u2_elem.info} -> display: {result}.")
            return result

    def wait_u2(self, timeout: int = Seldom.timeout, index: int = None, noLog: bool = False, **kwargs) -> bool:
        """
        Implicitly wait element on the page.
        """
        u2_elem = U2Element(**kwargs)
        timeout_backups = Seldom.timeout
        Seldom.timeout = timeout
        if noLog is not True:
            log.info(f"⌛  {u2_elem.desc} -> wait element: {timeout}s.")
        try:
            u2_elem.get_elements(empty=kwargs.get('empty', False), index=index).wait(timeout=timeout)
            result = True
        except:
            if noLog is False:
                log.warning(f"❌ {u2_elem.desc} -> not exist.")
            self.save_screenshot(report=True)
            result = False
        Seldom.timeout = timeout_backups
        return result

    def wait_gone_u2(self, timeout: int = None, index: int = None, **kwargs) -> bool:
        """
        等待元素消失

        """
        if not timeout:
            timeout = Seldom.timeout
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(empty=kwargs.get('empty', False), index=index)
        log.info(f"⌛  {u2_elem.desc} -> wait gone: {timeout}s.")
        result = elem.wait_gone(timeout=timeout)
        if not result:
            log.warning(f'❌ {u2_elem.desc} -> wait gone failed.')
            self.save_screenshot(report=True)
        return result

    def wait_stable(self, interval: float = 1.0, retry: int = 10, timeout: float = 20.0) -> bool:
        deadline = time.time() + timeout
        while time.time() < deadline:
            for _ in range(retry):
                first_snapshot = Seldom.driver.dump_hierarchy()
                time.sleep(interval)
                second_snapshot = Seldom.driver.dump_hierarchy()
                if first_snapshot == second_snapshot:
                    return True
                else:
                    log.info('⌛  Wait page stable...')
        self.save_screenshot(report=True)
        raise EnvironmentError("Unstable page")

    @staticmethod
    def start_recording_u2(output: str = None, fps: int = None) -> None:
        if output is None:
            log.warning('Please set the storage location for screen recording')
            output = 'record.mp4'
        if fps is None:
            fps = AppConfig.FPS
        log.info(f"📷️ start_recording -> ({output}).")
        Seldom.driver.screenrecord(output, fps=fps)

    @staticmethod
    def stop_recording_u2() -> None:
        log.info(f"📷️ record down.")
        Seldom.driver.screenrecord.stop()

    @staticmethod
    def save_screenshot(file_path: str = None, report: bool = False) -> None:
        """
        Saves a screenshots of the current window to a PNG image file.

        Usage:
            self.save_screenshot('/Screenshots/foo.png')
        """
        screenshot = Seldom.driver.screenshot()
        if file_path is None:
            file_path = os.path.join(AppConfig.PERF_RUN_FOLDER, f"{get_now_datetime(strftime=True)}.png")

        log.info(f"📷️ screenshot -> ({file_path}).")
        screenshot.save(file_path)
        if report:
            with open(file_path, "rb") as image_file:
                image_bytes = image_file.read()
                base64_data = base64.b64encode(image_bytes)
                base64_string = base64_data.decode("utf-8")
            AppConfig.REPORT_IMAGE.extend([base64_string])

    @staticmethod
    def write_log_u2(save_path: str = None) -> None:
        """
        把Android日志写入本地

        Usage:
        self.write_log_u2('/Log/log.txt')
        """
        if not save_path:
            save_path = os.path.join(AppConfig.PERF_RUN_FOLDER, f"{get_now_datetime(strftime=True)}.txt")
        if not os.path.exists(save_path):
            open(save_path, "w").close()
        try:
            Seldom.driver.shell('logcat -c')
            cmd = Seldom.driver.shell(f"logcat", stream=True)
            log_list = []
            for line in cmd.iter_lines():
                try:
                    log_list.append(line.decode('utf-8'))
                except Exception as e:
                    log.error(f'Error in write_log: {e}.')
                if not AppConfig.log:
                    break
            if not AppConfig.log:
                cmd.close()
            with open(save_path, "w") as f:
                for item in log_list:
                    try:
                        f.write(item + "\n")
                    except Exception as e:
                        log.warning(f'Error in write_log: [{e}], but skip!')
            log.info(f'Log saved in {save_path}')
        except Exception as e:
            raise Exception(f'❌ Error in write_log: {e}.')

    @staticmethod
    def get_elements_u2(**kwargs):
        """
        Get a set of elements

        Usage:
        ret = self.get_elements(css="#el")
        """
        u2_elem = U2Element(**kwargs)
        elems = u2_elem.get_elements(empty=True)
        if len(elems) == 0:
            log.warning(f"{u2_elem.warn}.")
        else:
            log.info(f"✅ {u2_elem.info}.")
        return elems

    @staticmethod
    def get_element_u2(index: int = None, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        u2_elem = U2Element(**kwargs)
        elem = u2_elem.get_elements(index=index)
        log.info(f"✅ {u2_elem.info}.")
        return elem

    @staticmethod
    def press(key: str) -> None:
        """
        keyboard
        :param key: keyword name
        press_key("HOME")
        """
        log.info(f'✅ Press key "{key}".')
        keycode = keycodes.get(key)
        Seldom.driver.press(keycode)

    @staticmethod
    def back() -> None:
        """go back"""
        log.info("✅ Go back.")
        Seldom.driver.press(keycodes.get('back'))

    @staticmethod
    def home() -> None:
        """press home"""
        log.info("✅ Press home.")
        Seldom.driver.press(keycodes.get('home'))

    @staticmethod
    def size() -> dict:
        """
        return screen resolution.
        """
        size = Seldom.driver.window_size()
        log.info(f"✅ Screen resolution: {size}.")
        return size

    @staticmethod
    def tap(x: int, y: int) -> None:
        """
        Tap on the coordinates
        :param x: x coordinates
        :param y: y coordinates
        :return:
        """
        log.info(f"✅ tap x={x},y={y}.")
        Seldom.driver.click(x=x, y=y)

    @staticmethod
    def swipe_up(times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.9,
                 end: float = 0.1) -> None:
        log.info(f"✅ swipe up {times} times.")

        if upper is True:
            start = (start / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end)
            if times != 1:
                time.sleep(1)

    def swipe_up_find_u2(self, times: int = 15, upper: bool = False, index: int = None, **kwargs) -> None:
        """
        swipe up to find element.

        Usage:
        self.swipe_up_find_u2(elem=ElemObj)
        self.swipe_up_find_u2(text='login')
        """

        swipe_times = 0
        u2_elem = U2Element(**kwargs)
        log.info(f'✅ {u2_elem.desc} -> swipe to find.')
        while not self.get_display_u2(**kwargs):
            self.swipe_up(upper=upper)
            swipe_times += 1
            if swipe_times > times:
                raise NotFindElementError(f"❌ Find element error: swipe {times} times no find ---> {u2_elem.desc}")

    @staticmethod
    def swipe_down_u2(times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.1,
                      end: float = 0.9) -> None:
        """
        swipe down
        """
        log.info(f"swipe down {times} times")

        if upper is True:
            end = (end / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end)
            if times != 1:
                time.sleep(1)

    @staticmethod
    def swipe_points_u2(start_point: Tuple[float, float], end_point: Tuple[float, float], duration: int = 0.1):
        Seldom.driver.swipe_points([start_point, end_point], duration=duration)
        log.info(f'✅ Swipe from {start_point} to {end_point}.')

    @staticmethod
    def screen_on_u2() -> None:
        if not Seldom.driver.info.get('screenOn'):
            Seldom.driver.screen_on()
            log.info('✅ Screen ON.')

    @staticmethod
    def open_url_u2(url) -> None:
        Seldom.driver.open_url(url)
        log.info(f'✅ Open {url}.')

    @staticmethod
    def icon_save_u2(save_path: str = None, package_name: str = None) -> str:
        """
        save app icon
        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        if not save_path:
            save_path = os.path.join(AppConfig.PERF_OUTPUT_FOLDER, f'{package_name}.png')
        Seldom.driver.app_icon(package_name).save(save_path)
        log.info(f'✅ Icon saved: {save_path}.')
        return save_path

    @staticmethod
    def app_info_u2(package_name: str = None) -> str:
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        info = Seldom.driver.app_info(package_name)
        log.info(f'✅ {package_name} -> info: {info}.')
        return info

    @staticmethod
    def func_u2(func_name, **kwargs):
        try:
            function = getattr(Seldom.driver, func_name)
            return function(**kwargs)
        except Exception as e:
            raise ValueError(f'❌ {func_name} is error ---> {e}.')

    @staticmethod
    def register_watch(args: list, name: str = None) -> str:
        """when all element exist than click"""
        if not name:
            name = get_word()
        watcher = Seldom.driver.watcher(name)
        value_list = []
        for elem in args:
            ele = U2Element(**elem)
            by, value = list(ele.kwargs.items())[0]
            if by == 'xpath':
                watcher.when(value)
                value_list.append(value)
            elif by == 'text':
                watcher.when(value)
                value_list.append(value)
            else:
                log.warning(f'{by}={value} type must between "xpath" and "text".')
        if not value_list:
            raise ValueError(f'Not right element be register!')
        else:
            log.info(f'✅ Register watch: {name}={value_list}')
            watcher.click()
            return name

    def start_watcher(self, args: list = None, name: str = None, time_interval: float = 0.5) -> str:
        name = self.register_watch(name=name, args=args)
        Seldom.driver.watcher.start(time_interval)
        log.info(f'✅ Start watch: {name}.')
        return name

    @staticmethod
    def stop_all_watcher():
        Seldom.driver.watcher.stop()
        log.info(f'✅ Stop all watch.')

    @staticmethod
    def remove_watcher(name: str):
        Seldom.driver.watcher.remove(name)
        log.info(f'✅ Remove watch ：{name}.')


u2 = U2Driver()
