测试报告
-----------

seldom 默认生成测试报告，在你运行测试用例所再目录下面。

例如，你的目录是这样的：

.. code:: shell

    mypro/
    └── test_sample.py

测试文件 ``test_sample.py`` 内容如下：

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

执行命令：

.. code:: shell

    > cd mypro/
    > seldom -r test_sampe.py

最终运行完成的目录结构如下：

.. code:: shell

    mypro/
    ├── reports/
    │   ├── 2020_01_01_11_20_33_result.html
    └── test_sample.py

通过浏览器打开 ``2020_01_01_11_20_33_result.html``
测试报告，查看测试结果。

.. figure:: ../image/report.png
   :alt:


debug模式
~~~~~~~~~

我们并不是所有时候运行测试用例都希望生成HTML测试报告，那么就可以打开\ ``debug``\ 模式。

.. code:: py

    ...

    if __name__ == '__main__':
        seldom.main("test_sample.py", debug=True)

这样就不会生成HTML测试报告了。

定义测试报告
~~~~~~~~~~~~

你可以通过\ ``report``\ 自定义报告的路径和名称，以及报告的\ ``title``
和\ ``description``\ 。

.. code:: py

    ...

    if __name__ == '__main__':
        seldom.main(report="./report.html",
                    title="百度测试用例",
                    description="测试环境：windows 10/ chrome")
