### seldom 跳过测试用例

seldom 通过`main()`方法运行测试用例只能指定到测试文件，但有时候我们一个测试文件可能会有很多测试类和方法。但在调试过程中之想执行某一部分用例，那么就可以设置用例的跳过。

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
