import seldom
from seldom import data


class TestRequest(seldom.TestCase):
    """
    http api test demo
    doc: https://requests.readthedocs.io/en/master/
    """

    def test_put_method(self):
        """
        test put request
        """
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        """
        test post request
        """
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        """
        test get request
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        """
        test delete request
        """
        self.delete('/delete')
        self.assertStatusCode(200)


class TestAssert(seldom.TestCase):
    """
    Test Assert
    """

    def test_data_assert(self):
        """
        The JSON data returned by the assertion
        :return:
        """
        self.get("/get")
        self.assertStatusCode(200)
        assert_data = {"headers": {"Host": "httpbin.org", "User-Agent": "python-requests/2.26.0"}}
        self.assertJSON(assert_data, exclude=["headers", "user-agent"])  # exclude 过滤掉 json中的部分字段。

    def test_format_assert(self):
        """
        Assert json-schema
        help doc: https://json-schema.org/
        """
        self.get("/get")
        self.assertStatusCode(200)
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

    def test_path_assert(self):
        """
        assert jmesPath
        help doc: https://jmespath.org/
        """
        payload = {"foot": "bread"}
        self.get('/get', params=payload)
        self.assertPath("args.foot", "bread")


class TestRespData(seldom.TestCase):
    """
    Test response data
    """

    def test_resp_data(self):
        """
        Get the returned data
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.post("/post", data=payload)
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"]["key1"], "value1")
        self.assertEqual(self.response["form"]["key2"], "value2")

    def test_data_dependency(self):
        """
        Test for interface data dependencies
        """
        headers = {"X-Account-Fullname": "bugmaster"}
        self.get("/get", headers=headers)
        self.assertStatusCode(200)

        username = self.response["headers"]["X-Account-Fullname"]
        self.post("/post", data={'username': username})
        self.assertStatusCode(200)


class TestDDT(seldom.TestCase):
    """
    Test Data Driver
    """

    @data([
        ("key1", 'value1'),
        ("key2", 'value2'),
        ("key3", 'value3')
    ])
    def test_data(self, key, value):
        """
        Data-Driver Tests
        """
        payload = {key: value}
        self.post("/post", data=payload)
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"][key], value)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org", debug=True)
