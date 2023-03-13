# 更多配置


### 开启headless模式

Firefox和Chrome浏览器支持`headless`模式，即将浏览器置于后台运行，这样不会影响到我们在测试机上完成其他工作。

```python
import seldom
from seldom import ChromeConfig

#...

if __name__ == '__main__':
    ChromeConfig.headless = True
    seldom.main(browser="chrome")
```

只需要将 ChromeConfig 类中的 headless 设置为 `True`即可， Firefox浏览器配置方法类似。

### 开放浏览器配置能力

seldom为了更加方便的使用驱动，屏蔽了浏览器的配置，为了满足个性化的需求，比如禁用浏览器插件，设置浏览器代理等。所以，通过ChromeConfig类的参数来开放这些能力。

* 浏览器忽略无效证书

```python
import seldom
from seldom import ChromeConfig
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略无效证书的问题
    ChromeConfig.options = chrome_options
    seldom.main(browser="chrome")
```

将要`ChromeOption`添加的设置赋值给`ChromeConfig`的`options`变量。

* 浏览器关闭沙盒模式

```python
import seldom
from seldom import ChromeConfig
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 关闭沙盒模式
    ChromeConfig.options = chrome_options
    ChromeConfig.headless = True
    seldom.main(browser="chrome")
```

* 开启实验性功能

chrome开启实验性功能参数 `excludeSwitches`。

```python

import seldom
from seldom import ChromeConfig
from selenium.webdriver import ChromeOptions


if __name__ == '__main__':
    option = ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    ChromeConfig.options = option
    seldom.main(browser="chrome")
```

### Selenium Grid

首先，安装Java环境，然后下载 `selenium-server`。

```shell
> java -jar selenium-server-4.3.0.jar standalone

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
from seldom import ChromeConfig

# ……
if __name__ == '__main__':
    ChromeConfig.command_executor = "http://10.2.212.3:4444"
    seldom.main(browser="chrome")

```

* 设置远程节点，[selenium Grid doc](https://www.selenium.dev/documentation/grid/getting_started/)。



### Page Objects设计模式

seldom API 的设计理念是将元素操作和元素定位放到起，本身不太适合实现`Page objects`设计模式。

[poium](https://github.com/SeldomQA/poium) 是`Page objects`设计模式最佳实践，如果想使用 poium，需要单独安装。

```shell
> pip install poium==1.1.6
```

将 seldom 与 poium 结合使用。

```python
import seldom
from poium import Page, Element


class BaiduPage(Page):
    """baidu page"""
    search_input = Element(id_="kw")
    search_button = Element(id_="su")


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    def test_case(self):
        """
        A simple test
        """
        page = BaiduPage(self.driver)
        page.open("https://www.baidu.com")
        page.search_input.send_keys("seldom")
        page.search_button.click()
        self.assertTitle("seldom_百度搜索")


if __name__ == '__main__':
    seldom.main(browser="chrome")
```