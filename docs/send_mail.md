### seldom 发邮件功能

如果你想将测试完成的报告发送到指定邮箱，那么可以调用发邮件的方法实现。

```python
import seldom
from seldom.mail import SMTP


class Test(seldom.TestCase):

    def test_case(self):
        self.get("http://www.baidu.com")
        self.type(css="#kw", text="seldom")
        self.click(css="#su")
        self.wait(2)
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main()
    smtp = SMTP(user="you@126.com", password="abc123", host="smtp.126.com")
    smtp.sender(to="receive@mail.com")
```

如果你自定义了报告的名称，那么需要指定报告名称。

```python
import seldom
from seldom.mail import SMTP

# ……

if __name__ == '__main__':
    report_path = "/you/path/to/report.html"
    seldom.main(report_name=report_path)
    smtp = SMTP(user="you@126.com", password="abc123", host="smtp.126.com")
    smtp.sender(to="receive@mail.com", attachments=report_path)

```

> 自动化发邮件不支持`debug` 模式，`debug`模式不会生成测试报告，自然也无法将报告发送到指定邮箱了。
