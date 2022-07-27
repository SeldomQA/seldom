# 高级用法

### 随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

seldom 提供了随机获取测试数据的方法。

```python
import seldom
from seldom import testdata


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        word = testdata.get_word()
        print(word)


if __name__ == '__main__':
    seldom.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

**更多的方法**

- first_name()
- last_name()
- username()
- get_birthday()
- get_date()
- get_digits()
- get_email()
- get_float()
- get_now_time()
- get_future_time()
- get_past_time()
- get_future_datetime()
- get_past_datetime()
- get_int()
- get_int32()
- get_int64()
- get_md5()
- get_uuid()
- get_word()
- get_words()
- get_phone()


### 用例的依赖

> 在 seldom 1.8.0 版本实现了该功能。

在编写用例的时候不推荐你编写依赖的用例，但是，有些时候我们并不能完全消除这些依赖。seldom 增加了用例依赖的方法。

**depend**

`depend` 装饰器用来设置依赖的用例。

```python
import seldom
from seldom import depend


class TestDepend(seldom.TestCase):

    def test_001(self):
        print("test_001")

    @depend("test_001")
    def test_002(self):
        print("test_002")

    @depend("test_002")
    def test_003(self):
        print("test_003")

if __name__ == '__main__':
    seldom.main(debug=True)
```

`test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。

**if_depend**

`id_depend` 装饰器不会依赖用例的执行状态，可以自己定义是否要跳过依赖的用例。

```python
import seldom
from seldom import if_depend

class TestIfDepend(seldom.TestCase):
    Test001 = True

    def test_001(self):
        TestIfDepend.Test001 = False  # 修改Test001为 False

    @if_depend("Test001")
    def test_002(self):
        ...


if __name__ == '__main__':
    seldom.main(debug=True)
```

1. 首先，定义变量 `Test001`，默认值为`True`。
2. 在`test_001`用例中，可以根据一些条件来选择是否修改`Test001`的值，如果改为`False`， 那么依赖的用例将被跳过。
3. 在`test_002`用例中，通过`id_depend`装饰器来判断`Test001`的值，如果为为`False`， 那么装饰的用例跳过，否则执行。

### 用例分类标签

> 在 seldom 2.4.0 版本实现了该功能。

**使用方式**

```python
# test_label.py
import seldom
from seldom import label


class MyTest(seldom.TestCase):

    @label("base")
    def test_label_base(self):
        self.assertEqual(1+1, 2)

    @label("slow")
    def test_label_slow(self):
        self.assertEqual(1, 2)

    def test_no_label(self):
        self.assertEqual(2+3, 5)


if __name__ == '__main__':
    # seldom.main(debug=True, whitelist=["base"])  # whitelist
    seldom.main(debug=True, blacklist=["slow"])    # blacklist
```

如果只运行标签为`base`的用例，设置白名单（whitelist）。

```shell
> python test_label.py

test_label_base (btest_label.MyTest) ... ok
test_label_slow (btest_label.MyTest) ... skipped "label whitelist {'base'}"
test_no_label (btest_label.MyTest) ... skipped "label whitelist {'base'}"

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK (skipped=2)
```

如果只想屏蔽标签为`slow`的用例，设置黑名单（blacklist）。

```shell
> python test_label.py

test_label_base (btest_label.MyTest) ... ok
test_label_slow (btest_label.MyTest) ... skipped "label blacklist {'slow'}"
test_no_label (btest_label.MyTest) ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK (skipped=1)
```

### 发送邮件

> 在 seldom 1.2.4 版本实现了该功能。

如果你想将测试完成的报告发送到指定邮箱，那么可以调用发邮件的方法实现。

```python
import seldom
from seldom import SMTP

# ...

if __name__ == '__main__':
    report_path = "/you/path/report.html"
    seldom.main(report=report_path)
    smtp = SMTP(user="send@126.com", password="abc123", host="smtp.126.com")
    smtp.sendmail(to="receive@mail.com", subject="Email title", attachments=report_path, delete=False)
```

