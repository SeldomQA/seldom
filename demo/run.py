import seldom

"""
说明：
path： 指定测试目录。
browser： Web测试，指定浏览器，默认chrome。
base_url： Http测试，指定接口地址。
app_info： 启动app配置,
app_server： appium server 地址。
title： 指定测试项目标题。
tester： 指定测试人员。
description： 指定测试环境描述。
debug： debug模式，设置为True不生成测试用例。
rerun： 测试失败重跑
"""

if __name__ == '__main__':
    # web case 配置
    # seldom.main(path="./test_dir/web_case",
    #             browser="chrome",
    #             title="seldom自带 Web demo",
    #             tester="虫师",
    #             description=["Browser: Chrome"],
    #             rerun=0)

    # api case 配置
    # seldom.main(path="./test_dir/api_case",
    #             base_url="http://httpbin.org",
    #             title="seldom自带 API demo",
    #             tester="虫师",
    #             rerun=0)

    # app case 配置
    # desired_caps = {
    #     'deviceName': 'JEF_AN20',
    #     'automationName': 'UiAutomator2',
    #     'platformName': 'Android',
    #     'platformVersion': '10.0',
    #     'appPackage': 'com.meizu.flyme.flymebbs',
    #     'appActivity': '.ui.LoadingActivity',
    #     'noReset': True,
    # }
    # seldom.main(path="./test_dir/app_case",
    #             app_info=desired_caps,
    #             app_server="http://127.0.0.1:4723",
    #             title="seldom自带 API demo",
    #             tester="虫师",
    #             rerun=0)

    # uiautomator2 case 配置
    desired_caps = {
        'deviceName': 'JEF_AN20',
        'platformName': 'Android',
        'appPackage': 'com.meizu.flyme.flymebbs',
    }
    seldom.main(path="./test_dir/app_case",
                app_info=desired_caps,
                title="seldom自带 APP demo",
                tester="Cobb",
                debug=True,
                rerun=0)
