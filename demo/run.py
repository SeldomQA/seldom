import seldom

"""
说明：
path： 指定测试目录。
browser： Web测试，指定浏览器，默认chrome - web专用
base_url： Http测试，指定接口地址。       - api专用
app_info： 启动app配置。                - app专用
app_server： appium server 地址。      - app专用
title： 指定测试项目标题。
tester： 指定测试人员。
description： 指定测试环境描述。
debug： debug模式，设置为True不生成测试用例。
rerun： 测试失败重跑
"""

if __name__ == '__main__':
    # web case 配置
    seldom.main(path="./test_dir/web_case",
                browser="chrome",
                title="seldom Web demo",
                tester="虫师",
                description=["Browser: Chrome"],
                rerun=2)

    # api case 配置
    # seldom.main(path="./test_dir/api_case",
    #             base_url="http://httpbin.org",
    #             title="seldom API demo",
    #             tester="虫师",
    #             rerun=2)

    # app case 配置
    # from seldom.appium_lab.android import UiAutomator2Options
    # capabilities = {
    #     'deviceName': 'ELS-AN00',
    #     'automationName': 'UiAutomator2',
    #     'platformName': 'Android',
    #     'appPackage': 'com.microsoft.bing',
    #     'appActivity': 'com.microsoft.sapphire.app.main.MainSapphireActivity',
    #     'noReset': True,
    # }
    # options = UiAutomator2Options().load_capabilities(capabilities)
    # seldom.main(path="./test_dir/app_case",
    #             app_server="http://127.0.0.1:4723",
    #             app_info=options,
    #             title="seldom App demo",
    #             tester="虫师",
    #             rerun=2)