- `subject`: 邮件标题，默认:`Seldom Test Report`。
- `to`: 添加收件人，支持多个收件人: `["aa@mail.com", "bb@mail.com"]`。
- `attachments`: 设置附件，默认发送 HTML 测试报告。
- `delete`: 是否删除报告&日志。（在服务器上运行自动化，每次都会产生一份报告和日志，手动删除比较麻烦。）

> `debug`模式不会生成测试报告， 自动化发邮件不支持`debug` 模式，自然也无法将报告发送到指定邮箱了。

### 发送钉钉

> 在 seldom 2.6.0 版本实现了该功能。

seldom 还提供了发送钉钉的 API。

帮助文档:
https://open.dingtalk.com/document/group/enterprise-created-chatbot

```python
import seldom
from seldom import DingTalk

# ...

if __name__ == '__main__':
    seldom.main()
    ding = DingTalk(
        access_token="690900b5ce6d5d10bb1218b8e64a4e2b55f96a6d116aaf50",
        key="xxxx",
        app_secret="xxxxx",
        at_mobiles=[13700000000, 13800000000],
        is_at_all=False,
    )
    ding.sender()
```

__参数说明:__

- `access_token`: 钉钉机器人的 access_token
- `key`: 如果钉钉机器人安全设置了关键字，则需要传入对应的关键字。
- `app_secret`: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
- `at_mobiles`: 发送通知钉钉中要@人的手机号列表，如：[137xxx, 188xxx]。
- `is_at_all`: 是否@所有人，默认为 False, 设为 True 则会@所有人。


### seldom日志

> 在 seldom 2.9.0 版本提供了日志的配置能力。

在项目中你可以使用seldom提供的`log` 打印日志。

* 使用log

```python
from seldom.logging import log

log.trace("this is trace info.")
log.info("this is info.")
log.error("this error info.")
log.debug("this debug info.")
log.success("this success info.")
log.warning("this warning info.")
```

* 运行日志

```shell

2022-04-30 16:31:49 test_log.py | TRACE | this is trace info.
2022-04-30 16:31:49 test_log.py | INFO | this is info.
2022-04-30 16:31:49 test_log.py | ERROR | this error info.
2022-04-30 16:31:49 test_log.py | DEBUG | this debug info.
2022-04-30 16:31:49 test_log.py | SUCCESS | this success info.
2022-04-30 16:31:49 test_log.py | WARNING | this warning info.
```

* 关闭日志颜色

```python
from seldom.logging import log_cfg
from seldom.logging import log


log_cfg.set_level(colorlog=False)  # 关闭日志颜色
log.trace("this is trace info.")
# ...
```

* 自定义日志格式

```python
from seldom.logging import log_cfg
from seldom.logging import log


# 定义日志格式
format = "<green>{time:YYYY-MM-DD HH:mm:ss}</> {file} |<level> {level} | {message}</level>"
log_cfg.set_level(format=format)
log.trace("this is trace info.")
```

* 日志级别

```python
from seldom.logging import log_cfg
from seldom.logging import log

# 设置日志级别
log_cfg.set_level(level="DEBUG")
log.trace("this is trace info.")
log.error("this error info.")
```

> log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR


### 缓存 cache

> 在 seldom 2.10.0 版本实现了该功能。

实际测试过程中，往往需要需要通过cache去记录一些数据，从而减少不必要的操作。例如 登录token，很多条用例都会用到登录token，那么就可以借助缓存来暂存登录token，从而减少重复动作。

```python
from seldom.utils import cache

# 清除指定缓存
cache.clear("token")

# 清除所有缓存
cache.clear()

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")
if token is None:
    # 写入缓存
    cache.set({"token": "123"})

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")

# 获取所有缓存
all_token = cache.get()
print(f"all: {all_token}")
```

> 注：seldom 提供的 `cache` 本质上是通过json文件来临时记录数据，没有失效时间。你需要在适当的位置做清除操作。例如，整个用例开始时清除。
