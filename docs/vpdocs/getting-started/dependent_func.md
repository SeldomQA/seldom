# 方法的依赖

> 在 seldom 3.4.0 版本实现了该功能。

在复杂的测试场景中，常常会存在用例依赖，以一个接口自动化平台为例，依赖关系：

`创建用例` --> `创建模块` --> `创建项目` --> `登录`。

__用例依赖的问题__

* 用例的依赖对于的执行顺序有严格的要求，比如让被依赖的方法先执行。
* 一旦使用用例依赖，依赖的用例就无法单独执行了，按照用例的设计原则，每条用例都应该独立执行。

__正确的做法__

`我们应该将依赖的操作封装成方法调用`。如果能通过装饰器实现调用，那就很有趣了。

[aomaker](https://github.com/ae86sen/aomaker) 提供了这种装饰器的实现，seldom 进行了复刻，只是的定位和用法用有所不同。

### 类内部方法调用

我们可以在测试类下面，创建普通的方法。然后通过`@dependent_func()`装饰器调用他。

```python
import seldom
from seldom.testdata import get_md5
from seldom.utils import cache, dependent_func


class DependentTest(seldom.TestCase):

    @staticmethod
    def user_login(username, password):
        """
        模拟用户登录，获取登录token
        """
        return get_md5(username+password)

    @dependent_func(user_login, username="tom", password="t123")
    def test_case(self,):
        """
        sample test case
        """
        token = cache.get("user_login")
        print("token", token)


if __name__ == '__main__':
    seldom.main(debug=True)
    cache.clear()
```

__说明__ 

这个例子涉及到不少知识点。

1. `test_case()` 用例依赖 `user_login()` 方法，通过 `@dependent_func()` 装饰器调用 `user_login` 方法。
2. `user_login()` 方法运行的时候需要参数（username、password），可以直接在  `@dependent_func()` 装饰器中设置参数：`username="tom"`、 `password="t123"`。
3. `user_login()` 方法运行运行完会生成 token, 保存于 cache中，通过 ` cache.get()` 可以获取到token, 默认通过方法名`user_login` 作为key获取。
4. 为了简化代码，生成token 是通过 `get_md5()` 根据传入的参数生成的一个 md5 值。
5. `cache.clear()` 用于清空缓存， 再次调用 `user_login()` 方法直接不执行，应为cache已经有上次的执行结果了。

__执行日志__

```shell
python zzz_demo.py
...
test_case (zzz_demo.DependentTest.test_case)
sample test case ... 2023-11-15 23:26:36 | INFO     | dependence.py | 🔗 <test_case> depends on <user_login>, execute.
2023-11-15 23:26:36 | INFO     | cache.py | 💾 Set cache data: user_login = 35e0ff9c4cba89998dda8255d0eb5408
2023-11-15 23:26:36 | INFO     | cache.py | 💾 Get cache data: user_login = 35e0ff9c4cba89998dda8255d0eb5408
token 35e0ff9c4cba89998dda8255d0eb5408
ok

----------------------------------------------------------------------
Ran 1 test in 0.005s

OK
2023-11-15 23:26:36 | SUCCESS  | runner.py | A run the test in debug mode without generating HTML report!
2023-11-15 23:26:36 | INFO     | cache.py | 💾 Clear all cache data
```


### 外部类方法依赖

* 创建依赖方法

```python
# common.py
from seldom.testdata import get_md5


class Login:

    @staticmethod
    def account_login(username, password):
        """
        模拟用户&密码登录，获取登录token
        """
        return get_md5(username+password)


login=Login()
```

* 用例引用依赖方法

```python
import seldom
from seldom.utils import cache, dependent_func
from common import Login # 方式1：引用依赖类
# from common import login  # 方式2：引用初始化好的类对象


class DependentTest(seldom.TestCase):


    @dependent_func(Login().account_login, key_name="token1", username="tom", password="t123")
    # @dependent_func(login.account_login, key_name="token1", username="tom", password="t123")
    def test_case(self):
        """
        Used tuple test data
        """
        token = cache.get("token1")
        print("token", token)


if __name__ == '__main__':
    seldom.main(debug=True)
```

__说明__

1. `Common` 类的`account_login()`方法可以不设置为静态方法，导入时需要类需要加括号：`Common().user_login`。 或者先初始化类对象`login=Login()` 再调用。
2. `key_name` 指定缓存的 `key`，如果指定为`token1`, 从缓存读取也使用这个`cache.get("token1")`。

### 多重方法依赖


复杂的场景当然是需要多重依赖的。

1. 被依赖的方法可以进一步使用 `dependent_func()`装饰器进行多重复依赖。

`查询模块` --> `查询项目` --> `登录`

```python
# common.py
from seldom.testdata import get_md5, get_int
from seldom.utils import cache, dependent_func

class Login:

    @staticmethod
    def account_login(username, password):
        """
        模拟用户&密码登录，获取登录token
        """
        return get_md5(username+password)

class DepFunc:

    @staticmethod
    @dependent_func(Login.account_login, key_name="token", username="jack", password="456")
    def get_project_id():
        token = cache.get("token")
        print(f"使用token:{token} 查询项目, 返回项目ID")
        return get_int(1, 1000)


    @staticmethod
    @dependent_func(get_project_id, key_name="pid")
    def get_module_id():
        pid = cache.get("pid")
        print(f"使用项目ID:{pid} 查询模块, 返回模块ID")
        return get_int(1, 1000)
```

在用例中直接调用 `DepFunc.get_module_id` 方法即可。

```python
import seldom
from seldom.utils import cache, dependent_func
from common import DepFunc


class DependentTest(seldom.TestCase):


    @dependent_func(DepFunc.get_module_id, key_name="mid")
    def test_case(self):
        """
        sample test case
        """
        mid = cache.get("mid")
        print(f"模块ID: {mid}")


if __name__ == '__main__':
    seldom.main(debug=True)
    cache.clear()
```


2. 测试用例也可以同时使用多个 `@dependent_func()` 装饰器依赖多个方法，顺序由上到下执行，这种方式主要用于被依赖的方法之间没有依赖关系。

```python
# common.py
from seldom.testdata import get_int, username


class DataFunc:

    @staticmethod
    def get_name():
        return username(language="zh")

    @staticmethod
    def get_age():
        return get_int(1, 99)
```

在用例中使用多个`@dependent_func()`依赖装饰器。

```python
import seldom
from seldom.utils import cache, dependent_func
from common import DataFunc


class DependentTest(seldom.TestCase):


    @dependent_func(DataFunc.get_name, key_name="name")
    @dependent_func(DataFunc.get_age, key_name="age")
    def test_case(self):
        """
        sample test case
        """
        name = cache.get("name")
        age = cache.get("age")
        print(f"名字: {name}, 年龄: {age}")


if __name__ == '__main__':
    seldom.main(debug=True)
    cache.clear()
```


### 参数化使用

参数化 `@data()`、 `@file_data()` 是seldom最重要的功能之一，能否和 `@dependent_func()` 一起使用？ 当然可以。

```python
import seldom
from seldom import data
from seldom.testdata import get_md5
from seldom.utils import cache, dependent_func


class DependentTest(seldom.TestCase):

    @staticmethod
    def user_login(username, password):
        """
        模拟用户登录，获取登录token
        """
        return get_md5(username+password)

    @data([
        ("case1", "foo"),
        ("case2", "bar"),
    ])
    @dependent_func(user_login, username="tom", password="t123")
    def test_case(self, _, keyword):
        """
        Used tuple test data
        """
        token = cache.get("user_login")
        print(keyword, "token", token)


if __name__ == '__main__':
    seldom.main(debug=True)
    cache.clear()
```

__说明__

1. `@data()` 装饰器必须写在 `@dependent_func()` 的上面。
2. 运行两条用例，`user_login()` 被执行过一次后，第二次则不需要重复执行，直接返回结果。
