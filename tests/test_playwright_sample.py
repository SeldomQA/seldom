"""
需要安装 playwright: https://playwright.dev/
> pip install playwright
"""
import seldom
import base64
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class Playwright(seldom.TestCase):

    def start(self):
        p = sync_playwright().start()
        self.browser = p.chromium.launch()
        self.page = self.browser.new_page()

    def end(self):
        self.browser.close()

    def test_start(self):
        page = self.page
        page.goto("https://playwright.dev")

        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

        get_started = page.locator('text=Get Started')
        expect(get_started).to_have_attribute('href', '/docs/intro')

        # 截图保存到报告
        screenshot_bytes = page.screenshot()
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
        self.images.append(screenshot_b64)

        get_started.click()

        expect(page).to_have_url('https://playwright.dev/docs/intro')


if __name__ == '__main__':
    seldom.main()
