import os
import time
import contextlib
import io
import socket
import threading
import imageio
import tidevice
from seldom.logging import log
from seldom.logging.exceptions import NotFindElementError
from seldom.running.config import Seldom, AppConfig

__all__ = ["WDADriver", "WDAElement", "make_screenrecord", "wda_"]

keycodes = {
    'HOME': 'home',
    'BACK': 'back',
    'LEFT': 'left',
    'ENTER': 'enter',
}

LOCATOR_LIST = {
    'id': "id",
    'name': "name",
    'xpath': "xpath",
    'text': "text",
    'className': "className",
    'value': "value",
    'label': "label"
}


class WDAObj:
    c = None  # device
    t = tidevice.Device()
    t.create_inner_connection()
    s = None  # session
    e = None  # element


class SocketBuffer:
    """
    Since I can't find a lib that can buffer socket read and write, so I write a one
    copy过来的方法：SocketBuffer 类是一个用于缓冲套接字读写操作的自定义实用工具类。
    它对原始套接字执行的操作进行封装，以便更方便地从套接字中读取数据或向套接字发送数据。
    """

    def __init__(self, sock: socket.socket):
        self._sock = sock
        self._buf = bytearray()

    def _drain(self):
        _data = self._sock.recv(1024)
        if _data is None:
            raise IOError("socket closed")
        self._buf.extend(_data)
        return len(_data)

    def read_until(self, delimeter: bytes) -> bytes:
        """ return without delimeter """
        while True:
            index = self._buf.find(delimeter)
            if index != -1:
                _return = self._buf[:index]
                self._buf = self._buf[index + len(delimeter):]
                return _return
            self._drain()

    def read_bytes(self, length: int) -> bytes:
        while length > len(self._buf):
            self._drain()

        _return, self._buf = self._buf[:length], self._buf[length:]
        return _return

    def write(self, data: bytes):
        return self._sock.sendall(data)


class WDAElement:
    """facebook-wda element API"""

    def __init__(self, **kwargs) -> None:
        if not kwargs:
            raise ValueError("Please specify a locator")
        self.desc = None
        self.kwargs = kwargs
        for by, value in list(self.kwargs.items()):
            if LOCATOR_LIST.get(by) is None:
                setattr(self, by, value)
                del self.kwargs[by]
                # log.trace(f'del element kwargs -> {by}:{value}')
        self.find_elem_info = None
        self.find_elem_warn = None

    def get_elements(self, index: int = 0, visible: bool = True, empty: bool = False, timeout: float = None):
        try:
            if not self.desc:
                self.desc = self.kwargs
            if timeout:
                wda_.implicitly_wait(timeout)
            WDAObj.e = WDAObj.s(**self.kwargs, visible=visible, index=index).get()
            if timeout:
                wda_.implicitly_wait(Seldom.timeout)
        except Exception as e:
            if empty is False:
                raise NotFindElementError(f"❌ Find element error: {self.desc} ---> {e}")
            else:
                return []
        self.find_elem_info = f"Find element: {self.desc}."
        return WDAObj.e

    @property
    def info(self):
        """return element info"""
        return self.find_elem_info

    @property
    def warn(self):
        """return element warn"""
        return self.find_elem_warn


