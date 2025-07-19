import seldom


class TestSaveResp(seldom.TestCase):

    def test_save_response(self):
        """将response保存到文件中"""
        resp = self.get("/get")
        self.save_response(resp)


class TestReqIP(seldom.TestCase):

    def test_get_ip_address(self):
        """检查当前请求的IP地址"""
        self.get("/get")
        self.ip_address()


if __name__ == '__main__':
    seldom.main(base_url="https://httpbin.org")
