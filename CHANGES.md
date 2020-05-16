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


