import seldom
from appium.options.android import UiAutomator2Options


class TestBBS(seldom.TestCase):
    """
    Test Flyme BBS
    """

    def test_bbs_search(self):
        """
        test flyme bbs search
        """
        self.sleep(5)
        self.click(id_="com.meizu.flyme.flymebbs:id/nw")
        self.type(id_="com.meizu.flyme.flymebbs:id/nw", text="flyme")
        self.click(id_="com.meizu.flyme.flymebbs:id/o1")
        self.sleep(2)
        elems = self.get_elements(id_="com.meizu.flyme.flymebbs:id/a29")
        for elem in elems:
            self.assertIn("flyme", elem.text.lower())


if __name__ == '__main__':
    capabilities = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(app_server="http://127.0.0.1:4723", app_info=options, debug=True)
