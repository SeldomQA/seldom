# ADB 操作

App（Android)测试必然需要用到adb命令， seldom根据需要封装了几个常用的操作。

* 获取设备信息

```python
from seldom.extend_lib.adb import get_devices

devices = get_devices()
print(devices)
```

* 启动&关闭app

```python
import time
from seldom.extend_lib.adb import launch_app, close_app

launch_app("com.microsoft.bing")
time.sleep(3)
close_app("com.microsoft.bing")
```
