import seldom
from seldom.request import api
from seldom.request import HttpRequest


class LoginApiObject(HttpRequest):
    """
    Login API objects
    """

    @api(
        describe="获取登录用户名",
        status_code=200,
        ret="headers.Account",
        check={"headers.Host": "httpbin.org"},
        debug=True
    )
    def get_login_user(self):
        """
        调用接口获得用户名
        """
        headers = {"Account": "bugmaster"}
        r = self.get(f"{self.base_url}/get", headers=headers)
        return r


class LoginTest(seldom.TestCase):

    def test_user_login(self):
        """test user login case"""
        lao = LoginApiObject()
        username = lao.get_login_user()
        self.assertEqual(username, "bugmaster")


if __name__ == '__main__':
    seldom.main(base_url="https://httpbin.org", debug=True)
