# 更多配置

selenium 在启动浏览器的时候可以做很多配置，seldom 试图简化这些配置，但是总有很多情况兼顾不到。

> `seldom 3.2` 版本开放了这些配置，你只需要将配置传给 seldom 即可。 

### 使用headless模式

Firefox和Chrome浏览器支持`headless`模式，将浏览器置于后台运行，这样不会影响到我们在测试机上完成其他工作。

* chrome

```python
import seldom
from selenium.webdriver import ChromeOptions

#...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.headless = True  # 开启 headless 模式
    browser = {
        "browser": "chrome",
        "option": chrome_options
    }
    seldom.main(browser=browser)
```

* firefox

```python
import seldom
from selenium.webdriver import FirefoxOptions
#...

if __name__ == '__main__':
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("-headless")  # 开启 headless 模式
    browser = {
        "browser": "firefox",
        "option": firefox_options
    }
    seldom.main(browser=browser)
```

### Selenium Grid

首先，安装Java环境，然后下载 `selenium-server`。

```shell
> java -jar selenium-server-4.8.1.jar standalone

00:25:28.023 INFO [LoggingOptions.configureLogEncoding] - Using the system default encoding
00:25:28.029 INFO [OpenTelemetryTracer.createTracer] - Using OpenTelemetry for tracing
00:25:36.978 INFO [NodeOptions.getSessionFactories] - Detected 16 available processors
00:25:37.012 INFO [NodeOptions.discoverDrivers] - Discovered 3 driver(s)
00:25:37.043 INFO [NodeOptions.report] - Adding Chrome for {"browserName": "chrome"} 16 times
00:25:37.045 INFO [NodeOptions.report] - Adding Firefox for {"browserName": "firefox"} 16 times
00:25:37.046 INFO [NodeOptions.report] - Adding Edge for {"browserName": "MicrosoftEdge"} 16 times
00:25:38.260 INFO [Node.<init>] - Binding additional locator mechanisms: id, name, relative
00:25:38.281 INFO [GridModel.setAvailability] - Switching Node 373df045-cf78-4d52-84c0-d99fd2c7a374 (uri: http://10.2.212.3:4444) from DOWN to UP
00:25:38.282 INFO [LocalDistributor.add] - Added node 373df045-cf78-4d52-84c0-d99fd2c7a374 at http://10.2.212.3:4444. Health check every 120s
00:25:42.503 INFO [Standalone.execute] - Started Selenium Standalone 4.3.0 (revision a4995e2c09*): http://10.2.212.3:4444
```

```python
import seldom


# ……
if __name__ == '__main__':
    browser = {
        "browser": "chrome",  # or "firefox"
        "command_executor": "http://10.2.212.3:4444",
    }
    seldom.main(browser=browser)

```

* 设置远程节点，[selenium Grid doc](https://www.selenium.dev/documentation/grid/getting_started/)。

### Mobile Web 模式

seldom 还支持 Mobile web 模式：

```python
import seldom
from selenium.webdriver import ChromeOptions

#...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 8"})
    
    browser = {
        "browser": "chrome",
        "option": chrome_options,
    }
    seldom.main(debug=True, browser=browser)
```

* deviceName: 指定移动设备的型号。

> 移动设备通过通过 浏览器开发者工具 查看，参考型号：
> 'iPhone 8', 'iPhone 8 Plus', 'iPhone SE', 'iPhone X', 'iPhone XR', 'iPhone 12 Pro',
'Pixel 2', 'Pixel XL', 'Pixel 5', 'Samsung Galaxy S8+', 'Samsung Galaxy S20 Ultra',
'iPad Air', 'iPad Pro', 'iPad Mini'。


### 更多浏览器配置

* 浏览器忽略无效证书

```python
import seldom
from selenium.webdriver import ChromeOptions

#...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略无效证书的问题
    browser = {
        "browser": "chrome",
        "option": chrome_options,
    }
    seldom.main(browser=browser)
```


* 浏览器关闭沙盒模式

```python
import seldom
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 关闭沙盒模式
    browser = {
        "browser": "chrome",
        "option": chrome_options,
    }
    seldom.main(browser=browser)
```

* 开启实验性功能

chrome开启实验性功能参数 `excludeSwitches`。

```python

import seldom
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    browser = {
        "browser": "chrome",
        "option": chrome_options,
    }
    seldom.main(browser=browser)
```
