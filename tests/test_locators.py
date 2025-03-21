"""
selenium locators
"""
import seldom
from seldom import Steps


class TestForm(seldom.TestCase):

    def start(self):
        self.test_url = "https://seleniumbase.io/demo_page"
        self.open(self.test_url)

    def test_locator(self):
        """locator"""
        self.type(id_="myTextarea", text="id", clear=True)
        self.type(name="textareaName", text="name", clear=True)
        self.type(class_name="textareaClass", text="class name", clear=True)
        self.type(css="#myTextarea", text="css", clear=True)
        self.type(xpath="//textarea[@id='myTextarea']", text="xpath", clear=True)
        self.click(link_text="seleniumbase.com")
        self.open(self.test_url)
        self.click(partial_link_text="se.com")
        self.open(self.test_url)

    def test_selector(self):
        """selector"""
        self.type("id=myTextarea", text="id", clear=True)
        self.type("name=textareaName", text="name", clear=True)
        self.type("class=textareaClass", text="class name", clear=True)
        self.type("#myTextarea", text="css", clear=True)
        self.type("//textarea[@id='myTextarea']", text="xpath", clear=True)
        self.click("text=seleniumbase.com")
        self.open(self.test_url)
        self.click("text*=se.com")
        self.open(self.test_url)

    def test_step(self):
        """chaining find"""
        s = Steps()
        s.open(self.test_url).find("id=myTextarea").clear().type("id") \
            .find("name=textareaName").clear().type("name") \
            .find("name=textareaName").clear().type("name") \
            .find("class=textareaClass").clear().type("class name") \
            .find("#myTextarea").clear().type("css") \
            .find("//textarea[@id='myTextarea']").clear().type("xpath") \
            .find("text=seleniumbase.com").click() \
            .open(self.test_url) \
            .find("text*=se.com").click() \
            .open(self.test_url)


if __name__ == '__main__':
    seldom.main(browser="edge", debug=True)
