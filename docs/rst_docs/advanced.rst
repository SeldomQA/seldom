Advanced Usage
----------------

Random Test Data
~~~~~~~~~~~~~~~~~~


`seldom` provides a method for randomly capturing test data.

**Demo**

.. code:: python

    import seldom
    from seldom import testdata


    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            word = testdata.get_word()
            self.open("https://www.baidu.com")
            self.type(id_="kw", text=word)
            self.click(css="#su")
            self.assertInTitle(word)


    if __name__ == '__main__':
        seldom.main()



Get a random word by `get_word()` and search for that word.


**More method**

-  first\_name()
-  last\_name()
-  username()
-  get\_birthday()
-  get\_date()
-  get\_digits()
-  get\_email()
-  get\_float()
-  get\_now\_time()
-  get\_past\_time()
-  get\_future\_time()
-  get\_past\_datetime()
-  get\_future\_datetime()
-  get\_int()
-  get\_int32()
-  get\_int64()
-  get\_md5()
-  get\_uuid()
-  get\_word()
-  get\_words()
-  get\_phone()


Data-driven Best Practices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you automate a function when the test data is different but the steps are the same, you can use parameterization to save test code.

**@data**

method of parameterizing test cases.

.. code:: python


    import seldom
    from seldom import data


    class BaiduTest(seldom.TestCase):

        @data([
            (1, 'seldom'),
            (2, 'selenium'),
            (3, 'unittest'),
        ])
        def test_baidu(self, _, keyword):
            """
            used parameterized test
            """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text=keyword)
            self.click(css="#su")
            self.assertTitle(keyword+"_百度搜索")



**@data_class**

Parameterizes a test class by setting attributes on the class.

.. code:: python

    import seldom
    from seldom import data_class

    @data_class(
        ("keyword", "assert_tile"),
        [("seldom", "seldom_百度搜索"),
         ("python", "python_百度搜索")
    ])
    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text=self.keyword)
            self.click(css="#su")
            self.assertTitle(self.assert_tile)


**CSV data file**

`seldom` support for parameterization of `CSV` files.

`data.csv` file contents:

+------------+------------+
| username   | password   |
+============+============+
| admin      | admin123   |
+------------+------------+
| guest      | guest123   |
+------------+------------+


.. code:: python

    import seldom
    from seldom import file_data


    class YouTest(seldom.TestCase):

        @file_data("data.csv", line=2)
        def test_login(self, username, password):
            """a simple test case """
            print(username)
            print(password)
            # ...


-  file: The name of the CSV file.
-  line: Start reading line 1 by default.

**Excel data file**

`seldom` support for parameterization of `excel` files.

.. code:: python

    import seldom
    from seldom import file_data


    class YouTest(seldom.TestCase):

        @file_data("data.xlsx", sheet="Sheet1", line=2)
        def test_login(self, username, password):
            """a simple test case """
            print(username)
            print(password)
            # ...


-  file : The name of the Excel file.
-  sheet: Excel sheet name, default to `sheet1`.
-  line : Start reading line 1 by default.

**JSON data file**

`seldom` support for parameterization of `JSON` files.

json file:

.. code:: json

    {
     "login1":  [
        ["admin", "admin123"],
        ["guest", "guest123"]
     ],
    "login2":  [
        {
          "username": "Tom",
          "password": "tom123"
        },
        {
          "username": "Jerry",
          "password": "jerry123"
        }
      ]
    }


Note: 'login1' and 'login2' are called in the same way. The difference is that the former is more concise while the latter is easier to read.

python code:


.. code:: python

    import seldom
    from seldom import file_data


    class YouTest(seldom.TestCase):

        @file_data("data.json", key="login1")
        def test_login(self, username, password):
            """a simple test case """
            print(username)
            print(password)
            # ...

-  file : The name of the JSON file..
-  key: Specifies the key of the dictionary. By default, parsing the entire JSON file is not specified.

**YAML file data**

`seldom` support for parameterization of `YAML` files.

data.yaml file:

.. code:: yaml

    login1:
      - - admin
        - admin123
      - - guest
        - guest123
    login2:
      - username: Tom
        password: tom123
      - username: Jerry
        password: jerry123


Like JSON usage, YAML is much more compact to write.

python code:

.. code:: python

    import seldom
    from seldom import file_data


    class YouTest(seldom.TestCase):

        @file_data("data.yaml", key="login1")
        def test_login(self, username, password):
            """a simple test case """
            print(username)
            print(password)
            # ...

-  file : The name of the YAML file.
-  key: Specifies the key of the dictionary. By default, parsing the entire YAML file is not specified.


