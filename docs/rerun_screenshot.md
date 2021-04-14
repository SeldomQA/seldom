## Rerun & Screenshot

Web自动化测试常常因为各种原因导致用例失败，而重跑机制可以进一步帮我们确定用例确实是失败了。在seldom中设置失败重跑非常简单。

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
    seldom.main(rerun=3, save_last_run=False)
```

__说明__

* rerun: 指定重跑的次数，默认为 `0`。
* save_last_run: 是否保存保存最后一次运行结果，默认为`False`。

__运行日志__

```shell
> seldom -r test_sample.py

2021-04-14 11:25:53,265 INFO Run the python version:
2021-04-14 11:25:53,265 - INFO - INFO Run the python version:
Python 3.7.1

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/
-----------------------------------------
                             @itest.info


DevTools listening on ws://127.0.0.1:12699/devtools/browser/301751bd-a833-44d1-8669-aa85d418b302
2021-04-14 23:31:54 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
ERetesting... test_case (test_demo.YouTest)..1
2021-04-14 23:32:05 [INFO] 📖 https://www.baidu.com
2021-04-14 23:32:06 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
ERetesting... test_case (test_demo.YouTest)..2
2021-04-14 23:32:17 [INFO] 📖 https://www.baidu.com
2021-04-14 23:32:22 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
ERetesting... test_case (test_demo.YouTest)..3
2021-04-14 23:32:32 [INFO] 📖 https://www.baidu.com
2021-04-14 23:32:36 [INFO] ✅ Find 1 element: id=kw , input 'seldom'.
2021-04-14 23:32:47 [INFO] generated html file: file:///D:\github\seldom\reports\2021_04_14_23_31_51_result.html
E
```

__测试报告__

![](image/report.png)


__说明__

1、如果只想查看最后一次的结果，`save_last_run` 设置为`True`。

2、查看截图，点击报告中的`show`链接。
