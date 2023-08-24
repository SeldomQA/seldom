import os
import seldom
from seldom.utils.perf import AppPerf, RunType, start_recording
from seldom.wdadriver import WDAElement


class Element:
    edit = WDAElement(label='编辑照片和视频', value='编辑照片和视频')


class TestDemo(seldom.TestCase):
    """
    Test Demo
    """

    @AppPerf(MODE=RunType.DEBUG)
    def test_demo(self):
        """
        test flyme bbs search
        """
        # self.sleep(5)
        self.launch_app_wda()
        start_recording()
        self.sleep(3)
        self.click_wda(elem=Element.edit, index=0)
        self.assertElement(label='最近项目')
        self.sleep(1)


if __name__ == '__main__':
    # uiautomator2 case 配置
    # desired_caps = {
    #     'deviceName': 'f5ede5e3',
    #     'platformName': 'Android',
    #     'appPackage': 'com.magicv.airbrush',
    # }
    desired_caps = {
        'udid': 'bfaaa7b76fe378fb64332ebab762bb36dc77d3c3',
        'platformName': 'iOS',
        'appPackage': 'com.magicv.AirBrush',
    }
    from seldom import AppConfig
    AppConfig.PERF_OUTPUT_FOLDER = os.path.join(os.getcwd(), "reports")
    seldom.main(app_info=desired_caps, debug=True)
