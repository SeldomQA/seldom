import seldom


class TestCase(seldom.TestCase):

    @staticmethod
    def start_class(cls):
        print("测试类开始执行")

    @staticmethod
    def end_class(cls):
        print("测试类结束执行")

    def start(self):
        print("一条测试用例开始")

    def end(self):
        print("一条测试结果")

    def test_case_one(self):
        ...

    def test_case_two(self):
        ...


if __name__ == '__main__':
    seldom.main(debug=True)
