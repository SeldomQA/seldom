# 浏览器启动配置

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

__Standalone__

独立运行，只需要启动一个服务，默认端口`4444`。

```shell
> java -jar selenium-server-4.31.0.jar standalone
```

__Hub和Node__

Hub和Node是一种分布式模式，由Hub管理Node执行。

* 启动Hub主节点

```shell
> java -jar selenium-server-4.31.0.jar hub
```

* 启动Node分支节点

```shell
> java -jar selenium-server-4.31.0.jar node
```

* 启动远程Node节点

```shell
java -jar selenium-server-4.31.0.jar node --hub http://<hub-ip>:4444
```

注：由于hub和远程node不同的主机，所以远程node需要指定Hub的IP地址（即`<hub-ip>`）

__Seldom使用__

下面是Seldom框架中如何指定 Selenium Server 地址来运行测试用例。

```python
import seldom
from selenium.webdriver import ChromeOptions

# ……

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    browser = {
        "options": chrome_options,  # chrome浏览器配置，其他类似
        "command_executor": "http://192.168.0.202:4444",  # selenium server 地址
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

### 浏览器忽略无效证书

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

### 浏览器关闭沙盒模式

```python
import seldom
from selenium.webdriver import ChromeOptions

# ...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')  # 关闭沙盒模式
    browser = {
        "browser": "chrome",
        "options": chrome_options,
    }
    seldom.main(browser=browser)
```

### 开启实验性功能

chrome开启实验性功能参数 `excludeSwitches`。

```python

import seldom
from selenium.webdriver import ChromeOptions

# ...

if __name__ == '__main__':
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    browser = {
        "browser": "chrome",
        "options": chrome_options,
    }
    seldom.main(browser=browser)
```

### 设置浏览器代理

```python
import seldom
from selenium.webdriver import ChromeOptions

# ...

if __name__ == '__main__':
    proxy = "127.0.0.1:1080"  # 示例代理地址和端口

    chrome_options = ChromeOptions()
    chrome_options.add_argument(f"--proxy-server={proxy}")
    browser = {
        "browser": "chrome",
        "options": chrome_options,
    }
    seldom.main(browser=browser)
```

### 连接已打开浏览器

* 查看浏览器安装位置

```shell
> selenium-manager.exe  --browser edge
[2024-10-08T03:50:40.000Z INFO ] Driver path: C:\Users\xx\.cache\selenium\msedgedriver\win64\130.0.2849.13\msedgedriver.exe
[2024-10-08T03:50:40.000Z INFO ] Browser path: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
```

* 启动浏览器

```shell
msedge.exe  --remote-debugging-port=9527 --user-data-dir="D:\webdriver\edge"
```

`--remote-debugging-port`: 浏览器远程调试端口。

`--user-data-dir`: 用户数据目录，创建一个空目录用于保存浏览器用户数据数据。

* 启动浏览器指定端口

```python
import seldom
from selenium.webdriver import EdgeOptions

# ...

if __name__ == '__main__':
    option = EdgeOptions()
    # 设置连接已打开浏览器
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    browser = {
        "browser": "edge",
        "options": option
    }
    seldom.main(browser=browser)

```
