### 3.10.0

* 重要：所有app/web元素定位支持`selector`模式，详细查看文档。
* 更新：`sleep()`增加默认值1s，也支持随机休眠范围：`self.seep((1, 3))`。
* 更新： `appium_lab`模块的 `Action()` 类下面的方法支持自定义休眠时间、间隔时间等。
* 修复：`Steps()`类的 `open()` 方法默认传url报错 [#241](https://github.com/SeldomQA/seldom/issues/241)。
* 告警：`type_enter()`添加移除警告，推荐使用`type()`。
* 文档：
    * 修改playwright使用示例。
    * 增加pyAutoGUI使用示例。

### 3.9.1

* 更新：脚手架项目模板，增加`run.py`文件。
* 修复：生成随机数，获取在线时间接口错误。
* 修复：`datetime.utcnow()`在Python 3.12 告警。
* App测试：
    * 修复`back()`、`home()`方法报错。
    * 增加`long_press_key()`方法。
* API测试：
    * 增加`assertStatusOk()`断言方法，断言接口返回状态码`200`。
    * `@check_response()`装饰器重命名`@api()`，更简洁。
* Web测试：
    * 增加`prompt_value()`方法，支持弹窗输入 [#166](https://github.com/SeldomQA/seldom/issues/166)。
    * 增加`action_chains()`方法，返回Selenium的`ActionChains()`
      类对象 [#119](https://github.com/SeldomQA/seldom/issues/119)。
    * 增加`is_visible()`方法，检查页面元素是否可见 [#62](https://github.com/SeldomQA/seldom/issues/62)。
    * `Pycharm`右键运行Web UI用例，抛异常提示。
* 文档更新：
    * 增加浏览器代理设置示例 [#31](https://github.com/SeldomQA/seldom/issues/31)。
    * 操作已打开浏览器示例 [#174](https://github.com/SeldomQA/seldom/issues/174)。
* 升级：`XTestRunner==1.8.0`。

### 3.9.0

* App测试。
    * 升级`Appium-Python-Client==4.1.0`
    * 提供`UiAutomator2Options`和`EspressoOptions`类，替换appium提供的这个两个类。
    * 移除不再支持的API: `launch_app()`、`close_app()`、`reset()`。
    * 增加App相关操作时的日志。
* Web测试浏览启动重构。
    * 支持`start/end`启动和关闭浏览器。
    * 支持`start_class/end_class`启动和关闭浏览器。
    * 支持`new_browser()`重新打开一个浏览器。
    * `self.open()` 检测到没有指定浏览器，不再默认启动一个`Chrome()`浏览器。
    * 链式API `Steps()`类添加`browser`参数。
* `Seldom.driver`对象支持多线程。
* `log`日志显示当前运行的线程。
* `Cache`缓存类支持多线程。
* 其他：移除直接依赖库：`requests`和`websocket-client`, 使用间接依赖。
    * `XTestRunner` -> `requests`
    * `Appium-Python-Client` -> `selenium` -> `websocket-client`

### 3.8.1

* App测试。
    * 支持`Appium-Python-Client==4.0.1`，修复`4.0.0` 引起的问题。
* `seldom` 命令，创建项目命令区分`web/app/api`项目。
* 修复`seldom-platform`平台运行错误。

### 3.8.0

* API测试：支持执行Excel测试用例, `seldom --api-excel api_case.xlsx` 具体用法查看文档。
* App：增加 `self.keyboard_search()`模拟键盘上的搜索按键。
* 优化: `@file_data()`参数化装饰器代码。

### 3.7.1

* 优化：`main()` 中的`path`参数支持列表，可以指定多个目录或文件。
* 新增：提供`from seldom.utils.send_extend import RunResult` 获取用例的执行数据。
* App测试。
    * 增加`swipe_right()`左滑 和 `swipe_left()`右滑支持。
    * `AppiumLab()` 默认允许不传`driver`参数。
* 其他：
    * `Python 3.12` 测试通过。

### 3.7.0

* `@data()`数据驱动装饰器增加`cartesian=True`参数，支持笛卡尔积。
* 新增`WebSocket`接口测试支持。
* App测试。
    * 支持`Appium-Python-Client==4.0.0`，修复`4.0.0` 引起的问题。
* Web测试
    * 重新支持指定浏览器驱动，使用`executable_path`参数。
* 其他：
    * 基于`selenium`依赖库，移除 `Python 3.7` 支持。

### 3.6.0

* `seldom.main()`方法增加`failfast`参数，debug模式，允许第一条用例失败，停止执行。
* 增加`@retry()`装饰器，用于函数&方法错误重试。
* HTTP测试
    * 支持`swagger`文档转seldom用例，使用命令 `seldom -s2c swagger.json` 。
    * 文档：增加 API Object model 概念的介绍，以及seldom中的应用。

### 3.5.0

* 新增：支持 Postgre SQL 数据库操作。
* web测试
    * `pause()` 用于暂停操作。
    * 移除`webdriver_manager_extend.py`文件（之前漏移除文件）。
* App测试
    * 支持`appium 2.0` 正式版。
    * 支持appium-OCR-plugin插件。
    * 增加`click_image()`方法，支持图片点击定位。
    * `press_key()` 支持`ENTER`参数，模拟键盘回车。

### 3.4.1

* 修复：`diff_json()` 对比特殊数据的异常没有捕捉到。
* web测试
    * `screenshots()` 增加`images`参数，支持传入截图对象 [#202](https://github.com/SeldomQA/seldom/issues/202)。
    * `open_electron()` 增加`chromedriver_path`参数，支持手动指定驱动地址。
* `setUpClass()`/`tearDownClass()` 增加异常捕捉，避免报错之后，用例无法统计的问题。

### 3.4.0

* 新增：`dependent_func()`装饰器，支持用例方法依赖调用，具体使用参考文档。
* api测试
    * 修复：har2case 请求头参数类型判断不准的问题。
* web测试
    * 增加`open_electron()` 方法，支持启动桌面electron应用。
    * 键盘操作`Key()`支持链式调用，例如: `self.Keys(id_="kw").select_all().cut()` 全选并删除。
* cache操作日志增加 emoji。
* 修复：`diff_json()` 优化，支持dict深度排序。 [#197](https://github.com/SeldomQA/seldom/issues/197)

### 3.3.0

* web测试
    * 浏览器驱动`webdriver-manager` 替换为`selenium-manager`。
    * 增加`execute_cdp_cmd()` 方法。
* 随机数据
    * `online_timestamp()` 在线获取时间戳。
    * `online_now_datetime()` 在线获取当前时间，格式为：`%Y-%m-%d %H:%M:%S`。
* 增加运行时内嵌（built-in）方法：`base_url()`、`driver()` - 无需导入，可以在自动化程序任意位置使用这两个方法。
* 移除`parameterized` 库的依赖，改为内置。
* 修复：`diff_json()` 对比 `[{}]` 数据时报错。 [#197](https://github.com/SeldomQA/seldom/issues/197)

### 3.2.3

* HTTP自动化
    * `confrun.py` 支持 `mock_url` hook 钩子函数。
    * 增加 `self.base_url` 获取 `base_url`。
* Web自动化
    * 更新：`get_elements()` 增加`empty`参数，设置为`True`, 允许返回空列表 `[]`
    * 更新： `debug=True` 模式，移除操作元素边框高亮，提高用例执行速度。
* App测试
    * 修复：`key_text()` 无法输入点号`.`的问题。
* 优化：`seldom_log.log` 文件只记录一次运行结果，减少文件大小。
* 升级：`webdriver_manager==4.0.0`  [#189](https://github.com/SeldomQA/seldom/issues/189)
* 其他： 添加 `pyproject.toml` 支持。
* 文档：增加其他库的使用例子。

### 3.2.2

* 功能：增加`@threads()`支持多线程运行用例。
* 功能：增加`@rerun()` 重复执行某个测试方法。
* 功能：数据库操作
    * `MySQLDB()`、`MSSQLDB()` 支持`charset` 参数设置字符集。
    * `init_table()` 批量插入数据库增加`clear` 参数，可以选择是否删除表再插入。
* 功能：Web自动化
    * 新增`save_screenshot()` 截图保存本地。
    * 修改`screenshots()` 自动截图保存到HTML报告，移除`file_path` 参数。
    * 修改`element_screenshot()` 元素截图保存到HTML报告，移除`file_path` 参数。
    * `type()` 方法增加 `click` 参数，针对app元素优化，app的输入框往往需要点击以下锁定光标再输入。
* 修复：浏览器配置参数 `option` 更名为 `options`。
* 其他：增加 python3.11 支持。

### 3.2.1

* 功能：增加`@disk_cache()`、`@memory_cache()` 缓存装饰器。
* 功能：app测试，seldom支持本身API支持appium定位。
* 功能：db操作，增加`insert_get_last_id()` 方法，插入数据并返回id。
* 修复：`@data_class()` 必传`input_values` 参数问题。
* 修复：设置log等级，HTML报告无法根据等级打印日志问题。

### 3.2.0

* Web UI测试，增加一组新的警告框 alert 操作。
    * `self.alert.text`
    * `self.alert.accept()`
    * `self.alert.dismiss()`
    * `self.alert.send_keys("text")`
* App UI测试。
    * `AppiumLab()` 类增加 `context()` 方法获取当前上下文。
    * `AppiumLab()` 类增加 `size()` 当前窗口尺寸。
* API 测试。
    * 增加`self.patch()` 请求方法。
    * 增加`self.json_to_dict()` 支持单引号JSON格式转字典。
* cache 增加文件锁，防止多线程读写错误（Windows不支持 fcntl）
* 支持 `XTestRunner=>1.6.2` 版本
    * XML格式的报告支持 rerun 重跑参数。
    * HTML 报告skip用例样式微调。
    * HTML 重跑只显示最后一次结果。
    * SMTP 发送报告增加 `ssl` 参数。
* `seldom.main()` 方法 ⚠ 不兼容更新
    * 移除 `save_last_run` 参数。
    * `browser` 参数支持`dict` 格式, 所有和浏览器配置相关的有发生修改。 包括
        * 设置浏览器驱动地址。
        * 设置 headless 模式。
        * 设置 options 参数。
        * 设置 selenium grid 地址。

### 3.1.3

* 功能：`file_data()` 增加`end_line`
  参数，对于csv/excel文件支持读取到第几行结束。[#163](https://github.com/SeldomQA/seldom/issues/163)
* 优化：`self.assertElement()` 断言元素时间过长的问题。
* 优化：`self.assertJSON()` 断言日志，区分告警和错误。
* 移除：`self.jresponse()` 方法。

### 3.1.2（internal）

> 内部版本：移除了日志打印的 emoji 表情。

* 功能：`seldom.main()` 方法 path 参数支持斜杠路径`\`（windows系统用`\` 表示路径）。

### 3.1.1

* 功能：`confrun.py` 增加`start_run()/end_run()` 钩子函数，用于运行前/后相关配置。
* 优化：`@api_data()` 装饰器增加 `headers` 参数。
* 优化：`assertJSON()` 断言增加 `exclude` 参数，屏蔽检查的字段，例如 `["start_time", "token"]`。
* 修复：`rediscover()` 查找用例bug。
* 依赖：升级`XTestRunner==1.5.0` 支持飞书/微信发送消息。

### 3.1.0

* 功能：提供 `confrun.py` 运行配置文件，配合 `seldom` 命令使用。
* 功能：Web测试，增加 `self.get_log()` 方法。
* 升级：`webdriver_manager==3.8.5` ，支持Mac M1芯片的浏览器驱动。[#159](https://github.com/SeldomQA/seldom/issues/159)
* 修复：seldom-platform平台同步多个项目引起的Bug。[#158](https://github.com/SeldomQA/seldom/issues/158)
* 修复：Web测试， `self.close()` 关闭浏览器Bug。

### 3.0.1

* 功能：支持 `SQL Server` 数据库支持，需要单独安装`pymssql`库。
* 功能：http接口测试增加`curl()`方法，支持请求转 `cURL`。
* 功能：`seldom` 命令增加`--log-level` 参数，log类型：`TRACE`, `DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR` 等。

### 3.0.0

* `seldom 3.0` 的核心是支持app测试，并且相关API已稳定，目的已达到，接下来将会在`3.0`基础上继续开发。
* 功能：`collect_cases()` 支持 `warning` 参数。

### 3.0.0beta2

* 修复：
    * 接口测试: 接口返回文本`r.text` 中文乱码问题。[#146](https://github.com/SeldomQA/seldom/issues/146)
    * app测试：感谢 @986379041
        * `install_app()` 错误
        * `close_app()` 错误
* 功能：
    * `TestMainExtend` 类增加 `tester`参数。 [#149](https://github.com/SeldomQA/seldom/issues/149)
    * 生成随机数，增加`get_month()` 和 `get_year()`方法。 [#152](https://github.com/SeldomQA/seldom/issues/152)
    * seldom命令增加清除所有缓存。`> seldom --clear-cache true`。 [#153](https://github.com/SeldomQA/seldom/issues/153)
* 其他:
    * seldom 运行用例，优化内存使用。

### 3.0.0beta1

* 支持App测试
    * 依赖`Appium-Python-Client`库。
    * `main()` 增加 `app_info`, `app_server` 参数。
    * 增加`appium_lab` 模块。
    * 增加`AppDriver` 类。
* 优化：基于pylint检查分析工具 优化代码。
* 其他：
    * 生成随机数，增加`get_timestamp()` 获取当前时间戳。
    * 数据库查询，增加`query_one()` 查询一条数据。

### 2.10.6 ~ 2.10.7

* 功能：`seldom`命令重大更新，支持更多参数和功能。
* 功能：`@file_data()` 当设置`Seldom.env`时支持更深一级遍历。
* 修复：`diff_json()` 对比数据错误。

### 2.10.4 ~ 2.10.5

* 重构log日志打印。 @Yongchin
    * 彻底修复日志重复打印的问题。
    * 移除`log.printf()` 非标准日志类型。
* 修复:
    * `sender()` 发送完邮件，`seldom_log.log` 文件无法删除的问题。
    * `TestMainExtend` 类`run_cases()`按照用例的顺序执行。@luna-CY
    * 修复`request` 带上`url=` 参数时异常。 @986379041@qq.com
* 依赖：`webdriver_manager`依赖升级到`3.8.2`
* 移除：`Opera` 浏览器的支持，selenium 4 已经移除了对opera的单独驱动支持。

### 2.10.3

* 数据驱动：`@data()` 和 `@file_data()` 优化用例名称和描述。
* 增加`Seldom.env`环境配置变量，`@file_data()` 数据驱动装饰器支持环境变量。
* 修复：`Edge`浏览器启动错误。
* 修复：HTTP接口测试`self.post()`方法 `data`参数不是dict类型错误。
* 平台化支持：优化用例收集，具体查看文档。

### 2.10.2

*

更新：移动模式列表更新，去掉旧设备，增加新设备 [link](https://github.com/SeldomQA/seldom/blob/master/docs/vpdocs/other/other.md)

* 功能：测试报告显示断言信息。
* 功能：`main()` 通过`open=False`可以控制运行完测试 不自动化打开测试报告。
* Web 测试：
    * 增加`self.new_browser()` 可以打开新的浏览器，但只能使用`selenium` 的 API
    * 增加`switch_to_frame_parent` 切换到上一级表单，[#118](https://github.com/SeldomQA/seldom/issues/118)。
    * 优化`assertNotElement` 执行慢的情况 [#120](https://github.com/SeldomQA/seldom/issues/120)
* HTTP 测试：
    * 优化：JSON日志进行格式化打印。

### 2.10.1

* 修复：seldom log 问题引起，错误信息无法在控制台打印。

> 2.10.0 为了解决[107](https://github.com/SeldomQA/seldom/issues/107)
> 问题，我们经过反复的讨论和优化，甚至对相关库XTestRunner做了修改；以为完美解决了这个问题，没想到还是引起了一些严重的错误。为此，我们感到非常沮丧，退回到2.9.0的实现方案。请升级到2.10.1版本。

### 2.10.0

* seldom log功能：
    * 修复打印日志显示固定文件的问题  [107](https://github.com/SeldomQA/seldom/issues/107)。
    * log方法变更：`log.warn()` -> `log.warning()`。
* 功能：提供了`cache` 类来模拟缓存。
* 功能：`@data()` 装饰器支持 `dict` 格式。
* 功能：`self.jresponse()` 方法设计不合理，给以废弃提示；可以使用`self.jsonpath()`/`self.jmespath()` 替代。
* 优化：断言方法`assertSchema()`、`assertJSON()`支持`response`传参。
* 优化：`@check_response()` check检查失败打印`response`。
* 修复：`webdriver_manager` 没有设置上限版本，导致`webdriver_manager>=3.6.x` 报错; 如果使用的 `seldom<=2.9`
  请重新安装`webdriver_manager==3.5.2`。

### 2.9.0

* seldom log功能：
    * 开放seldom 的`log`能力，可以配置`颜色（colorlog）`、`格式(format)`、`等级(level)` 等。
    * 重新定义了seldom打印日志的格式。
    * 所有log统一记录到`/reports/seldom_log.log`文件，不再每次生成单独文件。
* 功能：提供了`@check_response()` 装饰器，为接口封装提供强大的支持。
* 功能：集成`genson`库，生成JsonSchema模板 [100](https://github.com/SeldomQA/seldom/issues/100) 。
* 功能：增加`assertInPath()` 断言方法。
* 功能：增加`jmespath()`方法，方便提取测试数据。
* 优化：`jresponse()` 增加对`jmespath` 语法的支持。
* 优化：支持`self.get()/self.post()/self.put()/self.delete()` 返回response对象。

### 2.8.0

* 功能：增加MongoDB 数据库操作 [93](https://github.com/SeldomQA/seldom/issues/93) 。
* 功能：支持单个用例执行 [94](https://github.com/SeldomQA/seldom/issues/94) 。
* 功能：`sendmail()` 增加`delete`参数，发送完邮件删除`reports/`
  目录下面的报告和日志文件 [95](https://github.com/SeldomQA/seldom/issues/95) 。
* 功能：增加`jsonpath` 和 `jresponse()` ，更容易查找json数据 [96](https://github.com/SeldomQA/seldom/issues/96) 。
* 功能：创建项目脚手架增加api测试例子：`seldom -project mypro` 。
* 其他： 全新的seldom在线文档：https://seldomqa.github.io/ ，感谢 @nickliya

### 2.7.0

* 功能：引入`loguru` 库用于打印日志（之前使用python默认logging总有一些重复打印或不打印的问题）。
* 功能：web自动化增加一套方法链（method chaining）的API。
* 功能：支持手动指定浏览器驱动路径。

### 2.6.0

* 移除：自带的`HTMLTestRunner`，HTML报告采用`XTestRunner`。
* 移除：对`unittest-xml-reporting`库的依赖，XML报告使用`XTestRunner`。
* 修改：`SMTP`类发送邮件方法 `sender()` -> `sendmail()`， 发送邮件样式采用`XTestRunner`。
* 增加：`seldom.main()`方法增加`tester` 参数，用于设置测试人员名字，默认`Anonymous`。
* 增加：`seldom.main()`方法增加`language` 参数，用于设置报告中英文`en/zh-CN`，默认`en`。
* 增加：发送钉钉功能。
* 修改：接口测试 `self.session` -> `self.Session()`。
* 移除：接口测试 `self.request()` 方法移除（注：该方法原本不可用）。

### 2.5.1

* 功能：Http接口测试使用日志打印接口信息
* 功能：Http接口测试打印`json`参数 [83](https://github.com/SeldomQA/seldom/issues/83)
* 修复：Web UI测试`self.Key()` 无法定位元素的问题

### 2.5.0

* 功能：支持测试平台化。
* 功能：utils 增加`file`类，获取当前文件目录更方便。
* 修复：`self.select()` 操作下拉选择错误。
* 修复：`diff_json()` 对比json文件错误。

### 2.4.2

* 功能：增强`@file_data`使用方式，json/yaml支持内嵌`dict`数据。

### 2.4.1

* 优化：HTTP接口测试增加`cookies`信息打印。
* 优化：`@file_data()` 使用，支持指定目录。
* 修复：`visit()` 方法默认浏览器没有自动安装浏览器驱动的问题。
* 修复：`query_sql()` 执行SQL没有提交的问题。

### 2.4.0

* 适配selenium 4.0+ ，适配相关依赖库新版本。
* 测试用例支持`label`标签分类。
* 接口测试增加打印入参信息 [79](https://github.com/SeldomQA/seldom/issues/79) 。
* EdgeChromium浏览器支持`headless`模式。
* Web自动化测试增加元素截图`self.element_screenshot()`
* 优化HTML测试报告样式。
* 优化邮件模板样式。

### 2.3.3

* 增加 `assertNotText()` 断言方法 [75](https://github.com/SeldomQA/seldom/issues/75) 。
* 修复`main()`设置`rerun` 和 `save_last_run`参数，导致用例统计错误 [76](https://github.com/SeldomQA/seldom/issues/76) 。

### 2.3.2

* 接口调用如果是图片类型，不在打印内容。
* 增加`screenshot` 针对定位的元素截图, 用法`self.screenshot(id="xx")`。
* 测试报告：优化截图的样式。
* 发邮件功能，默认增加附件为测试报告。

### 2.3.1

* 修复`assertUrl()`、`assertInUrl()` 断言中文编码错误。
* 增加文件路径操作。
    * `file_path()` 获取当前文件路径。
    * `file_dir()` 获取当前文件目录。
    * `file_dir_dir()` 获取当前文件目录的目录。
    * `file_dir_dir_dir()` 获取当前文件目录的目录的目录。
    * `init_env_path()` 添加路径到环境变量。
* 优化`main()` 方法中代码的执行顺序。

### 2.3.0

* 集成 `webdriver-manager`，不需要再单独安装浏览器驱动。
* seldom logo 显示版本号。
* 固定`selenium`版本号，暂没做`4.0.0`适配。

### 2.2.4

* 修复HTTP接口测试，指定`url`参数错误的问题。[71](https://github.com/SeldomQA/seldom/issues/71)
* 支持发送多人邮件。[72](https://github.com/SeldomQA/seldom/issues/72)
* 优化HTMLTestRunner, 重跑次数不记录为用例数。
* 修复pip安装缺少`description.rst` 问题。

### 2.2.3

* 支持控制台操作步骤显示在HTML报告中。[42](https://github.com/SeldomQA/seldom/issues/42)
* 修改`get_elements()`返回空列表。[69](https://github.com/SeldomQA/seldom/issues/69)
* 修复因为`colorama`/`emoji`导致的编码错误。[70](https://github.com/SeldomQA/seldom/issues/70)

### 2.2.2

* 优化db操作方法。
* 打印`logs`合并到 `reports` 目录。

### 2.2.1

* webdriver文件增加类型。
* 删除utils 错误代码。
* 修复：`diff_json()` 函数处理复杂数据报错 #66
* 修复：运行接口测试用例报 driver 错误 #68
* 修复：测试报告`popper.min.js` CDN 太慢的问题

### 2.2.0

* 增加接口测试方法`session`、`request`。
* 增加`seldom -h2c`参数，用于将har文件转成测试用例。

### 2.1.1

* 增加随机生成时间方法`get_past_time()`、`get_future_time()`
* 优化：截图方法`screenshots()`，可以在任意位置使用该方法生成截图，并显示在HTML测试报告中。
* 修复：接口测试`main()`中base_url 和 方法中的 url 同时存在的问题。
* 修复：优化MySQL数据库连接的问题。
* 修复：发送邮件时的错误。
* 修复：当`main()`中的timeout设置为1时，断言失败的问题。

### 2.1.0

* 增加数据库操作，同时支持`sqlite3`、`mysql`。
* 优化`file_data()`，兼容2.0.0用法。

### 2.0.1

* 优化 `file_data()`, 自动查找数据文件。
* 优化脚手架，创建项目例子更新。

### 2.0.0

* webdriver API 修改
    * 移除 `self.get()`
    * 增加 `self.visit()`
    * 移除 `self.open_new_window()`
    * 移除 `self.current_window_handle()`
    * 移除 `self.new_window_handle()`
    * 移除 `self.window_handles()`
    * 修改 `self.switch_to_window()` 用法
    * 优化打印日志，为每种操作加上 emoji
* 增加`expected_failure`用例装饰器，用于标记一条用例失败
* 增加 `file_dir（）`, 返回当前文件所在目录的绝对路径。
* 运行完成自动通过浏览器打开HTML报告
* `main()`方法修改
    * 修复`debug`参数类型错误异常提示
    * 控制台更换字符logo*
* 整合 webdriver/request
* 上线 readthedocs 文档

### 2.0.0.beta

* 支持 HTTP接口测试

### 1.10.3

...

### 1.10.2

* HTMLTestRunner代码优化
* 修复bug

### 1.10.1

* webdriver代码重构
* 修复严重bug

### 1.10.0

* 增加断言元素方法：`assertElement`、`assertNotElement`
* 增加单个测试类、用例执行的方法
* 修复报告样式bug
* 命令行工具优化

### 1.9.0

* 测试报告重构
    * 用例描述单独一列
    * 增加单个用例运行时间
    * 新的报告样式
* 脚手架工具创建项目更新
* 增加随机生成手机号方法

### 1.8.0

* 增加用例依赖装饰器

### 1.7.2

* bug修复版本

### 1.7.0

* 重构浏览器驱动，开放浏览器可配置能力。

### 1.6.0

* 浏览器增加简写
* 支持 logs 日志
* 支持 XML 测试报告
* 增加 file_data 方法实现参数化。
* 修复一些bug

### 1.5.6

* 封装test fixture方法

### 1.5.5

* 修改HTMLTestRunner 错误日志的展示
* 增加mobile web的支持

### 1.5.4

* 增加keys键盘操作
* 元素操作增加聚焦
* debug 模式增加慢操作

### 1.5.3

* 修复bug
* 增加 yaml_to_list()方法

### 1.5.2

* 修复bug

### 1.5.1

* 修复日志重复打印问题
* 修复测试报告不截图问题
* 日志增加emoji表情

### 1.5.0

* 自动化运行过程中，对操作的元素加边框，使其更醒目。
* 去掉对 `setUpClass()`方法的占用，代码做了较大重构。
* 在使用poium时，驱动的获取方式改变，这一点不向下兼容。

### 1.2.6

* 完善自动化发邮件功能
* 增加 type_enter() 方法
* 优化项目的代码的调用
* 修复 seldom + poium 日志问题

### 1.2.5

* 重新定制测试报告样式
* seldom.main()增加timeout参数

### 1.2.4

* 增加数据解析相关操作方法
* 增加跳过测试相关方法
* 增加发邮件功能
* 修复bug, 优化代码

### 1.2.3

* 增加 slow_click() 方法。
* seldom.main() 默认运行当前文件不需要传参。
* seldom.main(report="report-name.html") 允许自定义报告名称。

### 1.2.2

* fix bug
* add function: csv_to_list()/ excel_to_list()

### 1.2.0

Global launch browser

### 1.1.0

selenium grid support
Added safari support

### 1.0.0

The framework function has been basically improved. I'm glad to release version 1.0

### 0.3.6

Add cookie manipulation APIs
Optimized element wait

### 0.3.5

Added chrome/firefox browser driver download command
Driver file path Settings are supported

### 0.3.3

add skip case

### 0.3.2

Added a switch to display the last rerun result
Optimized assertion method

### 0.3.0

Update element positioning

### 0.2.0

Change the project name to seldom
Introducing the poium test library,

### 0.1.5

* Increased test case failure rerun
* Add use case failure screenshots

### 0.1.2

new framework

#### 0.0.9

Simplifying API calls

#### 0.0.8

add parameterized
Beautification test report

#### 0.0.7

Re based on unittest.

#### 0.0.6

add setup.py file, Specification of the installation process, a time to install all dependencies.
Delete unnecessary files

#### 0.0.5

Increase the support of multiple positioning methods

#### 0.0.4

Method to add default to wait.
Modify the realization of the individual methods

#### 0.0.3.1 version update:

* Repair part bug.

#### 0.0.3 version update:

* With the nose instead of unittest.
* Discard HTMLTestRunner,Integrated nose-html-reporting.
* modify the examples under demo.

#### 0.0.2 version update:

* all the elements of the operation selector xpath replaced by css, css syntax because more concise.
* when you run the test case no longer need to specify the directory, the default directory for the current test.
* modify the examples under demo.