class WDADriver:
    """facebook-wda driver"""

    def __init__(self):
        WDAObj.c = Seldom.driver

    @staticmethod
    def implicitly_wait(timeout: float = None):
        """set facebook-wda implicitly wait"""
        if not timeout:
            timeout = Seldom.timeout
        WDAObj.s.implicitly_wait(timeout)
        log.info(f'Set facebook-wda Driver implicitly wait ---> {timeout}s')

    def install_app_wda(self, app_path: str):
        """Install the application found at `app_path` on the device.

        Args:
            app_path: the local or remote path to the application to install

        """
        os.system(f'tidevice --udid {Seldom.app_info.get("udid")} install {app_path}')
        log.info(f'Install APP path ---> {app_path}')
        return self

    def remove_app_wda(self, package_name: str = None):
        """Remove the specified application from the device.

        Args:
            package_name: the application id to be removed

        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        os.system(f'tidevice uninstall {package_name}')
        log.info(f'Remove APP ---> {package_name}')
        return self

    def launch_app_wda(self, package_name: str = None, stop: bool = False):
        """Start on the device the application specified in the desired capabilities."""
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        if stop:
            Seldom.driver.session().app_terminate(package_name)
        log.info(f'Launch APP ---> {package_name} STOP={stop}')
        WDAObj.s = Seldom.driver.session(package_name)

        return self

    def close_app_wda(self, package_name: str = None):
        """Stop the running application, specified in the desired capabilities, on
        the device.

        Returns:
            Union['WebDriver', 'Applications']: Self instance
        """
        if not package_name:
            package_name = Seldom.app_info.get('appPackage')
        log.info(f'Close APP ---> {package_name}')
        Seldom.driver.session().app_terminate(package_name)

        return self

    def set_text_wda(self, text: str, clear: bool = False, enter: bool = False, click: bool = False, index: int = 0,
                     **kwargs) -> None:
        """
        Operation input box.

        Usage:
            self.type(css="#el", text="selenium")
        """
        if clear is True:
            self.clear_text_wda(index, **kwargs)
        if click is True:
            self.click_wda(index, **kwargs)
            time.sleep(0.5)
        wda_elem = WDAElement(**kwargs)
        elem = wda_elem.get_elements(index)
        log.info(f"✅ {wda_elem.info} -> input '{text}'.")
        elem.set_text(text)
        if enter is True:
            elem.press('enter')

    @staticmethod
    def clear_text_wda(index: int = 0, **kwargs) -> None:
        """
        Clear the contents of the input box.

        Usage:
            self.clear(css="#el")
        """
        wda_elem = WDAElement(**kwargs)
        elem = wda_elem.get_elements(index=index)
        log.info(f"✅ {wda_elem.info} -> clear input.")
        elem.clear_text()

    @staticmethod
    def click_wda(index: int = 0, **kwargs) -> None:
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
            self.click(css="#el")
        """
        wda_elem = WDAElement(**kwargs)
        elem = wda_elem.get_elements(index=index)
        log.info(f"✅ {wda_elem.info} -> click.")
        elem.click()

    @staticmethod
    def click_text_wda(text: str, index: int = 0) -> None:
        """
        Click the element by the text

        Usage:
            self.click_text("新闻")
        """
        wda_elem = WDAElement(text=text)
        elem = wda_elem.get_elements(index)
        log.info(f"✅ {wda_elem.info} -> click text.")
        elem.click()

    @staticmethod
    def get_text_wda(index: int = 0, **kwargs) -> str:
        """
        Get element text information.

        Usage:
            self.get_text(css="#el")
        """
        wda_elem = WDAElement(**kwargs)
        elem = wda_elem.get_elements(index)
        text = elem.get_text()
        log.info(f"✅ {wda_elem.info} -> get text: {text}.")
        return text

    # @staticmethod
    # def get_display_u2(index: int = 0, **kwargs) -> bool:
    #     """
    #     Gets the element to display,The return result is true or false.
    #
    #     Usage:
    #         self.get_display(css="#el")
    #     """
    #     if 'elem' in kwargs:
    #         wda_elem = kwargs['elem']
    #     else:
    #         wda_elem = WDAElement(**kwargs)
    #     elem = wda_elem.get_elements(index, empty=True)
    #     if not elem:
    #         return False
    #     else:
    #         result = elem.exists
    #         log.info(f"✅ {wda_elem.info} -> element is display: {result}.")
    #         return result

    @staticmethod
    def wait_wda(timeout: float = 5, index: int = 0, noLog=False, **kwargs) -> bool:
        """
        Implicitly wait element on the page.
        """
        wda_elem = WDAElement(**kwargs)

        timeout_backups = Seldom.timeout
        Seldom.timeout = timeout
        if noLog is not True:
            log.info(f"⌛️ wait {wda_elem.desc} to exist: {timeout}s.")
        try:
            wda_elem.get_elements(index, empty=kwargs.get('empty', False)).wait(timeout=timeout)
            result = True
        except:
            if noLog is not True:
                log.info(f"❌Element {wda_elem.desc} not exist")
            result = False
        Seldom.timeout = timeout_backups
        return result

    def wait_gone_wda(self, timeout: int = None, index: int = 0, **kwargs) -> bool:
        """
        等待元素消失

        """
        if not timeout:
            timeout = Seldom.timeout
        wda_elem = WDAElement(**kwargs)
        log.info(f"⌛ wait {wda_elem.desc} gone: timeout={timeout}s.")
        result = wda_elem.get_elements(index, empty=kwargs.get('empty', False)).wait_gone(timeout=timeout)
        if not result:
            log.warning(f'⌛ wait {wda_elem.desc} gone failed.')
            # self.save_screenshot(report=True)
        return result


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
    #         log.info(f"📷️ screenshot -> ({file_path}).")
    #         Seldom.driver.save_screenshot(file_path)
    #     else:
    #         log.info(f"📷️ element screenshot -> ({file_path}).")
    #         wda_elem = WDAElement(**kwargs)
    #         elem = wda_elem.get_elements(index)
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
    #         log.info(f"📷️ screenshot -> ({file_path}).")
    #         Seldom.driver.save_screenshot(file_path)
    #     else:
    #         log.info("📷️ screenshot -> HTML report.")
    #         self.images.append(Seldom.driver.get_screenshot_as_base64())

    @staticmethod
    def get_element_wda(index: int = 0, **kwargs):
        """
        Get a set of elements

        Usage:
        elem = self.get_element(index=1, css="#el")
        elem.click()
        """
        wda_elem = WDAElement(**kwargs)
        elem = wda_elem.get_elements(index)
        log.info(f"✅ {wda_elem.info}.")
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

    # def size(self) -> dict:
    #     """
    #     return screen resolution.
    #     """
    #     size = Seldom.driver.window_size()
    #     log.info(f"screen resolution: {size}")
    #     return size
    @staticmethod
    def tap(x: int, y: int) -> None:
        """
        Tap on the coordinates
        :param x: x coordinates
        :param y: y coordinates
        :return:
        """
        log.info(f"tap x={x},y={y}.")
        Seldom.driver.click(x=x, y=y)

    @staticmethod
    def swipe_up_wda(times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.8,
                     end: float = 0.1) -> None:
        """
        swipe up
        """
        log.info(f"swipe up {times} times")

        if upper is True:
            start = (start / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end, 0.5)
            if times != 1:
                time.sleep(1)

    def swipe_up_find_wda(self, times: int = 15, upper: bool = False, index: int = 0, **kwargs):

        swipe_times = 0
        wda_elem = WDAElement(**kwargs)
        log.info(f'Swipe to find ---> {wda_elem.desc}')
        while not wda_elem.get_elements(index=index, empty=True, timeout=0.5):
            self.swipe_up_wda(upper=upper)
            swipe_times += 1
            if swipe_times > times:
                raise NotFindElementError(f"❌ Find element error: swipe {times} times no find ---> {wda_elem.desc}")

    @staticmethod
    def swipe_down_wda(times: int = 1, upper: bool = False, width: float = 0.5, start: float = 0.1,
                       end: float = 0.8) -> None:
        """
        swipe down
        """
        log.info(f"swipe down {times} times")

        if upper is True:
            end = (end / 2)

        for _ in range(times):
            Seldom.driver.swipe(width, start, width, end, 0.5)
            if times != 1:
                time.sleep(1)

    @staticmethod
    def func_wda(func_name, **kwargs):
        function = getattr(Seldom.driver, func_name)
        return function(**kwargs)


