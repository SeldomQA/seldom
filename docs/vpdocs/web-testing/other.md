# 更多配置

selenium 在启动浏览器的时候可以做很多配置，seldom 试图简化这些配置，但是总有很多情况兼顾不到。

> `seldom 3.2` 版本开放了这些配置，你只需要将配置传给 seldom 即可。

### 使用headless模式

Firefox和Chrome浏览器支持`headless`模式，将浏览器置于后台运行，这样不会影响到我们在测试机上完成其他工作。

* chrome

```python
import seldom
from selenium.webdriver import ChromeOptions

# ...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")  # 开启 headless 模式
    browser = {
        "browser": "chrome",
        "options": chrome_options
    }
    seldom.main(browser=browser)
```

* firefox

```python
import seldom
from selenium.webdriver import FirefoxOptions

# ...

if __name__ == '__main__':
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("-headless")  # 开启 headless 模式
    browser = {
        "browser": "firefox",
        "options": firefox_options
    }
    seldom.main(browser=browser)
```

* edge

```python
import seldom
from selenium.webdriver import EdgeOptions

# ...

if __name__ == '__main__':
    edge_option = EdgeOptions()
    edge_option.add_argument("--headless=new")

    browser = {
        "browser": "edge",
        "options": edge_option
    }
    seldom.main(browser=browser)
```

### Selenium Grid

首先，安装Java环境，然后下载 `selenium-server`。

```shell
> java -jar .\selenium-server-4.12.0.jar standalone

23:17:59.476 INFO [LoggingOptions.configureLogEncoding] - Using the system default encoding
23:17:59.481 INFO [OpenTelemetryTracer.createTracer] - Using OpenTelemetry for tracing
23:18:03.933 INFO [NodeOptions.getSessionFactories] - Detected 16 available processors
23:18:03.935 INFO [NodeOptions.discoverDrivers] - Looking for existing drivers on the PATH.
23:18:03.935 INFO [NodeOptions.discoverDrivers] - Add '--selenium-manager true' to the startup command to setup drivers automatically.
23:18:04.971 INFO [SeleniumManager.lambda$runCommand$1] - Driver path: C:\webdriver\chromedriver.exe
23:18:04.971 INFO [SeleniumManager.lambda$runCommand$1] - Browser path: C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
23:18:05.469 INFO [SeleniumManager.lambda$runCommand$1] - Driver path: D:\webdriver\msedgedriver.exe
23:18:05.470 INFO [SeleniumManager.lambda$runCommand$1] - Browser path: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
23:18:05.847 INFO [SeleniumManager.lambda$runCommand$1] - Driver path: C:\Users\fnngj\.cache\selenium\geckodriver\win64\0.33.0\geckodriver.exe
23:18:05.848 INFO [SeleniumManager.lambda$runCommand$1] - Browser path: C:\Program Files\Mozilla Firefox\firefox.exe
23:18:06.223 WARN [SeleniumManager.lambda$runCommand$1] - Unable to discover proper IEDriverServer version in offline mode
23:18:06.246 INFO [NodeOptions.report] - Adding Edge for {"browserName": "MicrosoftEdge","ms:edgeOptions": {"args": ["--remote-allow-origins=*"]},"platformName": "Windows 11"} 16 times
23:18:06.247 INFO [NodeOptions.report] - Adding Firefox for {"browserName": "firefox","platformName": "Windows 11"} 16 times
23:18:06.249 INFO [NodeOptions.report] - Adding Chrome for {"browserName": "chrome","goog:chromeOptions": {"args": ["--remote-allow-origins=*"]},"platformName": "Windows 11"} 16 times
23:18:06.343 INFO [Node.<init>] - Binding additional locator mechanisms: relative
23:18:06.360 INFO [GridModel.setAvailability] - Switching Node 35d0ca88-221c-4dba-8ad5-08b20a1280fc (uri: http://192.168.0.202:4444) from DOWN to UP
23:18:06.361 INFO [LocalDistributor.add] - Added node 35d0ca88-221c-4dba-8ad5-08b20a1280fc at http://192.168.0.202:4444. Health check every 120s
23:18:07.915 INFO [Standalone.execute] - Started Selenium Standalone 4.12.0 (revision 249f2a7d1b*): http://192.168.0.202:4444
```

```python
import seldom
from selenium.webdriver import ChromeOptions

# ……

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    browser = {
        "options": chrome_options,  # chrome浏览器配置，其他类似
        "command_executor": "http://192.168.0.202:4444",
    }
    seldom.main(browser=browser)
```

* 设置远程节点，[selenium Grid doc](https://www.selenium.dev/documentation/grid/getting_started/)。

### Mobile Web 模式

seldom 还支持 Mobile web 模式：

```python
import seldom
from selenium.webdriver import ChromeOptions

# ...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone 8"})

    browser = {
        "browser": "chrome",
        "options": chrome_options,
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

# ...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略无效证书的问题
    browser = {
        "browser": "chrome",
        "options": chrome_options,
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
        "options": chrome_options,
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
        "options": chrome_options,
    }
    seldom.main(browser=browser)
```
