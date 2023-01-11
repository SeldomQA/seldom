"""
需要安装 playwright: https://playwright.dev/
> pip install playwright
"""
import seldom
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
        page.goto("http://playwright.dev")
        print(page.title())
        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

        get_started = page.locator('text=Get Started')
        expect(get_started).to_have_attribute('href', '/docs/intro')
        get_started.click()

        expect(page).to_have_url('http://playwright.dev/docs/intro')


if __name__ == '__main__':
    seldom.main()

