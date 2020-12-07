## 实现用例的依赖

在编写用例的时候不推荐你编写依赖的用例，但是，有些时候我们并不能完全消除这些依赖。seldom 增加了用例依赖的方法。

* depend

`depend` 装饰器用来设置依赖的用例。

```python
import seldom
from seldom import depend


class TestDepend(seldom.TestCase):

    def test_001(self):
        self.get("https://www.runoob.com/try/try2.php?filename=bootstrap3-form-checkboxradio")
        self.switch_to_frame(id_="iframeResult")
        self.click(css='[type=checkbox]--error')  # 元素定位错误

    @depend("test_001")
    def test_002(self):
        self.click(xpath='//input[@type="checkbox"]', index=1)

    @depend("test_002")
    def test_003(self):
        self.click(id_='optionsRadios1')

if __name__ == '__main__':
    seldom.main(debug=True)
```

`test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。当`test_001`用例失败时，结果是这样的：

```shell
test_001 (cc.TestDepend) ... 2020-11-16 23:47:30 [INFO] ✅ Find element: id=iframeResult
ERROR
test_002 (cc.TestDepend) ... skipped 'test_001 failed  or  error or skipped'
test_003 (cc.TestDepend) ... skipped 'test_002 failed  or  error or skipped'

======================================================================
ERROR: test_001 (cc.TestDepend)
----------------------------------------------------------------------
...

----------------------------------------------------------------------
Ran 3 tests in 2.392s

FAILED (errors=1, skipped=2)
```

* if_depend

`id_depend` 装饰器不会依赖用例的执行状态，可以自己定义是否要跳过依赖的用例。

```python
import seldom
from seldom import if_depend

class TestIfDepend(seldom.TestCase):
    Test001 = True

    def test_001(self):
        self.get("https://www.baidu.com")
        TestIfDepend.Test001 = False  # 修改Test001为 False

    @if_depend("Test001")
    def test_002(self):
        self.get("http://news.baidu.com/")


if __name__ == '__main__':
    seldom.main(debug=True)
```

1. 首先，定义变量 `Test001`，默认值为`True`。
2. 在`test_001`用例中，可以根据一些条件来选择是否修改`Test001`的值，如果改为`False`， 那么依赖的用例将被跳过。
3. 在`test_002`用例中，通过`id_depend`装饰器来判断`Test001`的值，如果为为`False`， 那么装饰的用例跳过，否则执行。

执行结果：
```shell
test_001 (cc.TestIfDepend) ... ok
test_002 (cc.TestIfDepend) ... skipped 'Dependent use case not passed'

----------------------------------------------------------------------
Ran 2 tests in 0.497s

OK (skipped=1)
``` 