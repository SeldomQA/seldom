"""
seldom.main() - Run seldom main method.
Run:
> python run.py
"""
import seldom

"""
参数说明：
path： 指定测试目录。
base_url： Http测试，指定接口地址。
title： 指定测试项目标题。
tester： 指定测试人员。
description： 指定测试环境描述。
debug： debug模式，设置为True不生成测试用例。
rerun： 测试失败重跑
language： 测试报告语言：en/zh-CN。
"""

if __name__ == '__main__':
    seldom.main(path="./test_dir",
                base_url="http://httpbin.org",
                title="seldom API test demo",
                tester="虫师",
                rerun=2,
                language="zh-CN")
