# 浏览器与驱动

### 管理浏览器驱动

> seldom 2.3.0 版本集成webdriver_manager管理浏览器驱动。
>
> seldom 3.3.0 版本移除了webdriver_manager，selenium 4.6 之后内置了 selenium-manager 可以自动管理浏览器驱动。

#### 自动下载

如果你不配置浏览器驱动也没关系，seldom(selenium)会根据你使用的浏览器版本，自动化下载对应的驱动文件。

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

selenium驱动检查逻辑:

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

#### 手动下载

通过 `selenium-manager` 命令下载浏览器驱动，需要知道每个浏览器驱动的名字。

```shell
> selenium-manager --driver chromedriver  # chrome
> selenium-manager --driver msedgedriver  # edge
> selenium-manager --driver geckodriver   # firefox
```

### 指定浏览器驱动

虽然，`selenium-manager`可以方便的管理浏览器驱动，但`selenium-manager`自动下载浏览器驱动很慢，有些环境也不是方便。

> seldom 3.7 版本重新支持 `executable_path` 参数，指定浏览器驱动。

```python
import seldom

# ……

if __name__ == '__main__':
    browser = {
        "browser": "chrome",
        "executable_path": "D:\webdriver\chromedriver.exe",  # 设置chrome浏览器驱动位置，其他浏览器类似。
    }
    seldom.main(browser=browser)
```

### 指定不同的浏览器

我们运行的自动化测试不可能只在一个浏览器下运行，我们分别需要在chrome、firefox浏览器下运行。在seldom中需要只需要修改一个配置即可。

```python
import seldom

# ……

if __name__ == '__main__':
    seldom.main(browser="chrome")  # chrome浏览器,默认值
    seldom.main(browser="gc")  # google chrome简写
    seldom.main(browser="firefox")  # firefox浏览器
    seldom.main(browser="ff")  # firefox简写
    seldom.main(browser="edge")  # edge浏览器
    seldom.main(browser="safari")  # safari浏览器
    seldom.main(browser="ie")  # internet explore浏览器
```

在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`Chrome`浏览器。

### 控制浏览器启动和关闭

seldom 默认通过`seldom.main(browser="edge")`全局设置浏览器的启动和关闭，一般我们不需要关心浏览器的启动和关闭。

> seldom 3.9.0 支持手动控制浏览器的驱动和关闭。

* 每个用例启动和关闭浏览器。

```python
import seldom


class WebTestOne(seldom.TestCase):
    """case lunch browser"""

    def start(self):
        self.browser("edge")

    def end(self):
        self.quit()

    def test_baidu(self):
        self.open("http://www.baidu.com")
        ...

    def test_bing(self):
        self.open("http://cn.bing.com")
        ...


if __name__ == '__main__':
    seldom.main()
```

* 每个类启动和关闭浏览器。

```python
import seldom


class WebTestTwo(seldom.TestCase):
    """class lunch browser"""

    @classmethod
    def start_class(cls):
        cls.browser(cls, "gc")

    @classmethod
    def end_class(cls):
        cls.quit(cls)

    def test_baidu(self):
        self.open("http://www.baidu.com")
        ...

    def test_bing(self):
        self.open("http://cn.bing.com")
        ...


if __name__ == '__main__':
    seldom.main()
```

* 打开一个新的浏览器

seldom 默认会启动一个浏览器，在运行的过程中需要打开一个新的浏览器执行其他操作，可以使用`new_browser()`方法。

```python
import seldom


class WebTestNew(seldom.TestCase):
    """Web search test case"""

    def test_new_browser(self):
        # default browser
        self.open("http://www.baidu.com")
        self.Keys(css="#kw").input("seldom").enter()
        self.sleep(2)
        self.screenshots()
        self.assertInTitle("seldom")

        # open new browser
        browser = self.new_browser()
        browser.open("http://cn.bing.com")
        browser.type(id_="sb_form_q", text="seldom", enter=True)
        self.sleep(2)
        browser.screenshots()


if __name__ == '__main__':
    seldom.main(browser="edge")
```
