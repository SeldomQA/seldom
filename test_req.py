import seldom


class TestAPI(seldom.HttpRequest):

    def test_case(self):
        self.get("https://httpbin.org/get")
        self.assertStatusCode(200)  # 状态验证
        # 数据校验
        schema = {
            "type": "object",
            "properties": {
                "headers": {
                    "Host": "httpbin.org",
                    "User-Agent": "python-requests/2.22.0"
                },
                "origin": {"type": "string"},
                "url": {
                    "type": "string",
                    "minLength": 20
                }
            },
        }
        self.assertSchema(schema)


if __name__ == '__main__':
    seldom.run()
