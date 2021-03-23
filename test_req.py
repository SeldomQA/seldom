import seldom


class TestRequest(seldom.HttpRequest):

    def test_put_method(self):
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete('/delete')
        self.assertStatusCode(200)


class TestAssert(seldom.HttpRequest):

    def test_data_assert(self):
        self.get("/get")
        self.assertStatusCode(200)  # 状态验证
        assert_data = {"headers": {"Host": "httpbin.org", "User-Agent": "python-requests/2.25.0"}}
        self.assertJSON(assert_json=assert_data)

    def test_format_assert(self):
        self.get("/get")
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
    seldom.run(base_url="http://httpbin.org", debug=True)
