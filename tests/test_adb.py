import time
from seldom.utils.adbutils import ADBUtils

import unittest


class ADBUtilsTest(unittest.TestCase):

    def setUp(self):
        self.adb = ADBUtils()

    def test_devices(self):
        # 自动刷新并获取所有设备
        devices = self.adb.refresh_devices()
        print("当前连接设备:", devices)
        # 设置默认设备
        if devices:
            self.adb.set_default_device(devices[0][0])

    def test_app_lunch_and_close(self):
        # 应用操作
        package = "com.microsoft.bing"
        if self.adb.launch_app(package):
            print(f"成功启动 {package}")
            time.sleep(5)
            if self.adb.close_app(package):
                print(f"成功关闭 {package}")

    def test_app_info(self):
        # 获取信息
        app_info = self.adb.get_app_info()
        for info in app_info:
            print(info['package'], info["activity"])


if __name__ == '__main__':
    unittest.main()