wda_ = WDADriver()


@contextlib.contextmanager
def make_screenrecord(c=None, t=None, output_video_path='record.mp4', fps=AppConfig.FPS):
    """
    iOS录屏上下文管理器
    """
    if c is None:
        c = WDAObj.c = Seldom.driver
    if t is None:
        t = WDAObj.t
    _old_fps = c.appium_settings()['mjpegServerFramerate']
    _fps = fps
    c.appium_settings({"mjpegServerFramerate": _fps})

    # Read image from WDA mjpeg server
    pconn = t.create_inner_connection(9100)  # default WDA mjpeg server port
    sock = pconn.get_socket()
    buf = SocketBuffer(sock)
    buf.write(b"GET / HTTP/1.0\r\nHost: localhost\r\n\r\n")
    buf.read_until(b'\r\n\r\n')
    log.info(f"📷️ start_recording -> ({output_video_path}).")

    wr = imageio.get_writer(output_video_path, fps=_fps)

    def _drain(stop_event, done_event):
        while not stop_event.is_set():
            # read http header
            length = None
            while True:
                line = buf.read_until(b'\r\n')
                if line.startswith(b"Content-Length"):
                    length = int(line.decode('utf-8').split(": ")[1])
                    break
            while True:
                if buf.read_until(b'\r\n') == b'':
                    break

            imdata = buf.read_bytes(length)
            im = imageio.imread(io.BytesIO(imdata))
            wr.append_data(im)
        done_event.set()

    stop_event = threading.Event()
    done_event = threading.Event()
    threading.Thread(name="screenrecord", target=_drain, args=(stop_event, done_event), daemon=True).start()
    yield
    stop_event.set()
    done_event.wait()
    wr.close()
    c.appium_settings({"mjpegServerFramerate": _old_fps})
    log.info(f"📷️ record down.")
