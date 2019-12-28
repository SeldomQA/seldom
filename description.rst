seldom
---------------

WebUI automation testing framework based on Selenium and unittest.

Installation
------------

    $ pip install seldom


Quick Example
++++++++++++++++++


    import seldom


    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text="seldom")
            self.click(css="#su")
            self.assertTitle("seldom_百度搜索")


    if __name__ == '__main__':
        seldom.main("test_sample.py")


Documentation
++++++++++++++++++

https://github.com/SeldomQA/seldom
