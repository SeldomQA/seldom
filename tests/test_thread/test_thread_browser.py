import time
import seldom
from seldom.extend_lib import threads


class BingTest(seldom.TestCase):
    """Bing search test case"""

    def test_case(self):
        """a simple test case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.assertInTitle("seldom")


if __name__ == '__main__':

    @threads(3)
    def run_case(browser):
        seldom.main(browser=browser)


    browser = ["gc", "ff", "edge"]
    for b in browser:
        run_case(b)
        time.sleep(1)
