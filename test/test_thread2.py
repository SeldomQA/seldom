"""
author: bugmaster
data: 2022/9/7
desc: 多线程执行seldom命令
"""
import subprocess
import threading


def running1():
    subprocess.check_call([
        "seldom",  # seldom命令
        "--path", "./test_dir",  # 运行测试用目录
        "--browser", "chrome",  # 浏览器
        "--report", "result1.html"  # 测试报告(可以定义xml报告，容易合并)
    ], cwd="D:/github/seldom/demo"  # 进入执行用例的目录
    )


def running2():
    subprocess.check_call([
        "seldom",
        "--path", "./test_dir",
        "--browser", "firefox",
        "--report", "result2.html"
    ], cwd="D:/github/seldom/demo"
    )


def run():
    threads = []
    t1 = threading.Thread(target=running1, args=())
    threads.append(t1)
    t2 = threading.Thread(target=running2, args=())
    threads.append(t2)

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    run()
