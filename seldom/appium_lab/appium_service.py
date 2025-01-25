import time
from seldom.logging import log
from seldom.utils import file
from appium.webdriver.appium_service import AppiumService as OriginalServer


class AppiumService(OriginalServer):
    """
    appium service
    """

    def __init__(self,
                 addr: str = "127.0.0.1",
                 port: str = "4723",
                 log: str = None,
                 use_plugins: str = None,
                 args: list = []):
        super().__init__()
        self.addr = addr
        self.port = port
        self.log = log
        self.use_plugins = use_plugins
        self.args = args

    def start_service(self, **kwargs) -> None:
        """
        start service
        :param kwargs:

        args = [
            f'-p {self.port}',
            f'-g {self.log_file_path}',
            '--session-override',
            '--log-timestamp',
            '--session-override',
            '--local-timezone',
            '--allow-insecure chromedriver_autodownload',
        ]
        :return:
        """

        start_args = ['--address', self.addr, '--port', self.port]

        if self.log is None:
            now_time = str(time.time()).split(".")[0]
            log_file = file.join(file.dir, f"appium_server_{now_time}.log")
            for param in ["--log", log_file]:
                start_args.append(param)

        if self.use_plugins is not None:
            start_args.append("--use-plugins")
            start_args.append(self.use_plugins)

        for param in self.args:
            start_args.append(param)

        log.info(f"🚀 launch appium server: {start_args}")

        self.start(args=start_args, **kwargs)


if __name__ == '__main__':
    # service = AppiumService()
    service = AppiumService(use_plugins="iamges,ocr", args=["--allow-cors"])
    service.start_service()
