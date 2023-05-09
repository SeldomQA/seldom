import time
import seldom
from seldom.utils import threads


@threads(3)  # !!!核心!!!! 设置线程数
def run_case(path):
    """
    根据传入的path执行用例
    """
    seldom.main(path=path, debug=True)


if __name__ == "__main__":
    # 定义三个目录，分别丢给3个线程，当然取决于 @threads(s) 的数量。
    paths = [
        "./demo/test_dir/more_case/test_case1.py",
        "./demo/test_dir/more_case/test_case2.py",
        "./demo/test_dir/more_case/test_case3.py"
    ]
    for url in paths:
        run_case(url)
    end = time.time()


