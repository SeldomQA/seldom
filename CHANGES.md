### 2.0.0 

done
* webdriver API 修改
  * 移除 `self.get()`
  * 增加 `self.visit()`
  * 移除 `self.open_new_window()`
  * 移除 `self.current_window_handle()`
  * 移除 `self.new_window_handle()`
  * 移除 `self.window_handles()`
  * 修改 `self.switch_to_window()` 用法
* 增加`expected_failure`，用于标记一条用例失败
* 增加 `file_dir（）`, 返回当前文件所在目录的绝对路径。
* webdriver API 优化打印日志  
* 运行完成自动通过浏览器打开HTML报告

todo
* 上线 readthedocs 文档，整理中...
* 整合 webdriver/request， 未开始


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
* 重构浏览器驱动，开放浏览器可配置能力。[文档](./docs/driver.md)

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


