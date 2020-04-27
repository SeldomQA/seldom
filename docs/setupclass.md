## 如何使用setupclass

如果你阅读seldom的源码，会发现`setUpClass()`方法已经被占用了。

```python
import unittest
from time import sleep
from seldom.webdriver import WebDriver
from seldom.running.config import Seldom
from seldom.logging import log


class TestCase(unittest.TestCase, WebDriver):

    @classmethod
    def setUpClass(cls):
        cls.driver = Seldom.driver
        cls.timeout = Seldom.timeout

```

如果，我想在项目当中使用`setUpClass()`方法，必然会重写，这就导致seldom的`setUpClass()`方法不可能，从而程序运行错误。 我们可以在自己的项目中这样定义。

```python
import seldom
from seldom.mail import SMTP


class Test(seldom.TestCase):

    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        print("hello")
        print("world")

```

既保持了父类的`setUpClass()`可用，又可以让子类继续扩展`setUpClass()`的操作。
