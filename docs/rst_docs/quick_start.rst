Quick Start
-------------

Download Browser Driver
~~~~~~~~~~~~~~~~~~~~~~~~~


As with `Selenium`, before you can run automated tests using `seldom`, you need to configure the browser driver, This step is very important.


**Automatically download**

`Seldom` provides automatic download driven by `Chrome/Firefox` browser.

.. code:: shell

    > seldom -install chrome
    > seldom -install firefox



By default, download to the current 'lib/' directory.


'ChromeDriver' Mirror image of Taobao used.

**Manually download**

`seldom` cannot determine the version of your current browser, so it is recommended to download it manually.


-  Firefox:
   `geckodriver <https://github.com/mozilla/geckodriver/releases>`__

-  Chrome:
   `Chromedriver <https://sites.google.com/a/chromium.org/chromedriver/home>`__

-  IE:
   `IEDriverServer <http://selenium-release.storage.googleapis.com/index.html>`__

-  Opera:
   `operadriver <https://github.com/operasoftware/operachromiumdriver/releases>`__

-  Edge:
   `MicrosoftWebDriver <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver>`__

-  Safari: safaridriver
   (macOS,default path:`/usr/bin/safaridriver`)

Configure the environment variables for the downloaded driver file.Different operating systems (Windows/MacOS/Linux) are configured differently.


``main()`` Method
~~~~~~~~~~~~~~~~~~~


`main()` method is `seldom` run test entry method, It provides some of the most basic and important configurations.


.. code:: python

    import seldom

    # ...

    if __name__ == '__main__':

        seldom.main(path="./",
                    browser="chrome",
                    base_url="",
                    report=None,
                    title="project name",
                    description="Environment description",
                    debug=False,
                    rerun=0,
                    save_last_run=False,
                    timeout=None,
        )



**Parameter specification**

-  path : Specifies the test directory or file.
-  browser : Run browser name, default `Chrome`.
-  base\_url : A parameter to test the HTTP interface testing, setting the global URL.
-  report : The name of the custom test report, The default format is `YYYY_mm_dd_HH_MM_SS_result.html`.
-  title : Test report title.
-  description : Test report description.
-  debug : Debug mode,  set to True does not generate test HTML tests, default is `False`.
-  rerun : Sets the number of failed reruns, Default is `0`.
-  save\_last\_run : Sets to save only the last result, default to `False`.
-  timeout : Sets the timeout, Default `10` seconds.


Run Test
~~~~~~~~~~

**Run under a terminal (recommended)**


Create the file `run.py`, And import `main()` method.


.. code:: py

    import seldom

    # ...

    seldom.main()    # 


`main()` Method Run the use case in the current file by default.


.. code:: shell

    > python run.py      # Run with the Python command
    > seldom -r run.py   # Run with the Seldom command


**Set the running directory, file**


You can specify the directory or file to run with the `path` parameter.


.. code:: py

    seldom.main(path="./")  
    seldom.main(path="./test_dir/")
    seldom.main(path="./test_dir/test_sample.py")
    seldom.main(path="D:/seldom_sample/test_dir/test_sample.py")


**Run a class or method**


The `seldom -m` command can provide a more granular run.

.. code:: shell

    > seldom -m test_sample     #  test_sample.py file
    > seldom -m test_sample.SampleTest      #  SampleTest Class
    > seldom -m test_sample.SampleTest.test_case    # test_case method


Failed Rerun
~~~~~~~~~~~~~~~~

`seldom` support failed reruns, as well as screenshots.

.. code:: python

    import seldom

    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text="seldom")
            self.click(css="#su_error")
            #...


    if __name__ == '__main__':
        seldom.main(rerun=3, save_last_run=False)



**Parameters**

-  rerun : Sets the number of failed reruns, Default is `0`.
-  save\_last\_run : Sets to save only the last result, default to `False`.


**Run logs**

.. code:: shell

    > seldom -r test_sample.py

    2021-04-14 11:25:53,265 INFO Run the python version:
    2021-04-14 11:25:53,265 - INFO - INFO Run the python version:
    Python 3.7.1

                  __    __
       ________  / /___/ /___  ____ ____
      / ___/ _ \/ / __  / __ \/ __ ` ___/
     (__  )  __/ / /_/ / /_/ / / / / / /
    /____/\___/_/\__,_/\____/_/ /_/ /_/
    -----------------------------------------
                                 @itest.info


    DevTools listening on ws://127.0.0.1:12699/devtools/browser/301751bd-a833-44d1-8669-aa85d418b302
    2021-04-14 23:31:54 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
    ERetesting... test_case (test_demo.YouTest)..1
    2021-04-14 23:32:05 [INFO] 📖 https://www.baidu.com
    2021-04-14 23:32:06 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
    ERetesting... test_case (test_demo.YouTest)..2
    2021-04-14 23:32:17 [INFO] 📖 https://www.baidu.com
    2021-04-14 23:32:22 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
    ERetesting... test_case (test_demo.YouTest)..3
    2021-04-14 23:32:32 [INFO] 📖 https://www.baidu.com
    2021-04-14 23:32:36 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
    2021-04-14 23:32:47 [INFO] generated html file: file:///D:\github\seldom\reports\2021_04_14_23_31_51_result.html
    E



**The test report**

.. figure:: ../image/report.png
   :alt: 


To view the screenshots, click the `show` button in the report.


Test Report
~~~~~~~~~~~~~

`seldom` automatically generates HTML test reports by default.

-  Befor running the test case

.. code:: shell

    mypro/
    └── test_sample.py

-  After running the test case

.. code:: shell

    mypro/
    ├── reports/
    │   ├── 2020_01_01_11_20_33_result.html
    └── test_sample.py


Open the `2020_01_01_11_20_33_result.html` test report through a browser, View the test results.


**Debug mode**


if you don't want to generate and HTML report every time you run, You can opent the `debug` mode.

.. code:: py


    if __name__ == '__main__':
        seldom.main(debug=True)


**Define Test Reports**

.. code:: py


    if __name__ == '__main__':
        seldom.main(report="./report.html",
                    title="xxxx",
                    description="run evn：windows 10/ chrome")


-  report: Configure the report name and path.
-  title: Customize the title of the report.
-  description: Add report information.


**XML Test Reoprt**

If you want to generate a report in XML format, just change the suffix name `.xml` of the report.

.. code:: py


    if __name__ == '__main__':
        seldom.main(report="./report.xml")

