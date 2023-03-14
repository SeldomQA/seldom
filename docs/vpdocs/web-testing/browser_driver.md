# 浏览器与驱动


### 下载浏览器驱动

> seldom 2.3.0 版本集成webdriver_manager管理浏览器驱动。

和Selenium一样，在使用seldom运行自动化测试之前，需要先配置浏览器驱动，这一步非常重要。

seldom 集成 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) ，提供了`chrome/firefox/ie/edge/opera`浏览器驱动的自动下载。


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
    seldom.main(browser="gc", debug=True)
```

* 运行测试

```shell

> python selenium_sample.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info


[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 103.0.5060
[WDM] - Get LATEST chromedriver version for 103.0.5060 google-chrome
[WDM] - About to download new driver from https://registry.npmmirror.com/-/binary/chromedriver/103.0.5060.53/chromedriver_win32.zip
[WDM] - Driver has been saved in cache [C:\Users\fnngj\.wdm\drivers\chromedriver\win32\103.0.5060.53]
...
```

seldom 检测到的`Chrome`浏览器后，自动化下载对应版本的驱动，并保存到本地，以便于下次执行的时候就不需要下载了。

并且，非常贴心的将`chromedriver`的下载地址从 google 切换成了 taobao 的镜像地址。

__手动下载__

通过`seldom`命令下载浏览器驱动。

```shell
> seldom -install chrome
> seldom -install firefox
> seldom -install ie
> seldom -install edge
```

1. 默认下载到当前的`C:\Users\username\.wdm\drivers\` 目录下面。
2. Chrome: `chromedriver` 驱动，众所周知的原因，使用的taobao的镜像。
3. Safari: `safaridriver` （macOS系统自带，默认路径:`/usr/bin/safaridriver`）


指定浏览器驱动

> seldom 3.2.0版本通过新的方式指定浏览器驱动。

* chrome

```python
import seldom

# ...

if __name__ == '__main__':
    browser = {
        "browser": "chrome",
        "executable_path": f"D:\webdriver\chromedriver.exe"
    }
    seldom.main(browser=browser, tester="虫师")
```

* firefox

```python
import seldom

# ...

if __name__ == '__main__':
    browser = {
        "browser": "firefox",
        "executable_path": f"D:\webdriver\geckodriver.exe"
    }
    seldom.main(browser=browser, tester="虫师")
```

其他浏览器&驱动配置方式相同，指定 `browser` 名称 和 `executable_path` 驱动路径。

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
