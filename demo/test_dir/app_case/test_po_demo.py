from appium.options.android import UiAutomator2Options
from poium import Page, Element

import seldom
from seldom.appium_lab.keyboard import KeyEvent


class BBSPage(Page):
    """BBS Page"""
    search_button = Element("id=com.microsoft.bing:id/sa_hp_header_search_box")
    search_input = Element("id=com.microsoft.bing:id/sapphire_search_header_input")
    search_count = Element('//android.widget.TextView[@resource-id="count"]')


class TestBBS(seldom.TestCase):
    """
    Test BBS
    """

    def start(self):
        self.bbs_page = BBSPage(self.driver)
        self.ke = KeyEvent(self.driver)

    def test_bbs(self):
        """
        test bbs search
        """
        self.sleep(2)
        self.bbs_page.search_button.click()
        self.sleep(1)
        self.bbs_page.search_input.send_keys("seldom")
        self.ke.press_key("ENTER")
        self.sleep(1)
        counts = self.bbs_page.search_count
        self.assertIn("个结果", counts.text.lower())


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
