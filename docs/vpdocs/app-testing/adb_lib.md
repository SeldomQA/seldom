# ADB 操作

App（Android)测试必然需要用到adb命令， seldom根据需要封装了几个常用的操作。

* 获取设备信息

```python
from seldom.utils.adbutils import ADBUtils

adb = ADBUtils()
devices = adb.refresh_devices()
print("当前连接设备:", devices)

# 设置默认设备 - 多设备的情况下,后续操作需要设置设备ID
if devices:
    adb.set_default_device(devices[0][0])
```

打印信息:

```shell
当前连接设备: [('MDX0220413011925', 'ELS-AN00')]
```

* 获取当前启动的app信息

```shell
from seldom.utils.adbutils import ADBUtils

adb = ADBUtils()

app_info = adb.get_app_info()
for info in app_info:
    print(info['package'], info["activity"])
```

打印信息

```shell
com.huawei.android.launcher com.huawei.android.launcher.unihome.UniHomeLauncher
com.hpbr.bosszhipin com.hpbr.bosszhipin.module.main.activity.MainActivity
com.android.mms com.android.mms.ui.ConversationList
com.tencent.mm com.tencent.mm.ui.LauncherUI
com.delivery.aggregator com.delivery.aggregator.activity.QYMainActivity
com.huawei.browser com.huawei.browser.BrowserMainActivity
com.huawei.android.launcher .unihome.UniHomeLauncher
com.hpbr.bosszhipin .module.main.activity.MainActivity
com.android.mms .ui.ConversationList
com.tencent.mm .ui.LauncherUI
com.delivery.aggregator .activity.QYMainActivity
com.huawei.browser .BrowserMainActivity
```

* 启动&关闭app

```python
import time
from seldom.utils.adbutils import ADBUtils

adb = ADBUtils()

package = "com.microsoft.bing"
if adb.launch_app(package):
    print(f"成功启动 {package}")
    time.sleep(5)
    if adb.close_app(package):
        print(f"成功关闭 {package}")
```

打印信息:

```shell
成功启动 com.microsoft.bing
成功关闭 com.microsoft.bing
```
 
