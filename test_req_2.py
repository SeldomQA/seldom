import seldom


class TestAPI(seldom.TestCase):

    def test_responses(self):
        """
        提取 response 数据
        """
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("http://httpbin.org/get", params=payload)
        jsonpath1 = self.responses("$..name", mode="jsonpath")
        jsonpath2 = self.responses("$..hobby", mode="jsonpath")
        jsonpath3 = self.responses("$..hobby[0]", mode="jsonpath")
        jsonpath4 = self.responses("$..hobby[0]", mode="jsonpath", index=0)
        print(f"jsonpath1 --> {jsonpath1}")
        print(f"jsonpath2 --> {jsonpath2}")
        print(f"jsonpath3 --> {jsonpath3}")
        print(f"jsonpath4 --> {jsonpath4}")

        jmespath1 = self.responses("args.name", mode="jmespath")
        jmespath2 = self.responses("args.hobby", mode="jmespath")
        jmespath3 = self.responses("args.hobby[0]", mode="jmespath")

        print(f"\njmespath1 --> {jmespath1}")
        print(f"jmespath2 --> {jmespath2}")
        print(f"jmespath3 --> {jmespath3}")

# import seldom
#
#
# class TestAPI(seldom.TestCase):
#
#     def test_assert_schema(self):
#         """
#         assertSchema used.
#         """
#         payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
#         self.get("/get", params=payload)
#         schema = {
#             "type": "object",
#             "properties": {
#                 "age": {"type": "string"},
#                 "name": {"type": "string"},
#                 "hobby": {
#                     "type": "array",
#                     "items": {
#                         "type": "string"
#                     },
#                 }
#             }
#         }
#         self.assertSchema(schema, self.responses("args"))


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org", debug=True)

# from jsonschema import validate
#
#
# r = [{'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-627a847e-63df6add1617a3e809dadf72'}]
#
# s = {'type': 'object', 'properties': {'Host': {'type': 'string'}, 'name': {'type': 'string'}, 'hobby': {'type': 'array', 'items': {'type': 'string'}}}}
#
#
#
# validate(instance=r, schema=s)
#


