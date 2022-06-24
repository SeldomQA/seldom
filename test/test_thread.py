"""
author: bugmaster
data: 2022/6/18
desc: 线程用法
"""
import time
import seldom
from seldom import data
from seldom.utils.thread_lab import ThreadWait


@ThreadWait
def slow_event(case_name, s):
    """
    Take care of things that are slow！
    :param case_name: case name
    :param s: Some of the parameters
    :return:
    """
    print(f"{case_name} running sleep {s}s")
    time.sleep(s)
    return s + 1


class MyTest(seldom.TestCase):

    @classmethod
    def start_class(cls):
        # 存放用例和结果
        cls.assertDict = {}

    def test_case_success(self):
        self.sleep(1)
        # 调用slow_event
        slow_event("test_case_success", 2)
        self.assertDict['test_case_success'] = 3

    def test_case_fail(self):
        self.sleep(1)
        # 调用slow_event
        slow_event("test_case_fail", 3)
        self.assertDict['test_case_fail'] = 3

    @data([
        ("case", "0_case", 4, 5),
        ("case", "1_case", 5, 6),
        ("case", "2_case", 6, 7),
    ])
    def test_ddt(self, _, name, sec, ret):
        self.sleep(1)
        # 调用slow_event
        slow_event(f"test_case3_{name}", sec)
        self.assertDict[f"test_case3_{name}"] = ret

    def test_zz_result(self):
        """
        ** 必须最后一个执行
        ** 等待前面的所有用例运行完成，搜集结果并断言
        """
        all_result = ThreadWait.get_all_result()
        for case, value in all_result.items():
            self.assertEqual(self.assertDict[case], value)


if __name__ == '__main__':
    seldom.main(debug=False)

