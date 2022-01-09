HTTP Interface Testing
-------------------------

`seldom` has many advantages in doing interface testing.

- Support HTML/XML test reports
- Support parameterization
- Support generating random data

`seldom 2.0` added support for automated testing of HTTP interfaces..

`Seldom` compatible  `Requests <https://docs.python-requests.org/en/master/>`__ API.


+-----------------+---------------------+
| seldom          | requests            |
+=================+=====================+
| self.get()      | requests.get()      |
+-----------------+---------------------+
| self.post()     | requests.post()     |
+-----------------+---------------------+
| self.put()      | requests.put()      |
+-----------------+---------------------+
| self.delete()   | requests.delete()   |
+-----------------+---------------------+

Seldom VS Request+unittest
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take a look at how unittest + requests automate interfaces:

.. code:: python

    import unittest
    import requests


    class TestAPI(unittest.TestCase):

        def test_get_method(self):
            payload = {'key1': 'value1', 'key2': 'value2'}
            r = requests.get("http://httpbin.org/get", params=payload)
            self.assertEqual(r.status_code, 200)


    if __name__ == '__main__':
        unittest.main()


This is actually pretty neat.The same use case, implemented in `seldom`.


.. code:: python

    # test_req.py
    import seldom


    class TestAPI(seldom.TestCase):

        def test_get_method(self):
            payload = {'key1': 'value1', 'key2': 'value2'}
            self.get("http://httpbin.org/get", params=payload)
            self.assertStatusCode(200)


    if __name__ == '__main__':
        seldom.main()

The advantages of `seldom` are assertions, logging, and reporting.

HAR TO CASE
~~~~~~~~~~~~~

For those unfamiliar with the Requests library, writing interface test cases through `seldom` can still be a bit difficult.
Thus, Cement provided the order for `har` file to turn `case`.

First, open the Fiddler tool to grab the packet and select a particular request.

Then, select the menu bar:`file` -> `Export Sessions` -> `Selected Sessions...`

.. figure:: ../image/fiddler.png
   :alt:


Select the file format to export.

.. figure:: ../image/fiddler2.png
   :alt:

Click on the `next` save as the `demo.har` file.

Finally, the script file `demo.py` is converted by 'seldom -h2c'.


.. code:: shell

    > seldom -h2c .\demo.har
    .\demo.py
    2021-06-14 18:05:50 [INFO] Start to generate testcase.
    2021-06-14 18:05:50 [INFO] created file: D:\.\demo.py



`demo.py` file.

.. code:: python

    import seldom


    class TestRequest(seldom.TestCase):

        def start(self):
            self.url = "http://httpbin.org/post"

        def test_case(self):
            headers = {"User-Agent": "python-requests/2.25.0", "Accept-Encoding": "gzip, deflate", "Accept": "application/json", "Connection": "keep-alive", "Host": "httpbin.org", "Content-Length": "36", "Origin": "http://httpbin.org", "Content-Type": "application/json", "Cookie": "lang=zh"}
            cookies = {"lang": "zh"}
            self.post(self.url, json={"key1": "value1", "key2": "value2"}, headers=headers, cookies=cookies)
            self.assertStatusCode(200)


    if __name__ == '__main__':
        seldom.main()


Run Test
~~~~~~~~~~

Open Debug mode \ ``seldom.run(debug=True)`` Run use cases.


