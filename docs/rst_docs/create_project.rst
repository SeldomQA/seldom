Create project
--------------

In this chapter we will quickly experience the `seldom` project

Create case
~~~~~~~~~~~~~~

Create a Python file: `test_sample.py` .

.. code:: py

    import seldom

    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text="seldom")
            self.click(css="#su")
            self.assertInTitle("seldom")

    if __name__ == '__main__':
        seldom.main()


If you have an environment for `Selenium`, you can now run this use case.


Automated project creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`seldom` provides scaffolding to help us quickly create Web UI automation projects.



1. view the help:



.. code:: shell

    > seldom -h
    usage: seldom [-h] [-v] [-project PROJECT] [-r R] [-m M] [-install INSTALL]

    WebUI automation testing framework based on Selenium.

    optional arguments:
      -h, --help        show this help message and exit
      -v, --version     show version
      -project PROJECT  Create an Seldom automation test project.
      -h2c H2C          HAR file converts an interface test case.
      -r R              run test case
      -m M              run tests modules, classes or even individual test methods
                        from the command line
      -install INSTALL  Install the browser driver, For example, 'chrome',
                        'firefox'.




2. Create project:



.. code:: shell

    > seldom -project mypro




3. View directory structure:


.. code:: shell

    mypro/
    ├── test_dir/
    │   ├── test_sample.py
    ├── test_data/
    │   ├── data.json
    ├── reports/
    └── run.py

-  ``test_dir/`` Test case directory.
-  ``test_dir/`` Test data file directory.
-  ``reports/``  Test Report directory.
-  ``run.py`` Run the test file.
