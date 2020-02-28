## 切换浏览器

我们运行的自动化测试不可能只在一个浏览器下运行，我们分别需要在chrome、firefox浏览器下运行，有时候甚至需要无界面模式。

在seldom中需要只需要修改一个配置即可。

```python
import seldom

# ……

if __name__ == '__main__':
    seldom.main(browser="chrome") # chrome浏览器,默认值
    seldom.main(browser="firefox") # firefox浏览器
    seldom.main(browser="ie")  # IE浏览器
    seldom.main(browser="opera") # opera浏览器
    seldom.main(browser="edge") # edge浏览器
    seldom.main(browser="safari") # safari浏览器
    seldom.main(browser="chrome_headless") # chrome浏览器headless模式
    seldom.main(browser="firefox_headless") # Firefox浏览器headless模式

```

在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`Chrome`浏览器。

## 安装浏览器驱动

虽然说安装浏览及驱动是做Web UI 自动化的前提，但是，浏览器驱动的下载安装和设置总是难倒了一部分新手。

seldom 提供了下载浏览器驱动的命令。

__下载`Chrome`浏览器驱动：__

```shell
seldom -install chrome
```

注：众所周知的原因，chromedriver使用的taobao的镜像。

__下载`Firefox`浏览器驱动：__

```shell
seldom -install firefox
```

默认下载到当前的`lib/` 目录下面，将`lib/` 目录添加环境变量`path`。

如果你连添加环境变量`path`都不会，没关系！你可以在seldom中指定浏览器驱动文件目录的绝对路径。

```python
import seldom

# ……
if __name__ == '__main__':
    seldom.main(path="test_sample.py",
                browser="chrome",
                driver_path="D:\git\seldom\lib\chromedriver.exe")

```

注：浏览器要`browser`与驱动`driver_path` 要保持对应关系。


## 支持远程节点（Selenium Grid）


首先，安装Java环境，然后下载 `selenium-server`。

```shell
> java -jar selenium-server-standalone-3.141.59.jar
```

运行自动化测试，指定 `grid_url`。

```python
import seldom

# ……
if __name__ == '__main__':
    seldom.main(path="test_sample.py",
                browser="chrome",
                grid_url="http://127.0.0.1:4444/wd/hub")

```
