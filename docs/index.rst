Welcome to seldom documentation!
============================================

Web UI/HTTP automated testing framework based on unittest.

Features:

* Provide scaffolding to quickly generate automated test items
* Start and close the browser globally, reducing the number of browser launches
* Provides support for multiple data file parameterization
* Support for use case failure/error reruns
* Automatically generate HTML test reports
* Support for HTTP interface testing (v 2.0)


Using `seldom` to write test Web UI automation tests is very simple.


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


User guide
===============

.. toctree::
   :maxdepth: 2

   rst_docs/installation
   rst_docs/create_project
   rst_docs/quick_start
   rst_docs/seldom_api
   rst_docs/advanced
   rst_docs/other
   rst_docs/http
   rst_docs/db_operation


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`