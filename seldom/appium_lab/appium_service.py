from appium.webdriver.appium_service import AppiumService as OriginalServer


class AppiumService(OriginalServer):

    def __init__(self, addr, port='4723'):
        self.addr = addr
        self.port = port

        super().__init__()

    def start_service(self, **kwargs):
        # args = [
        #     f'-p {self.port}',
        #     # f'-g {self.log_file_path}',
        #     '--session-override',
        #     '--log-timestamp',
        #     '--session-override',
        #     '--local-timezone',
        #     '--allow-insecure chromedriver_autodownload',
        # ]
        args = ['--address', self.addr, '-p', self.port]
        self.start(args=args, **kwargs)


if __name__ == '__main__':
    service = AppiumService('127.0.0.1')
    service.start_service()
