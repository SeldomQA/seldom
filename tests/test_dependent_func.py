import seldom
from seldom.testdata import get_md5
from seldom.utils import cache, dependent_func


class DependentTest(seldom.TestCase):

    @staticmethod
    def user_login(username, password):
        """
        模拟用户登录，获取登录token
        """
        return get_md5(username + password)

    @dependent_func(user_login, username="tom", password="t123")
    def test_case(self):
        """
        sample test case
        """
        token = cache.get("user_login")
        print("token", token)


if __name__ == '__main__':
    seldom.main()
    cache.clear()
