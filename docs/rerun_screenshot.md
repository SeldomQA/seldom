## 用例失败重跑&自动截图

Web自动动测试常常因为各种原因导致用例失败，而重跑机制可以进一步帮我们确定用例确实是失败了。在seldom中设置失败重跑非常简单。

```python
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text="seldom")
        self.click(css="#su_error")
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main(path="test_sample.py",
                rerun=3,
                save_last_run=False,
    )
```

说明：

* rerun: 指定重跑的次数，默认为 `0`。
* save_last_run: 是否保存保存最后一次运行结果，默认为`False`。

运行日志：

```shell
seldom -r test_sample.py
2020-01-04 11:25:53,265 INFO Run the python version:
2020-01-04 11:25:53,265 - INFO - INFO Run the python version:
Python 3.7.1

            _      _
           | |    | |
 ___   ___ | |  __| |  ___   _ __ ___
/ __| / _ \| | / _` | / _ \ | '_ ` _ \
\__ \|  __/| || (_| || (_) || | | | | |
|___/ \___||_| \__,_| \___/ |_| |_| |_|
-----------------------------------------
                             @itest.info


DevTools listening on ws://127.0.0.1:12699/devtools/browser/301751bd-a833-44d1-8669-aa85d418b302
2020-01-04 11:26:00,705 INFO Find element: id=kw
2020-01-04 11:26:00,705 - INFO - INFO Find element: id=kw
2020-01-04 11:26:10,917 ERROR Find 0 elements through：css selector=#su_error
2020-01-04 11:26:10,917 - ERROR - ERROR Find 0 elements through：css selector=#su_err or
ERetesting... test_case (test_sample.YouTest)..1
2020-01-04 11:26:11,466 INFO Find element: id=kw
2020-01-04 11:26:11,466 - INFO - INFO Find element: id=kw
2020-01-04 11:26:21,647 ERROR Find 0 elements through：css selector=#su_error
2020-01-04 11:26:21,647 - ERROR - ERROR Find 0 elements through：css selector=#su_err or
ERetesting... test_case (test_sample.YouTest)..2
2020-01-04 11:26:22,158 INFO Find element: id=kw
2020-01-04 11:26:22,158 - INFO - INFO Find element: id=kw
2020-01-04 11:26:32,343 ERROR Find 0 elements through：css selector=#su_error
2020-01-04 11:26:32,343 - ERROR - ERROR Find 0 elements through：css selector=#su_err or
ERetesting... test_case (test_sample.YouTest)..3
2020-01-04 11:26:33,559 INFO Find element: id=kw
2020-01-04 11:26:33,559 - INFO - INFO Find element: id=kw
2020-01-04 11:26:43,757 ERROR Find 0 elements through：css selector=#su_error
2020-01-04 11:26:43,757 - ERROR - ERROR Find 0 elements through：css selector=#su_err or
generated html file: file:///D:\git\seldom\reports\2020_01_04_11_25_53_result.html
E
```

测试报告：

![](image/report.png)


__说明：__

1、如果只想查看最后一次的结果，`save_last_run` 设置为`True`。

2、查看截图，点击报告中的`show`链接。
