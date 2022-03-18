import seldom

if __name__ == '__main__':
    seldom.main(path="./test_dir/",
                base_url="http://httpbin.org",  # test_http_demo.py
                browser="chrome",
                title="seldom自带demo",
                tester="虫师",
                description=["Browser: Chrome", "API: http://httpbin.org"],
                rerun=0)

'''
说明：
path ： 指定测试目录。
browser ： Web测试，指定浏览器，默认chrome。
base_url ： Http测试，指定接口地址。
title ： 指定测试项目标题。
tester ： 指定测试人员。
description ： 指定测试环境描述。
debug ： debug模式，设置为True不生成测试用例。
rerun ： 测试失败重跑
'''