.. code:: shell

    > python .\test_req.py
    2021-04-29 18:19:39 [INFO] A run the test in debug mode without generating HTML report!
    2021-04-29 18:19:39 [INFO]
                  __    __
       ________  / /___/ /___  ____ ____
      / ___/ _ \/ / __  / __ \/ __ ` ___/
     (__  )  __/ / /_/ / /_/ / / / / / /
    /____/\___/_/\__,_/\____/_/ /_/ /_/
    -----------------------------------------
                                 @itest.info

    test_get_method (test_req.TestAPI) ...
    ----------- Request 🚀 ---------------
    url: http://httpbin.org/get         method: GET
    ----------- Response 🛬️ -------------
    type: json
    {'args': {'key1': 'value1', 'key2': 'value2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-608d67ba-7948c8610ccaac8c77284b7e'}, 'origin': '113.89.239.34', 'url': 'http://httpbin.org/get?key1=value1&key2=value2'}
    ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.619s

    OK

This can be clearly seen through the logs/reports.
- The method requested
- request url
- Type of response
- Data for the response


Assertion
~~~~~~~~~~~

Asserting the data returned by the interface is an important part of our work in interface automation.

**assertJSON**

The interface returns the result:

.. code:: json

    {
      "args": {
        "hobby": [
          "basketball",
          "swim"
        ],
        "name": "tom"
      }
    }


My goal is to assert the values of the 'name' and 'hobby' parts..

.. code:: python

    import seldom


    class TestAPI(seldom.TestCase):

        def test_assert_json(self):
            payload = {'name': 'tom', 'hobby': ['basketball', 'swim']}
            self.get("http://httpbin.org/get", params=payload)
            assert_json = {'args': {'hobby': ['swim', 'basketball'], 'name': 'tom'}}
            self.assertJSON(assert_json)


Running logs


.. code:: shell

    test_get_method (test_req.TestAPI) ...
    ----------- Request ---------------
    url: http://httpbin.org/get         method: GET
    ----------- Response -------------
    type: json
    {'args': {'hobby': ['basketball', 'swim'], 'name': 'tom'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-608a896d-48fac4f6139912ba01d2626f'}, 'origin': '183.178.27.36', 'url': 'http://httpbin.org/get?name=tom&hobby=basketball&hobby=swim'}
    💡 Assert data has not key: headers
    💡 Assert data has not key: origin
    💡 Assert data has not key: url
    ok

    ----------------------------------------------------------------------
    Ran 1 test in 1.305s

    OK

`seldom` will also prompt you for fields that have not been asserted.


**assertPath**

'assertPath' is an assertion method based on 'jmespath', very powerful.

jmespath:https://jmespath.org/specification.html

The interface returns the result:

.. code:: json

    {
      "args":{
        "hobby":
          ["basketball", "swim"],
        "name": "tom"
      }
    }


Assertion using PATH:


.. code:: python

    import seldom


    class TestAPI(seldom.TestCase):

        def test_assert_path(self):
            payload = {'name': 'tom', 'hobby': ['basketball', 'swim']}
            self.get("http://httpbin.org/get", params=payload)
            self.assertPath("name", "tom")
            self.assertPath("args.hobby[0]", "basketball")


**assertSchema**

Sometimes you don't care what the data itself is, but you need to assert the type of the data.
'assertSchema' is an assertion method based on 'JSONSchema'.

jsonschema: https://json-schema.org/learn/

The interface returns the result:

.. code:: json

    {
      "args": {
        "hobby":
          ["basketball", "swim"],
        "name": "tom",
        "age": "18"
      }
    }


Assertion using `assertSchema`:

.. code:: python

    import seldom


    class TestAPI(seldom.TestCase):

        def test_assert_schema(self):
            payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
            self.get("/get", params=payload)
            schema = {
                "type": "object",
                "properties": {
                    "args": {
                        "type": "object",
                        "properties": {
                            "age": {"type": "string"},
                            "name": {"type": "string"},
                            "hobby": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                            }
                        }
                    }
                },
            }
            self.assertSchema(schema)


Again, the assertions provided by `seldom` are very flexible and powerful.


Interface Data Dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In scenario testing, we need to call the next interface using data from the previous interface.

**Sample 1**

.. code:: python

    import seldom

    class TestRespData(seldom.TestCase):

        def test_data_dependency(self):
            """
            Test for interface data dependencies
            """
            headers = {"X-Account-Fullname": "bugmaster"}
            self.get("/get", headers=headers)
            self.assertStatusCode(200)

            username = self.response["headers"]["X-Account-Fullname"]
            self.post("/post", data={'username': username})
            self.assertStatusCode(200)


\ ``self.response``\ Used to record the result returned by the last interface, just use it.

**Sample 2**

Defining common modules

.. code:: python

    # common.py
    from seldom import HttpRequest


    class Common(HttpRequest):

        def get_login_user(self):
            """
            Call the interface to get the user name
            """
            headers = {"X-Account-Fullname": "bugmaster"}
            self.get("http://httpbin.org/get", headers=headers)
            user = self.response["headers"]["X-Account-Fullname"]
            return user


Create classes that inherit `HttpRequest` class calls using Http request methods 'get/post/put/delete'.

Referencing public modules

.. code:: python

    import seldom
    from common import Common


    class TestRequest(seldom.TestCase):

        def start(self):
            self.c = Common()

        def test_case(self):
            #  get_login_user()
            user = self.c.get_login_user()
            print(user)
            self.post("http://httpbin.org/post", data={'username': user})
            self.assertStatusCode(200)


    if __name__ == '__main__':
        seldom.main(debug=True)


Data-Driver
~~~~~~~~~~~~~

`seldom` has a strong data-driven nature and is very convenient for interface testing.

**@data**

.. code:: python

    import seldom
    from seldom import data


    class TestDDT(seldom.TestCase):

        @data([
            ("key1", 'value1'),
            ("key2", 'value2'),
            ("key3", 'value3')
        ])
        def test_data(self, key, value):
            """
            Data-Driver Tests
            """
            payload = {key: value}
            self.post("/post", data=payload)
            self.assertStatusCode(200)
            self.assertEqual(self.response["form"][key], value)

**@file\_data**

data file:

.. code:: json

    {
     "login":  [
        ["admin", "admin123"],
        ["guest", "guest123"]
     ]
    }


code file:

.. code:: python

    import seldom
    from seldom import file_data


    class TestDDT(seldom.TestCase):

        @file_data("data.json", key="login")
        def test_data(self, username, password):
            """
            Data-Driver Tests
            """
            payload = {username: password}
            self.post("http://httpbin.org/post", data=payload)
            self.assertStatusCode(200)
            self.assertEqual(self.response["form"][username], password)

More like data files(csv/excel/yaml),\ `View <https://github.com/SeldomQA/seldom/blob/master/docs/advanced.md>`__


Random Test Data
~~~~~~~~~~~~~~~~~~

SELDOM provides a method of randomly generating test data to generate some commonly used data.

.. code:: python

    import seldom
    from seldom import testdata


    class TestAPI(seldom.TestCase):

        def test_data(self):
            phone = testdata.get_phone()
            payload = {'phone': phone}
            self.get("http://httpbin.org/get", params=payload)
            self.assertPath("args.phone", phone)


For more types of test data, `View <https://github.com/SeldomQA/seldom/blob/master/docs/advanced.md>`__
