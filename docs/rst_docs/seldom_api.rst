seldom API
-----------

Find Element
~~~~~~~~~~~~~~

Selenium provides 8 ways of find element, which are consistent with Selenium.


-  id\_
-  name
-  class\_name
-  tag
-  link\_text
-  partial\_link\_text
-  css
-  xpath

**Demo**

.. code:: python

    self.type(id_="kw", text="seldom")
    self.type(name="wd", text="seldom")
    self.type(class_name="s_ipt", text="seldom")
    self.type(tag="input", text="seldom")
    self.type(xpath="//input[@id='kw']", text="seldom")
    self.type(css="#kw", text="seldom")
    self.click(link_text="hao123")
    self.click(partial_link_text="hao")

**Help Information**

-  `CSS Selectors <https://www.w3school.com.cn/cssref/css_selectors.asp>`__
-  `xpath Syntax <https://www.w3school.com.cn/xpath/xpath_syntax.asp>`__

**Index**

Sometimes a single element cannot be found by a single location, then you can specify the index of an element via `index`.

.. code:: py

    self.type(tag="input", index=7, text="seldom")


`tag="input"` Matches a set of elements, `index=7` Specifies the eighth element in the set, `index` default subscript `0`.


Fixture
~~~~~~~~~

A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions.

`seldom` provides a way to implement fixtures.

**start & end**

Fixture for each test case.

.. code:: python

    import seldom


    class TestCase(seldom.TestCase):

        def start(self):
            print("start case")

        def end(self):
            print("end case")

        def test_search_seldom(self):
            self.open("https://www.baidu.com")
            self.type_enter(id_="kw", text="seldom")

        def test_search_poium(self):
            self.open("https://www.baidu.com")
            self.type_enter(id_="kw", text="poium")



**start\_class & end\_class**

Fixture for each test class.

.. code:: python

    import seldom


    class TestCase(seldom.TestCase):

        @classmethod
        def start_class(cls):
            print("start test class")

        @classmethod
        def end_class(cls):
            print("end test class")

        def test_search_seldom(self):
            self.open("https://www.baidu.com")
            self.type_enter(id_="kw", text="seldom", clear=True)

        def test_search_poium(self):
            self.open("https://www.baidu.com")
            self.type_enter(id_="kw", text="poium", clear=True)


    Warning: Don't write the use case steps into the fixture method!
    Because it is not part of a use case, the test report will not be generated if the steps in it fail to run.


Assertion
~~~~~~~~~~~


`seldom` provides a set of assertion methods for Web pages.


**Deom**

.. code:: python

    # Asserts is equals to "title"
    self.assertTitle("title")

    # Asserts contains "title"
    self.assertInTitle("title")

    # Asserts is equals to "title"
    self.assertUrl("url")

    # Asserts contains "url"
    self.assertInUrl("url")

    # Asserts that the page contains "text"
    self.assertText("text")

    # Asserts that the page not contains "text"
    self.assertNotText("text")

    # Assert that the warning message is equal to "text"
    self.assertAlertText("text")

    # Asserts whether an element exists
    self.assertElement(css="#kw")

    # Asserts if the element does not exist
    self.assertNotElement(css="#kwasdfasdfa")


Skipping tests and expected failures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following decorators and exception implement test skipping and expected failures:


**Method**

- @seldom.skip(reason) : Unconditionally skip the decorated test. reason should describe why the test is being skipped.

- @seldom.skip\_if(condition, reason) : Skip the decorated test if condition is true.

- @seldom.skip\_unless(condition, reason) : Skip the decorated test unless condition is true.

- @seldom.expected\_failure : Mark the test as an expected failure or error. If the test fails or errors it will be considered a success. If the test passes, it will be considered a failure.


**Demo**

.. code:: python

    import seldom

    @seldom.skip("skip this use test class")
    class YouTest(seldom.TestCase):

        @seldom.skip("skip this case")
        def test_case(self):
            # ...


    if __name__ == '__main__':
        seldom.main()


WebDriver API
~~~~~~~~~~

`Seldom` simplifies the API, Make it easier for you to navigate Web pages.

Most APIs are provided by `WebDriver` class:

