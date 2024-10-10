"""
seldom.main() - Run seldom main method.
Run:
> python run.py
"""
import seldom
from seldom.appium_lab.android import UiAutomator2Options

"""
参数说明：
path： 指定测试目录。
app_info： 启动app配置。
app_server： appium server 地址。
title： 指定测试项目标题。
tester： 指定测试人员。
description： 指定测试环境描述。
debug： debug模式，设置为True不生成测试用例。
rerun： 测试失败重跑。
language： 测试报告语言：en/zh-CN。
"""

if __name__ == '__main__':
    capabilities = {
        'deviceName': 'ELS-AN00',
        'automationName': 'UiAutomator2',
        'platformName': 'Android',
        'appPackage': 'com.microsoft.bing',
        'appActivity': 'com.microsoft.sapphire.app.main.MainSapphireActivity',
        'noReset': True,
    }
    options = UiAutomator2Options().load_capabilities(capabilities)
    seldom.main(path="./test_dir",
                app_info=options,
                app_server="http://127.0.0.1:4723",
                title="Seldom App test demo",
                tester="虫师",
                rerun=2,
                language="zh-CN")
