## seldom vs pytest

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