**ddt library**

Seldom supports third party parameterized libraries:\ `ddt <https://github.com/datadriventests/ddt>`__\ .

installation:

.. code:: shell

    > pip install ddt

Create the test file `test_data.json`:

.. code:: json

    {
        "test_data_1": {
            "word": "seldom"
        },
        "test_data_2": {
            "word": "unittest"
        },
        "test_data_3": {
           "word": "selenium"
        }
    }


In `seldom` use `ddt`.


.. code:: python

    import seldom
    from ddt import ddt, file_data


    @ddt
    class YouTest(seldom.TestCase):

        @file_data("test_data.json")
        def test_case(self, word):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text=word)
            self.click(css="#su")
            self.assertInTitle(word)


    if __name__ == '__main__':
        seldom.main()


See the ddt documentation for more usage:https://ddt.readthedocs.io/en/latest/example.html


Page Objects Design Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


`poium <https://github.com/SeldomQA/poium>`__ Is `Page objects` design pattern best practice.

**installation:**

.. code:: shell

    > pip install poium==1.0.0


**Use `seldom` and `poium` together**


.. code:: python

    import seldom
    from poium import Page, Element


    class BaiduPage(Page):
        """baidu page"""
        search_input = Element(id_="kw")
        search_button = Element(id_="su")


    class BaiduTest(seldom.TestCase):
        """Baidu serach test case"""

        def test_case(self):
            """
            A simple test
            """
            page = BaiduPage(self.driver)
            page.get("https://www.baidu.com")
            page.search_input = "seldom"
            page.search_button.click()
            self.assertInTitle("seldom")


    if __name__ == '__main__':
        seldom.main()


Automatic Email
~~~~~~~~~~~~~~~~~

**Demo**

.. code:: python

    import seldom
    from seldom import SMTP

    # ...

    if __name__ == '__main__':
        seldom.main()
        smtp = SMTP(user="send@126.com", password="abc123", host="smtp.126.com")
        smtp.sendmail(to="receive@mail.com", subject='Email title')


-  subject: Email title, default: `Seldom Test Report`.
-  to: Addressee email, Add multiple recipients commas ',' to separate.


Use Case Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

While it is not recommended to write dependent use cases, there are times when you can't completely avoid them.

**depend**

`depend` Decorators are used to set dependent use cases.

.. code:: python

    import seldom
    from seldom import depend


    class TestDepend(seldom.TestCase):

        def test_001(self):
            # ...

        @depend("test_001")
        def test_002(self):
            # ...

        @depend("test_002")
        def test_003(self):
            # ...

    if __name__ == '__main__':
        seldom.main(debug=True)


`test_002` depends on `test_001`, and `test_003` depends on `test_002`.


**if\_depend**

Customize the state of the use case, and the dependent use case chooses whether to skip.

.. code:: python

    import seldom
    from seldom import if_depend

    class TestIfDepend(seldom.TestCase):
        Test001 = True

        def test_001(self):
            self.open("https://www.baidu.com")
            TestIfDepend.Test001 = False  # Change Test001 to False

        @if_depend("Test001")
        def test_002(self):
            self.open("http://news.baidu.com/")


    if __name__ == '__main__':
        seldom.main(debug=True)


Use case classification label
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function is implemented in seldom version 2.4.0.

**demo**

.. code:: python

    # test_label.py
    import seldom
    from seldom import label


    class MyTest(seldom.TestCase):

        @label("base")
        def test_label_base(self):
            self.assertEqual(1+1, 2)

        @label("slow")
        def test_label_slow(self):
            self.assertEqual(1, 2)

        def test_no_label(self):
            self.assertEqual(2+3, 5)


    if __name__ == '__main__':
        # seldom.main(debug=True, whitelist=["base"])  # whitelist
        seldom.main(debug=True, blacklist=["slow"])    # blacklist


If you only run the use cases labeled `base`, set the whitelist.


.. code:: shell
    > python test_label.py
    test_label_base (btest_label.MyTest) ... ok
    test_label_slow (btest_label.MyTest) ... skipped "label whitelist {'base'}"
    test_no_label (btest_label.MyTest) ... skipped "label whitelist {'base'}"

    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK (skipped=2)


If you only want to block the use cases labeled `slow`, set a blacklist.


.. code:: shell
    > python test_label.py

    test_label_base (btest_label.MyTest) ... ok
    test_label_slow (btest_label.MyTest) ... skipped "label blacklist {'slow'}"
    test_no_label (btest_label.MyTest) ... ok
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK (skipped=1)
