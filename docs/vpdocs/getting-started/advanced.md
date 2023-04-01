# 高级用法

### fixture

有时自动化测试用例的运行需要一些前置&后置步骤，seldom提供了相应的方法。

__start & end__

针对每条用例的fixture，可以放到`start()/end()`方法中。

```python
import seldom


class TestCase(seldom.TestCase):

    def start(self):
        print("一条测试用例开始")

    def end(self):
        print("一条测试结果")

    def test_search_seldom(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="seldom")

    def test_search_poium(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="poium")

```

__start_class & end_class__

针对每个测试类的fixture，可以放到`start_class()/end_class()`方法中。

```python
import seldom


class TestCase(seldom.TestCase):
    
    @classmethod
    def start_class(cls):
        print("测试类开始执行")

    @classmethod
    def end_class(cls):
        print("测试类结束执行")

    def test_search_seldom(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="seldom", clear=True)

    def test_search_poium(self):
        self.open("https://www.baidu.com")
        self.type_enter(id_="kw", text="poium", clear=True)

```

> 警告：不要把用例的操作步骤写到fixture方法中! 因为它不属于某条用例的一部分，一旦里面的操作步骤运行失败，测试报告都不会生成。

### 跳过测试

seldom 提供了跳过用例的装饰用于跳过暂时不执行的用例。

__装饰器__

* skip: 无条件地跳过一个测试。
* skip_if： 如果条件为真，则跳过测试。
* skip_unless: 跳过一个测试，除非条件为真。
* expected_failure: 预期测试用例会失败。

__使用方法__

```python
import seldom

@seldom.skip()  # 跳过测试类
class YouTest(seldom.TestCase):

    @seldom.skip()  # 跳过测试用例
    def test_case(self):
        ...


if __name__ == '__main__':
    seldom.main()
```

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

```python
from seldom.testdata import *


# 随机一个名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))
print("名字(中文男)：", first_name(gender="male", language="zh"))
print("名字(中文女)：", first_name(gender="female", language="zh"))

# 随机一个姓
print("姓:", last_name())
print("姓(中文):", last_name(language="zh"))

# 随机一个姓名
print("姓名:", username())
print("姓名(中文):", username(language="zh"))

# 随机一个生日
print("生日:", get_birthday())
print("生日字符串:", get_birthday(as_str=True))
print("生日年龄范围:", get_birthday(start_age=20, stop_age=30))

# 日期
print("日期(当前):", get_date())
print("日期(昨天):", get_date(-1))
print("日期(明天):", get_date(1))

print("当月：", get_month())
print("上个月：", get_month(-1))
print("下个月：", get_month(1))

print("今年：", get_year())
print("去年：", get_year(-1))
print("明年：", get_year(1))

# 数字
print("数字(8位):", get_digits(8))

# 邮箱
print("邮箱:", get_email())

# 浮点数
print("浮点数:", get_float())
print("浮点数范围:", get_float(min_size=1.0, max_size=2.0))

# 随机时间
print("当前时间:", get_now_datetime())
print("当前时间(格式化字符串):", get_now_datetime(strftime=True))
print("未来时间:", get_future_datetime())
print("未来时间(格式化字符串):", get_future_datetime(strftime=True))
print("过去时间:", get_past_datetime())
print("过去时间(格式化字符串):", get_past_datetime(strftime=True))

# 随机数据
print("整型:", get_int())
print("整型32位:", get_int32())
print("整型64位:", get_int64())
print("MD5:", get_md5())
print("UUID:", get_uuid())

print("单词:", get_word())
print("单词组(3个):", get_words(3))

print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))
```

* 运行结果

