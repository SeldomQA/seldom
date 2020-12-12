## seldom 生成测试数据

测试数据是测试用例的重要部分。但有时候我们不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就要求我们随机生成新数据。

seldom提供了随机获取测试数据的方法。

```python
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
    seldom.main(path="test_sample.py")
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

__testdata还提供了更多的方法:__

* first_name()
* last_name()
* username()
* get_birthday()
* get_date()
* get_digits()
* get_email()
* get_float()
* get_future_datetime()
* get_int()
* get_int32()
* get_int64()
* get_md5()
* get_now_time()
* get_past_datetime()
* get_uuid()
* get_word()
* get_words()
* get_phone()
