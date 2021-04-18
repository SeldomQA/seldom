生成测试数据
------------

测试数据是测试用例的重要部分，有我们不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

seldom提供了随机获取测试数据的方法。

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
            self.assertTitle(word + "_百度搜索")


    if __name__ == '__main__':
        seldom.main()

通过\ ``get_word()`` 随机获取一个单词，然后对这个单词进行搜索。

**testdata还提供了更多的方法:**

-  first\_name()
-  last\_name()
-  username()
-  get\_birthday()
-  get\_date()
-  get\_digits()
-  get\_email()
-  get\_float()
-  get\_future\_datetime()
-  get\_int()
-  get\_int32()
-  get\_int64()
-  get\_md5()
-  get\_now\_time()
-  get\_past\_datetime()
-  get\_uuid()
-  get\_word()
-  get\_words()
-  get\_phone()
