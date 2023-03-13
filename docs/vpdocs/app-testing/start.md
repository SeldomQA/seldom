# app 测试

`seldom 3.0` 基于appium支持APP测试。

appium 官方网站：https://appium.io/

## 环境安装

app 的自动化测试环境相比较 web 要复杂一些，请参考appium官方。

1. 安装node

https://nodejs.org/en/

```shell
> node --version
v16.17.0
```

2. 安装appium

```shell
> npm install -g appium  # get appium 1.x
> npm install -g appium@next # get appium 2.x
```

3. 启动appium

```shell
> appium
[Appium] Welcome to Appium v2.0.0-beta.43
[Appium] Appium REST http interface listener started on 0.0.0.0:4723
```

4. 移动设备

准备一台设备（Android/iOS手机）通过USB数据线连接电脑。通过以下工具确认手机与电脑是否连接。

* adb
```shell
> adb devices 
List of devices attached
UMXDU000000000000       device
```

* taobao-iphone-device
```shell
> tidevice list
List of apple devices attached
00008030-00000000000000 xxx的iPhoneSE
```


## 编写测试

基于seldom编写app自动化测试, 由于appium 继承自selenium，所以，部分API共用。

```python
import seldom


class TestBBS(seldom.TestCase):

    def test_bbs_search(self):
        self.click(id_="com.meizu.flyme.flymebbs:id/nw")
        self.type(id_="com.meizu.flyme.flymebbs:id/nw", text="flyme")
        self.click(id_="com.meizu.flyme.flymebbs:id/o1")
        self.sleep(2)
        elems = self.get_elements(id_="com.meizu.flyme.flymebbs:id/a29")
        for title in elems:
            print(title.text)
            self.assertIn("lyme", title.text)


if __name__ == '__main__':
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'appPackage': 'com.meizu.flyme.flymebbs',
        'appActivity': '.ui.LoadingActivity',
        'noReset': True,
    }
    seldom.main(app_info=desired_caps, app_server="http://127.0.0.1:4723")
```

> 注：上面的测试用例隐含了appium的一些知识点，你需要对appium有足够的了解。


* 运行日志

```shell
python test_app.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.0.0
-----------------------------------------
                             @itest.info


XTestRunner Running tests...

----------------------------------------------------------------------
2022-10-03 00:01:30 webdriver.py | INFO | 💤️ sleep: 5s.
2022-10-03 00:01:35 webdriver.py | INFO | ✅ Find 1 element: id=com.meizu.flyme.flymebbs:id/nw  -> click.
2022-10-03 00:01:36 webdriver.py | INFO | ✅ Find 1 element: id=com.meizu.flyme.flymebbs:id/nw  -> input 'flyme'.
2022-10-03 00:01:37 webdriver.py | INFO | ✅ Find 1 element: id=com.meizu.flyme.flymebbs:id/o1  -> click.
2022-10-03 00:01:37 webdriver.py | INFO | 💤️ sleep: 2s.
2022-10-03 00:01:39 webdriver.py | INFO | ✅ Find 5 element: id=com.meizu.flyme.flymebbs:id/a29 .
flyme的屏幕色彩显示应该是比较差的

魅族17的Flyme9状态栏下拉问题。

flyme9.3连上耳机来电话还是会外放

flyme自带录屏功能吗？

关于Flyme 8.18.0A稳定版


Generating HTML reports...
.12022-10-03 00:01:40 runner.py | SUCCESS | generated html file: file:///D:\github\seldom\reports\2022_10_03_00_01_23_result.html
2022-10-03 00:01:40 runner.py | SUCCESS | generated log file: file:///D:\github\seldom\reports\seldom_log.log
```
