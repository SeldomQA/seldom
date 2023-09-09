# 浏览器与驱动


### 下载浏览器驱动

> seldom 2.3.0 版本集成webdriver_manager管理浏览器驱动。

和Selenium一样，在使用seldom运行自动化测试之前，需要先配置浏览器驱动，这一步非常重要。

seldom 集成 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) ，提供了`chrome/firefox/ie/edge/opera`浏览器驱动的自动下载。

> selenium 4.6 之后内置了 selenium-manager 可以自动管理浏览器驱动。 seldom 3.3 版本将 webdriver_manager 替换为官方的 selenium-manager。


__自动下载__

如果你不配置浏览器驱动也没关系，seldom会根据你使用的浏览器版本，自动化下载对应的驱动文件。

* 编写简单的用例

```python
import seldom


class BingTest(seldom.TestCase):

    def test_bing_search(self):
        """selenium api"""
        self.open("http://www.bing.com")
        self.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    seldom.main(browser="edge", debug=True)
```

__驱动检查逻辑:__

1. 首先判断 环境变量 `PATH` 是否配置了浏览器驱动。 通过`where` 查找命令位置，如果可以找到说明，已配置了，环境变量`PATH`。

```shell
> where msedgedriver
D:\webdriver\msedgedriver.exe
```

2. 如果没有找到浏览器驱动，会根据当前浏览器版本，查找对应驱动文件下载。 `selenium-manager` 可以查看浏览器驱动的默认安装路径。

```shell
> selenium-manager --driver msedgedriver
INFO    Driver path: C:\Users\xxx\.cache\selenium\msedgedriver\win64\116.0.1938.76\msedgedriver.exe
INFO    Browser path: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
```

__手动下载__

通过`seldom`命令下载浏览器驱动，基于 webdriver_manager (该库后续版本会移除)。

```shell
> seldom -install chrome
> seldom -install firefox
> seldom -install ie
> seldom -install edge
```

1. 默认下载到当前的`C:\Users\username\.wdm\drivers\` 目录下面。
2. Chrome: `chromedriver` 驱动，众所周知的原因，使用的taobao的镜像。
3. Safari: `safaridriver` （macOS系统自带，默认路径:`/usr/bin/safaridriver`）

通过 `selenium-manager` 命令下载浏览器驱动，需要知道每个浏览器驱动的名字。

```shell
> selenium-manager --driver chromedriver  # chrome
> selenium-manager --driver msedgedriver  # edge
> selenium-manager --driver geckodriver   # firefox
```

### 指定不同的浏览器

我们运行的自动化测试不可能只在一个浏览器下运行，我们分别需要在chrome、firefox浏览器下运行。在seldom中需要只需要修改一个配置即可。

```python
import seldom

# ……

if __name__ == '__main__':
    seldom.main(browser="chrome") # chrome浏览器,默认值
    seldom.main(browser="gc")     # google chrome简写
    seldom.main(browser="firefox") # firefox浏览器
    seldom.main(browser="ff")      # firefox简写
    seldom.main(browser="edge")    # edge浏览器
    seldom.main(browser="safari")  # safari浏览器
    seldom.main(browser="ie")      # internet explore浏览器
```

在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`Chrome`浏览器。
