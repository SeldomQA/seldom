## 浏览器与驱动

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

除此之外，还支持 Mobile web 模式：

```python
import seldom

#...

if __name__ == '__main__':
    seldom.main(browser="iPhone 6") # iPhone 6 手机浏览器展示
```

支持的设备类型，如下：

```python

PHONE_LIST = [
    'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8', 'iPhone 8 Plus',
    'iPhone X', 'Pixel 2', 'Pixel XL', "Galaxy S5"
]
PAD_LIST = ['iPad', 'iPad Pro']

```

## 开启headless模式

Firefox和 Chrome浏览器支持`headless` 模式，即将浏览器置于后台运行，这样不会影响到我们在测试机上完成其他工作。

```python
import seldom
from seldom import ChromeConfig

#...

if __name__ == '__main__':
    ChromeConfig.headless = True
    seldom.main(browser="chrome")
```

只需要将 ChromeConfig 类中的 headless 设置为 `True`即可， Firefox浏览器配置方法类似。

## 开放Chrome浏览器配置能力

seldom为了更加方便的使用驱动，屏蔽了浏览器的配置，但架不住部分个性化的需求，比如禁用浏览器插件，设置浏览器代理等。所以，通过ChromeConfig类的参数来开放这些能力。

例如，浏览器忽略无效证书的问题。

```python
import seldom
from seldom import ChromeConfig
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略无效证书的问题
    ChromeConfig.chrome_options = chrome_options
    seldom.main(browser="chrome")
```

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
from seldom.driver import ChromeConfig

# ……
if __name__ == '__main__':
    ChromeConfig.executable_path = "D:\git\seldom\lib\chromedriver.exe"
    seldom.main(browser="chrome")
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
    seldom.main(browser="chrome",
                grid_url="http://127.0.0.1:4444/wd/hub")

```

## 驱动下载地址

当然，你也可以手动下载不同浏览器驱动：

geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver
