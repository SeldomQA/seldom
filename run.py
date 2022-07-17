import json
from seldom import SeldomTestLoader
from seldom.running.next_runner import TestMainExtend

if __name__ == '__main__':
    SeldomTestLoader.collectCaseInfo = True
    main_extend = TestMainExtend(path="./test_dir/")
    print(main_extend.collect_cases(json=True))

    case = [
        {
            "file": "module_web.test_first_demo",
            "class": {
                "name": "BaiduTest",
                "doc": "Baidu search test case"
            },
            "method": {
                "name": "test_case",
                "doc": "a simple test case "
            }
        }
    ]
    main_extend = TestMainExtend(path="./test_dir")
    main_extend.run_cases(case)

    # seldom.main(path="./test_dir",
    #             base_url="http://httpbin.org",  # test_http_demo.py
    #             browser="chrome",
    #             title="百度测试用例",
    #             description="测试环境：Chrome",
    #             rerun=0)

'''
说明：
path ： 指定测试目录。
browser: 指定浏览，默认chrome。
title ： 指定测试项目标题。
description ： 指定测试环境描述。
debug ： debug模式，设置为True不生成测试用例。
rerun ： 测试失败重跑
'''
