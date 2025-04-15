# 介绍

## 新书推荐

<p>
  <a href="https://item.jd.com/10124939676219.html">
    <img alt="京东链接" src="/image/book.jpg" style="width: 360px; margin-right: 140px;" />
  </a>
</p>

京东 [购买链接](https://item.jd.com/14859108.html)

天猫 [购买链接](https://detail.tmall.com/item.htm?id=852715481274&skuId=5817727406269)

当当 [购买链接](https://product.dangdang.com/29809610.html)

依托于 SeldomQA 相关项目的开发和维护，在 `自动化测试框架设计`、 `定制化测试报告设计`、 `设计模式`，以及`测试平台开发`
方面有着深厚技术积累和独特的设计理念。

一本真正介绍 __自动化测试框架设计__ 的书终于出版了，书中浅显易懂的介绍了 SeldomQA
相关项目中的诸多设计和封装技术。并且，介绍了`一个开源自动化测试框架从设计到发布的整个流程`。
如果你正在使用SeldomQA相关项目之余，想了解他们背后的设计，那么这本书非常值得购买。

## seldom框架

### 特点

> seldom 是基于 unittest 的全功能自动化测试框架；针对自动化测试达到开箱即用。

__seldom特点__

* 支持测试类型（web/app/api)
* 丰富的断言
* 生成随机测试数据
* 用例依赖
* 用例分类标签
* 支持发送（邮件、钉钉、飞书、企微）消息等
* 日志打印
* 缓存cache
* 命令行工具
* 强大的数据驱动（JSON/YAML/CSV/EXCEL）
* HTML/XML报告
* 失败重跑&截图
* 数据库操作（MySQL/sqlite3/Mongodb）
* 支持平台化

### 设计理念

简单一句话就是回到最初写代码的样子。

自动化测试框架很多，只有在测试领域有一个比较奇怪的现象，如何用不写代码的方式解决自动化问题。为此，我们发明了用特定领域语言写用例，发明了用
excel 写用例，发明了用 YAML/JSON 写用例。这些方案看似简化了用例的编写，但是，会让解决复杂的问题变得更复杂。比如实现个分支判断/循环，传递参数，调用封装的步骤，编程语言中用
if/for 、变量、函数就实现了，但是用非编程语言的方式写用例处理起来就很麻烦。最终，并不能完全脱离编程，那么为什么不一开始就选择一个编程框架呢？

然而，seldom的定位是尽量用简单的设计去解决复杂问题，例如
Flask、requests、yagmail...等，这些框架/库都有一个共同的特点，用简单的方式去解决复杂的问题，在编程语言这个层面，并不会给你太多限制，你可以完全使用它，也可以只用一部分，也可以平滑的实现它不支持的功能。

seldom的目标以就让你用最少的代码编写自动化测试用例，当遇到seldom没有的功能，你可以方便的进行扩展。-- 这就是seldom的设计理念。

### 发展历史

2015年7月15号我在github上提交一个自动化项目，命名为：`pyse`， 即各取了`python` 和 `selenium`前两个字符。项目非常简单核心就三个文件。

* `pyse.py`：针对 selenium API做了简单封装。
* `HTMLTestRunner.py`: 修改的HTMLTestRunner报告。
* `TestRunner.py`: 一个简单的 unittest运行器。

之后项目断断续续的在维护，直到2019年，也许是太闲了，加上对UI自动化有了更深入的理解，重新投入主要精力维护pyse项目。

后来就需要将提交到pypi，这样更方便通过pip安装，发现 `pyse` 早已经被占用了，后来更名为`seldom`
，其实命名没有太多寓意，就是看他长得和`selenium`比较接近。

2020年1月发布1.0版本，之所以发布1.0
是因为自认为框架的功能比较成熟了，并且花费时间补充了文档。大家都不重视文档，其实文档非常重要，也需要花大量的时间更新和维护。有时候你加个功能很简单，编写说明文档和使用示例就要花费等同的时间。

1.0 版本之后，项目核心围绕着 selenium API的封装 和 unittest框架扩展（seldom基于unittest）等。

2021年4月正式发布 2.0，集成requests, 正式支持http接口测试。起因是发现cypress支持http调用，哦，原来UI测试工具也可以去做接口，格局一下子打开了！如何在不影响现有selenium
API的情况下集成requests是2.0考虑的重点。

2022年1月seldom项目正式在公司内部推广使用，当时我们做了几版的接口测试平台，平台的开发维护成本比较高，对于复杂的场景用例，编写成本比框架还要复杂简单；功能也依赖于平台所提供的，相比较而言，框架却有最大的灵活性，可以很好的基于业务做各种设计和封装。

因为在公司得到推广使用，seldom明显进入了更加快速的迭代开发阶段，并且稳定性、可用性灰得到了很大的提升。

seldom 3.0 背景
seldom集成App测试是顺理成章的事情，早在几个月前我已经在公司项目中尝试 seldom + appium
进行App自动化测试。App自动化的维护成本确实比接口要高许多，这是由App本身的特点决定的，框架很难做到实质上的改变。

2022年10月seldom 3.0 beta发布，之所以选择appium有几个原因：

* appium 是由商业工具在维护，历史比较长，不会随意停止维护。
* appium 应用更加广泛，使用得人更多，支持得平台多（android/ios/flutter）
* appium 继承selenium，对于seldom来说对原有API改动最小。

目前，seldom 3.0 正式版已经发布，欢迎使用。

### seldom vs pytest

seldom 是建立在 unittest 的基础上的自动化测试框架。与 pytest进行对比，无疑相当于像拿一台`电脑`与一颗 intel `CPU` 进行比较，虽然
intel `CPU` 很强大，但我们无法直接拿一个`CPU`打游戏，对吧? pytest 就像一个 `CPU`
，虽然很强大，但无法直接拿来做自动化测试，比如配合各种测试库。而seldom不需要额外安装测试库，即可开始编写自动化测试用例。

* seldom vs pytest 对比差异

| 功能            | seldom                                     | pytest                                |
|---------------|--------------------------------------------|---------------------------------------|
| web UI测试      | 支持 ✅                                       | 支持(需安装 selenium) ⚠️                   |
| web UI断言      | 支持（assertText、assertTitle、assertElement） ✅ | 不支持 ❌                                 |
| playwright    | 支持（需安装playwright） ⚠️                       | 支持(playwright提供playwright-pytest插件) ✅ |
| 失败截图          | 支持（自动实现） ✅                                 | 支持（需要设置） ✅                            |
| http接口测试      | 支持 ✅                                       | 支持（需安装 requests） ⚠️                   |
| http接口断言      | 支持（assertJSON、assertPath、assertSchema） ✅   | 不支持 ❌                                 |
| app UI测试      | 支持 ✅                                       | 支持（需安装 appium） ⚠️                     |
| Page Object模式 | 支持（推荐poium） ✅                              | 支持（推荐poium） ✅                         |
| 脚手架           | 支持（快速创建项目） ✅                               | 不支持 ❌                                 |
| 生成随机测试数据      | 支持`testdata` ✅                             | 不支持 ❌                                 |
| 发送消息          | 支持（email、钉钉、飞书、微信）✅                        | 不支持 ❌                                 |
| log日志         | 支持 ✅                                       | 不支持 ❌                                 |
| 数据库操作         | 支持（sqlite3、MySQL、SQL Server） ✅             | 不支持 ❌                                 |
| 用例依赖          | 支持`@depend()` ✅                            | `@pytest.mark.dependency()`支持 ✅       |
| 失败重跑          | 支持`rerun` ✅                                | pytest-rerunfailures 支持 ✅             |
| 用例分类标签        | 支持`@label()` ✅                             | `@pytest.mark.xxx`支持 ✅                |
| HTML测试报告      | 支持 ✅                                       | pytest-html、allure ✅                  |
| XML测试报告       | 支持 ✅                                       | 自带 `--junit-xml` ✅                    |
| 数据驱动方法        | `@data()` ✅                                | `@pytest.mark.parametrize()`  ✅       |
| 数据驱动文件        | `@file_data()`(JSON\YAML\CSV\Excel) ✅      | 不支持 ❌                                 |
| 钩子函数          | `confrun.py`用例运行钩子 ⚠️                      | `conftest.py` 功能更强大 ✅                 |
| 命令行工具CLI      | 支持`seldom` ✅                               | 支持`pytest` ✅                          |
| 并发执行          | 不支持 ❌                                      | pytest-xdist、pytest-parallel ✅        |
| 平台化           | 支持（seldom-platform）✅                       | 不支持 ❌                                 |
| 第三方插件         | seldom（unittest）的生态比较糟糕 ⚠️                 | pytest有丰富插件生态 ✅                       |

__说明__

* ✅  : 表示支持。

* ⚠️: 支持，但支持的不好，或没有对方好。

* ❌  : 不支持，表示框架没有该功能，第三方插件也没有。

## 框架学习

B站实战视频：https://www.bilibili.com/video/BV1QHQVYoEHC
