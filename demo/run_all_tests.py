from pyse import TestRunner


runner = TestRunner('./baidu_case','百度自动化测试报告','测试环境：Chrome')
runner.run()


'''
说明：
'./baidu_case' ： 指定测试目录。
'百度测试用例' ： 测试项目标题。
'测试环境：Chrome' ： 测试环境描述。
'''