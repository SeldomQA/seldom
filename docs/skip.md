## 跳过测试用例

seldom 提供了跳过用例的装饰用于跳过暂时不执行的用例。


__相关方法：__

* `skip`: 无条件地跳过一个测试。
* `skip_if`： 如果条件为真，则跳过测试。
* `skip_unless`: 跳过一个测试，除非条件为真。
* `expected_failure`: 预期测试用例会失败。


```python
import seldom

@seldom.skip()  # 跳过测试类
class YouTest(seldom.TestCase):

    @seldom.skip()  # 跳过测试用例
    def test_case(self):
        # ...


if __name__ == '__main__':
    seldom.main()
```

你可以通过 `skip()`装饰器设置要跳过的测试类或用例。
