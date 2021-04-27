Welcome to seldom documentation!
============================================

基于 selenium 和 unittest 的 Web UI/HTTP自动化测试框架。

特点:

* 提供更加简单API编写自动化测试
* 提供脚手架，快速生成自动化测试项目
* 全局启动和关闭浏览器，减少浏览器的启动次数
* 提供支持多种数据文件参数化
* 支持用例失败/错误重跑
* 定制化HTML测试报告，支持用例失败重跑和错误自动截图
* 支持HTTP接口测试 (v 2.0)

使用seldom编写测试web UI自动化测试非常简单。

.. code:: py

    import seldom


    class YouTest(seldom.TestCase):

        def test_case(self):
            """a simple test case """
            self.open("https://www.baidu.com")
            self.type(id_="kw", text="seldom")
            self.click(css="#su")
            self.assertTitle("seldom_百度搜索")


    if __name__ == '__main__':
        seldom.main()


User guide
===============

.. toctree::
   :maxdepth: 2

   rst_docs/installation
   rst_docs/create_project
   rst_docs/driver
   rst_docs/run_test
   rst_docs/main
   rst_docs/reports
   rst_docs/find_element
   rst_docs/seldom_api
   rst_docs/assertion
   rst_docs/rerun_screenshot
   rst_docs/parameterized
   rst_docs/poium
   rst_docs/testdata
   rst_docs/send_mail
   rst_docs/fixture
   rst_docs/depend


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`