```shell
名字： Hayden
名字（男）： Brantley
名字（女）： Julia
名字（中文男）： 觅儿
名字（中文女）： 若星
姓: Lee
姓（中文）: 白
姓名: Genesis
姓名（中文）: 廉高义
生日: 2000-03-11
生日字符串: 1994-11-12
生日年龄范围: 1996-01-12
日期（当前）: 2022-09-17
日期（昨天）: 2022-09-16
日期（明天）: 2022-09-18
数字(8位): 48285099
邮箱: melanie@yahoo.com
浮点数: 1.5315717275531858e+308
浮点数范围: 1.6682402084146244
当前时间: 2022-09-17 23:33:22.736031
当前时间(格式化字符串): 2022-09-17 23:33:22
未来时间: 2054-05-02 11:33:47.736031
未来时间(格式化字符串): 2070-08-28 16:38:45
过去时间: 2004-09-03 12:56:23.737031
过去时间(格式化字符串): 2006-12-06 07:58:37
整型: 7831034423589443450
整型32位: 1119927937
整型64位: 3509365234787490389
MD5: d0f6c6abbfe1cfeea60ecfdd1ef2f4b9
UUID: 5fd50475-2723-4a36-a769-1d4c9784223a
单词: habitasse
单词组（3个）: уж pede. metus.
手机号: 13171039843
手机号(移动): 15165746029
手机号(联通): 16672812525
手机号(电信): 17345142737
```

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

`if_depend` 装饰器不会依赖用例的执行状态，可以自己定义是否要跳过依赖的用例。

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
3. 在`test_002`用例中，通过`if_depend`装饰器来判断`Test001`的值，如果为为`False`， 那么装饰的用例跳过，否则执行。

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
    smtp = SMTP(user="send@126.com", password="abc123", host="smtp.126.com", ssl=True)
    smtp.sendmail(to="receive@mail.com", subject="Email title", attachments=report_path, delete=False)
```

__SMTP()类__

- `user`: 邮箱用户名。
- `password`: 邮箱密码。
- `host`: 邮箱服务地址。
- `ssl`: `True` 使用 `SMTP_SSL()`，`False` 使用 `SMTP()`，两种方式应对不同的邮箱服务。

__sendmail()方法__
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

* cache

```python
from seldom.utils import cache

# 清除指定缓存
cache.clear()

# 获取指定缓存
token = cache.get("token")
print(f"token: {token}")

# 判断为空写入缓存
if token is None:
    cache.set({"token": "123"})

# 设置存在的数据(相当于更新)
cache.set({"token": "456"})

# value复杂格式设置存在的数据
cache.set({"user": [{"name": "tom", "age": 11}]})


# 获取所有缓存
all_token = cache.get()
print(f"all: {all_token}")

# 清除指定缓存
cache.clear("token")
```

> 注：seldom 提供的 `cache` 本质上是通过json文件来临时记录数据，没有失效时间。你需要在适当的位置做清除操作。例如，整个用例开始时清除。

* memery_cache

使用内存的实现的cache 装饰器。

```python
import time
import seldom
from seldom.utils import memory_cache


@memory_cache()
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    time.sleep(2)
    c = x + y
    return c


class MyTest(seldom.TestCase):

    def test_case(self):
        """test cache 1"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case2(self):
        """test cache 2"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case3(self):
        """test cache 3"""
        r = add(1, 2)
        self.assertEqual(r, 3)


if __name__ == '__main__':
    seldom.main(debug=True)
```

* disk_cache

使用磁盘实现的cache 装饰器。

```python
import time
import seldom
from seldom.utils import disk_cache


@disk_cache()
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    time.sleep(2)
    c = x + y
    return c


class MyTest(seldom.TestCase):

    def test_case(self):
        """test cache 1"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case2(self):
        """test cache 2"""
        r = add(1, 2)
        self.assertEqual(r, 3)

    def test_case3(self):
        """test cache 3"""
        r = add(1, 2)
        self.assertEqual(r, 3)


if __name__ == '__main__':
    dc = disk_cache()
    # 清除所有函数缓存
    # dc.clear()
    # 清除 `add()` 函数缓存
    dc.clear("add")
    seldom.main(debug=True)
```
