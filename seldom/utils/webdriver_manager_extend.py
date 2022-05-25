"""
https://github.com/SergeyPirogov/webdriver_manager
"""
import os

from webdriver_manager.core.manager import DriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.drivers.chrome import ChromeDriver


class ChromeDriverManager(DriverManager):
    """
    Since Google cannot be used in China, Taobao is used to replace Google
    """

    def __init__(self,
                 version="latest",
                 os_type=None,
                 path=None,
                 name="chromedriver",
                 url="https://registry.npmmirror.com/-/binary/chromedriver",
                 latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                 chrome_type=ChromeType.GOOGLE,
                 cache_valid_range=1,
                 download_manager=None):
        super().__init__(
            path,
            cache_valid_range=cache_valid_range,
            download_manager=download_manager)

        self.driver = ChromeDriver(
            name=name,
            version=version,
            os_type=os_type,
            url=url,
            latest_release_url=latest_release_url,
            chrome_type=chrome_type,
            http_client=self.http_client,
        )

    def install(self):
        driver_path = self._get_driver_path(self.driver)
        os.chmod(driver_path, 0o755)
        return driver_path
