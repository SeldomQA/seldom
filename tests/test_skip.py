import seldom


@seldom.skip(reason="跳过类")
class SkipTest(seldom.TestCase):

    def test_case(self):
        ...


class YouTest(seldom.TestCase):

    @seldom.skip(reason="跳过用例")
    def test_skip_case(self):
        ...

    def test_if_skip(self):
        login = False
        if login is False:
            self.skipTest(reason="登录失败，跳过后续执行")


if __name__ == '__main__':
    seldom.main(debug=True)