.. code:: python

    import seldom

    class TestCase(seldom.TestCase):

        def test_seldom_api(self):
            # Accept warning box.
            self.accept_alert()
            
            # Adds a cookie to your current session.
            self.add_cookie({'name' : 'foo', 'value' : 'bar'})
            
            # Adds a cookie to your current session.
            cookie_list = [
                {'name' : 'foo', 'value' : 'bar'},
                {'name' : 'foo', 'value' : 'bar'}
            ]
            self.add_cookie(cookie_list)
            
            
            # Clear the contents of the input box.
            self.clear(css="#el")
            
            # It can click any text / image can be clicked
            # Connection, check box, radio buttons, and even drop-down box etc..
            self.click(css="#el")
            
            # Mouse over the element.
            self.move_to_element(css="#el")
            
            # Click the element by the link text
            self.click_text("新闻")
            
            # Simulates the user clicking the "close" button in the titlebar of a popup window or tab.
            self.close()
            
            # Delete all cookies in the scope of the session.
            self.delete_all_cookies()
            
            # Deletes a single cookie with the given name.
            self.delete_cookie('my_cookie')
            
            # Dismisses the alert available.
            self.dismiss_alert()
            
            # Double click element.
            self.double_click(css="#el")
            
            # Execute JavaScript scripts.
            self.execute_script("window.scrollTo(200,1000);")
            
            # Setting width and height of window scroll bar.
            self.window_scroll(width=300, height=500)
            
            # Setting width and height of element scroll bar.
            self.element_scroll(css=".class", width=300, height=500)
            
            # open url.
            self.open("https://www.baidu.com")
            
            # Gets the text of the Alert.
            self.get_alert_text
            
            # Gets the value of an element attribute.
            self.get_attribute(css="#el", attribute="type")
            
            # Returns information of cookie with ``name`` as an object.
            self.get_cookie()
            
            # Returns a set of dictionaries, corresponding to cookies visible in the current session.
            self.get_cookies()
            
            # Gets the element to display,The return result is true or false.
            self.get_display(css="#el")
            
            # Get a set of elements
            self.get_element(css="#el", index=0)
            
            # Get element text information.
            self.get_text(css="#el")
            
            # Get window title.
            self.get_title
            
            # Get the URL address of the current page.
            self.get_url
            
            # Set browser window maximized.
            self.max_window()
            
            # Mouse over the element.
            self.move_to_element(css="#el")
            
            # open url.
            self.open("https://www.baidu.com")
            
            # Quit the driver and close all the windows.
            self.quit()
            
            # Refresh the current page.
            self.refresh()
            
            # Right click element.
            self.right_click(css="#el")
            
            # Saves a screenshots of the current window to a PNG image file.
            self.screenshots() # Save to HTML report
            self.screenshots('/Screenshots/foo.png')  # Save to the specified directory

            # Saves a element screenshot of the element to a PNG image file.
            self.element_screenshot(css="#id") # Save to HTML report
            self.element_screenshot(css="#id", file_path='/Screenshots/foo.png') # Save to the specified directory

            """
            Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
            then an UnexpectedTagNameException is thrown.
            <select name="NR" id="nr">
                <option value="10" selected="">10 dollar</option>
                <option value="20">20 dollar</option>
                <option value="50">50 dollar</option>
            </select>
            """
            self.select(css="#nr", value='20')
            self.select(css="#nr", text='20 dollar')
            self.select(css="#nr", index=2)
            
            # Set browser window wide and high.
            self.set_window(100, 200)
            
            # Submit the specified form.
            self.submit(css="#el")
            
            # Switch to the specified frame.
            self.switch_to_frame(css="#el")
            
            # Returns the current form machine form at the next higher level.
            # Corresponding relationship with switch_to_frame () method.
            self.switch_to_frame_out()
            
            
            # Switches focus to the specified window.
            # This switches to the new windows/tab (0 is the first one)
            self.switch_to_window(1)
            
            # Operation input box.
            self.type(css="#el", text="selenium")
            
            
            # Implicitly wait.All elements on the page.
            self.wait(10)
            
            # Setting width and height of window scroll bar.
            self.window_scroll(width=300, height=500)


Keys
~~~~~~

Sometimes we need to use the keyboard, For example: ``enter`` ,``backspace`` ,``TAB`` ,``ctrl/command + a``, ``ctrl/command + c`` and so on.

`sedom` provides a set of keyboard operations.

**Demo**

.. code:: py

    import seldom


    class Test(seldom.TestCase):

        def test_key(self):
            self.open("https://www.baidu.com")

            self.Keys(css="#kw").input("seldomm")

            self.Keys(id_="kw").backspace()

            self.Keys(id_="kw").input("github")

            self.Keys(id_="kw").select_all()

            self.Keys(id_="kw").cut()

            self.Keys(id_="kw").paste()

            self.Keys(id_="kw").enter()


    if __name__ == '__main__':
        seldom.main()
