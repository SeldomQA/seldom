import seldom
from common import Common


class TestRequest(seldom.TestCase):

    def start(self):
        self.c = Common()
        self.url = "http://httpbin.org/post"

    # def test_case(self):
    #     user = self.c.get_login_user()
    #     print(user)
    #     self.post("http://httpbin.org/post", data={'username': user})
    #     self.assertStatusCode(200)

    def test_case2(self):
        headers = {"User-Agent": "python-requests/2.25.0", "Accept-Encoding": "gzip, deflate", "Accept": "application/json", "Connection": "keep-alive", "Host": "httpbin.org", "Content-Length": "36", "Origin": "http://httpbin.org", "Content-Type": "application/json", "Cookie": "lang=zh"}
        cookies = {"lang": "zh"}
        self.post(self.url, json={"key1": "value1", "key2": "value2"}, headers=headers, cookies=cookies)


if __name__ == '__main__':
    seldom.main(debug=True)



import seldom


class TestCaseTestCase(seldom.TestCase):

    def test_add_event_all_null(self):
        data = {"eid": "", "limit": "", "address": "", "start_time": ""}
        self.post("/add_event/", params=data)
        self.assertPath("body.status", 10021)
        self.assertPath("body.message", "parameter error")


if __name__ == "__main__":
    seldom.main(base_url="http://127.0.0.1:8000/api")



