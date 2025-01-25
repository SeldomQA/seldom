import seldom
from seldom.utils import genson


class TestHttpAssert(seldom.TestCase):

    def test_assert_json(self):
        """
        test assertJSON
        """
        payload = {"name": "tom", "hobby": ["basketball", "swim"]}
        self.get("/get", params=payload)
        assert_data = {
            "hobby": ["swim", "basketball"],
            "name": "tom"
        }
        self.assertJSON(assert_data, self.response["args"])

    def test_assert_path(self):
        """
        test assertJSON
        """
        payload = {'name': 'tom', 'hobby': ['basketball', 'swim']}
        self.get("/get", params=payload)
        self.assertPath("args.name", "tom")
        self.assertPath("args.hobby[0]", "basketball")
        self.assertInPath("args.hobby[0]", "ball")

    def test_assert_schema(self):
        """
        test assertJSON
        """
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("/get", params=payload)

        schema = genson(self.response["args"])
        print("json Schema: \n", schema)

        # 断言数据结构和类型
        assert_data = {
            "$schema": "http://json-schema.org/schema#",
            "type": "object",
            "properties": {
                "age": {
                    "type": "string"
                },
                "hobby": {
                    "type": "array", "items": {"type": "string"}
                },
                "name": {
                    "type": "string"
                }
            },
            "required":
                ["age", "hobby", "name"]
        }
        self.assertSchema(assert_data, self.response["args"])


if __name__ == '__main__':
    seldom.main(debug=True, base_url="http://httpbin.org")
