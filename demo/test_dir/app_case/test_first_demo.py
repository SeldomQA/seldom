from appium.options.android import UiAutomator2Options

import seldom
from seldom.appium_lab.keyboard import KeyEvent


class TestBingApp(seldom.TestCase):
    """
    Test Bing APP
    """

    def start(self):
        self.ke = KeyEvent(self.driver)

    def test_bing_search(self):
        """
        test bing bbs search
        """
        self.sleep(2)
        self.click(id_="com.microsoft.bing:id/sa_hp_header_search_box")
        self.type(id_="com.microsoft.bing:id/sapphire_search_header_input", text="seldom")
        self.ke.press_key("ENTER")
        self.sleep(1)
        elem = self.get_element(xpath='//android.widget.TextView[@resource-id="count"]')
        self.assertIn("个结果", elem.text.lower())


if __name__ == '__main__':
    capabilities = {
        'deviceName': 'ELS-AN00',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'appPackage': 'com.microsoft.bing',
        'appActivity': 'com.microsoft.sapphire.app.main.MainSapphireActivity',
        'noReset': True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(app_server="http://127.0.0.1:4723", app_info=options, debug=True)
