import seldom
from seldom.extend_lib import threads


@threads(3)  # !!!核心!!!! 设置线程数
def run_case(path: str):
    """
    根据传入的path执行用例
    """
    seldom.main(path=path, debug=True)


if __name__ == "__main__":
    # 定义3个测试文件，分别丢给3个线程执行。
    paths = [
        "./test_dir/more_case/test_case1.py",
        "./test_dir/more_case/test_case2.py",
        "./test_dir/more_case/test_case3.py"
    ]
    for p in paths:
        run_case(p)
