"""
playwright demo
doc: https://playwright.dev
"""
import seldom
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class Playwright(seldom.TestCase):

    def start(self):
        self.p = sync_playwright().start()
        self.chromium = self.p.chromium.launch(headless=False)
        self.page = self.chromium.new_page()

    def end(self):
        self.chromium.close()
        self.p.stop()

    def test_playwright_start(self):
        """
        test playwright index page
        """
        self.page.goto("http://playwright.dev")
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

        get_started = self.page.locator('text=Get Started')
        expect(get_started).to_have_attribute('href', '/docs/intro')
        get_started.click()

        expect(self.page).to_have_url('http://playwright.dev/docs/intro')
        # playwright 实现截图
        screenshot_bytes = self.page.screenshot()
        self.screenshots(image=screenshot_bytes)

    def test_playwright_todo(self):
        """
        test playwright todoMVC
        """
        self.page.goto("https://demo.playwright.dev/todomvc/#/")
        new_todo = self.page.locator(".new-todo")
        new_todo.fill("sleep")
        new_todo.press("Enter")
        new_todo.fill("code")
        new_todo.press("Enter")
        new_todo.fill("eat")
        new_todo.press("Enter")
        self.page.locator('li').filter(has_text='code').get_by_label('Toggle Todo').check()
        self.page.locator('li').filter(has_text='sleep').get_by_label('Toggle Todo').check()
        self.page.locator('li').filter(has_text='eat').get_by_label('Toggle Todo').check()
        # 截图
        screenshot_bytes = self.page.screenshot()
        self.screenshots(image=screenshot_bytes)


if __name__ == '__main__':
    seldom.main()
