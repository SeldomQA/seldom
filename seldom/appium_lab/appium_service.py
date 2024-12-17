from appium.webdriver.appium_service import AppiumService as OriginalServer


class AppiumService(OriginalServer):
    """
    appium service
    """

    def __init__(self, addr: str = "127.0.0.1", port: str = "4723"):
        super().__init__()
        self.addr = addr
        self.port = port

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

        args = ['--address', self.addr, '-p', self.port]
        self.start(args=args, **kwargs)


if __name__ == '__main__':
    service = AppiumService()
    service.start_service()
