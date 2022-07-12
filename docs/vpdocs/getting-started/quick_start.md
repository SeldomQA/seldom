# 快速开始

### 基本规范

`seldom`继承`unittest`单元测试框架，所以他的编写规范与[unittest](https://docs.python.org/3/library/unittest.html)基本保持一致。

```shell
# test_sample.py
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    seldom.main()
```

基本规范：

1. 创建测试类`YouTest`并继承`seldom.TestCase`类。
2. 创建测试方法`test_case`, 必须以`test`开头。
3. `seldom.mian()`是框架运行的入口方法，接下来详细介绍。


### `main()` 方法

`main()`方法是seldom运行测试的入口, 它提供了一些最基本也是最重要的配置。

```python
import seldom

# ...

if __name__ == '__main__':

    seldom.main(path="./",
                browser="chrome",
                base_url=None,
                report=None,
                title="百度测试用例",
                tester="虫师",
                description="测试环境:chrome",
                debug=False,
                rerun=0,
                save_last_run=False,
                language="en",
                timeout=None,
                whitelist=[],
                blacklist=[],
                open=True
    )
```

__参数说明__


* path : 指定测试目录或文件， 与`case`参数互斥。
* case : 指定测试用例， 与`path`参数互斥。
* browser : 针对Web UI测试需要指定浏览器（"chrome"、"firefox" 等）。
* base_url : 针对HTTP接口测试的参数，设置全局的URL。
* report : 自定义测试报告的名称，默认格式为`2020_04_04_11_55_20_result.html`。
* title : 指定测试报告标题。
* tester : 指定测试人员, 默认`Anonymous`。
* description : 指定测试报告描述。
* debug : debug模式，设置为True不生成测试HTML测试，默认为`False`。
* rerun : 设置失败重新运行次数，默认为 `0`。
* save_last_run : 设置只保存最后一次的结果，默认为`False`。
* language : 设置HTML报告中英文，默认`en`, 中文`zh-CN`。
* timeout : 设置超时时间，默认`10`秒。
* whitelist :  用例标签（label）设置白名单。
* blacklist :  用例标签（label）设置黑名单。
* open :  是否使用浏览器自动打开测试报告，默认`True`。

### 运行测试

> seldom 强烈建议通过命令行工具执行

1. 运行当前文件中的用例

创建 `test_sample.py` 文件，在要文件中使用`main()`方法，如下：

```py
# test_sample.py
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    seldom.main()  # 默认运行当前文件中的用例
```

`main()`方法默认运行当前文件中的所有用例。

```shell
> python test_sample.py      # 通过python命令运行
> seldom -r test_sample.py   # 通过seldom命令运行
```

2. 指定运行目录、文件

可以通过`path`参数指定要运行的目录或文件。

```py
# run.py
import seldom

seldom.main(path="./")  # 指定当前文件所在目录下面的用例。
seldom.main(path="./test_dir/")  # 指定当前目录下面的test_dir/ 目录下面的用例。
seldom.main(path="./test_dir/test_sample.py")  # 指定测试文件中的用例。
seldom.main(path="D:/seldom_sample/test_dir/test_sample.py")  # 指定文件的绝对路径。
```

* 运行文件

```shell
> python run.py
```

3. 指定单个类、方法执行

可以通过`case`参数指定要运行文件、类和方法。

> 注：如果指定了`case`参数，那么`path`参数将无效。

```python
# test_sample.py
import seldom
from seldom import data


class TestCase(seldom.TestCase):

    def test_case(self):
        """ sample case """
        pass

    @data([
        ("case1", "seldom"),
        ("case2", "XTestRunner"),
    ])
    def test_ddt(self, name, search):
        """ ddt case """
        print(f"name: {name}, search_key: {search}")


if __name__ == '__main__':
    seldom.main(case="test_sample")  # 指定当前文件
    seldom.main(case="test_sample.TestCase")  # 指定测试类
    seldom.main(case="test_sample.TestCase.test_case")  # 指定测试用例

    # 使用参数化的用例
    seldom.main(case="test_sample.TestCase.test_ddt")  # 错误用法
    seldom.main(case="test_sample.TestCase.test_ddt_0_case1")  # 正确用例
```

* 运行文件

```shell
> python test_sample.py
```

4. seldom命令指定单个类、方法

`seldom -m`命令可以提供更细粒度的运行。

```shell
> seldom -m test_sample # 运行 test_sample.py 文件
> seldom -m test_sample.SampleTest # 运行 SampleTest 测试类
> seldom -m test_sample.SampleTest.test_case # 运行 test_case 测试方法
```

> seldom命令指定类、方法有两个问题：
> 1. 不支持poium，如果要使用，必须手动给`Seldom.driver` 赋值浏览器驱动。
> 2. 如果是Web UI自动化测试，无法自动关闭浏览器，需要手动关闭浏览器`self.close()`


### 失败重跑

Seldom支持`错误`&`失败`重跑。

```python
# test_sample.py
import seldom


class YouTest(seldom.TestCase):

  
    def test_error(self):
        """error case"""
        self.assertEqual(a, 2)

    def test_fail(self):
        """fail case """
        self.assertEqual(1+1, 3)


if __name__ == '__main__':
    seldom.main(rerun=3, save_last_run=False)
```

参数说明：

* rerun: 指定重跑的次数，默认为 `0`。
* save_last_run: 设置是否只保存最后一次运行结果，默认为`False`。

运行日志：

```shell
> python test_sample.py


              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.x.x
-----------------------------------------
                             @itest.info



.\test_sample.py

XTestRunner Running tests...

----------------------------------------------------------------------
ERetesting... test_error (test_sample.YouTest)..1
ERetesting... test_error (test_sample.YouTest)..2
ERetesting... test_error (test_sample.YouTest)..3
EFRetesting... test_fail (test_sample.YouTest)..1
FRetesting... test_fail (test_sample.YouTest)..2
FRetesting... test_fail (test_sample.YouTest)..3
Generating HTML reports...
F2022-07-12 00:22:52 log.py | SUCCESS | generated html file: file:///D:\github\seldom\reports\2022_07_12_00_22_51_result.html
2022-07-12 00:22:52 log.py | SUCCESS | generated log file: file:///D:\github\seldom\reports\seldom_log.log
```

### 测试报告

seldom 默认生成HTML测试报告，在运行测试文件下自动创建`reports`目录。

* 运行测试用例前

```shell
mypro/
└── test_sample.py
```

* 运行测试用例后

```shell
mypro/
├── reports/
│   ├── 2020_01_01_11_20_33_result.html
│   ├── seldom_log.log
└── test_sample.py
```

通过浏览器打开 `2020_01_01_11_20_33_result.html` 测试报告，查看测试结果。

![](/image/report.png)


__debug模式__

如果不想每次运行都生成HTML报告，可以打开`debug`模式。

```py
import seldom

seldom.main(debug=True)
```

__定义测试报告__


```py
import seldom

seldom.main(report="./report.html",
            title="百度测试用例",
            tester="虫师",
            description="测试环境：windows 10/ chrome")
```

* report: 配置报告名称和路径。
* title: 自定义报告的标题。
* tester: 指定自动化测试工程师名字。
* description: 添加报告信息，支持列表, 例如：["OS: windows","Browser: chrome"]。

__XML测试报告__

如果需要生成XML格式的报告，只需要修改报告的后缀名为`.xml`即可。

```py
import seldom

seldom.main(report="report.xml")
```

