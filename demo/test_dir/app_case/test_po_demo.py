import seldom
from poium import Page, Element, Elements


class BBSPage(Page):
    """BBS Page"""
    search_input = Element(id_="com.meizu.flyme.flymebbs:id/nw")
    search_button = Element(id_="com.meizu.flyme.flymebbs:id/o1")
    search_result = Elements(id_="com.meizu.flyme.flymebbs:id/a29")


class TestBBS(seldom.TestCase):
    """
    Test BBS
    """

    def start(self):
        self.bbs_page = BBSPage(self.driver)

    def test_bbs(self):
        """
        test bbs search
        """
        self.sleep(5)
        self.bbs_page.search_input.click()
        self.bbs_page.search_input.send_keys("flyme")
        self.bbs_page.search_button.click()
        elems = self.bbs_page.search_result
        for title in elems:
            self.assertIn("flyme", title.text.lower())


if __name__ == '__main__':
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    seldom.main(app_info=desired_caps, app_server="http://127.0.0.1:4723", debug=True)
