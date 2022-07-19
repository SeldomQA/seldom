# import seldom
#
#
# class YouTest(seldom.TestCase):
#
#     def test_case(self):
#         """a simple test case """
#         self.open("https://www.baidu.com")
#         self.type(id_="kw", text="seldom")
#         self.click(css="#su_error")
#         #...
#
#
# if __name__ == "__main__":
#     seldom.main(rerun=3, save_last_run=False)
#

import seldom
from seldom.utils import genson


class TestAPI(seldom.TestCase):

    def test_extract_responses(self):
        """
        提取 response 数据
        """
        payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
        self.get("http://httpbin.org/get", params=payload)

        # response
        response1 = self.response["args"]["name"]
        response2 = self.response["args"]["hobby"]
        response3 = self.response["args"]["hobby"][0]
        print(f"response1 --> {response1}")
        print(f"response2 --> {response2}")
        print(f"response3 --> {response3}")

        # jmespath
        jmespath1 = self.jmespath("args.name")
        jmespath2 = self.jmespath("args.hobby")
        jmespath3 = self.jmespath("args.hobby[0]")
        jmespath4 = self.jmespath("hobby[0]", response=self.response["args"])
        print(f"\njmespath1 --> {jmespath1}")
        print(f"jmespath2 --> {jmespath2}")
        print(f"jmespath3 --> {jmespath3}")
        print(f"jmespath4 --> {jmespath4}")

        # jsonpath
        jsonpath1 = self.jsonpath("$..name")
        jsonpath2 = self.jsonpath("$..hobby")
        jsonpath3 = self.jsonpath("$..hobby[0]")
        jsonpath4 = self.jsonpath("$..hobby[0]", index=0)
        jsonpath5 = self.jsonpath("$..hobby[0]", index=0, response=self.response["args"])
        print(f"\njsonpath1 --> {jsonpath1}")
        print(f"jsonpath2 --> {jsonpath2}")
        print(f"jsonpath3 --> {jsonpath3}")
        print(f"jsonpath4 --> {jsonpath4}")
        print(f"jsonpath5 --> {jsonpath5}")


if __name__ == '__main__':
    seldom.main(debug=False)

    # def test_assert_json(self):
    #     # 接口参数
    #     payload = {"name": "tom", "hobby": ["basketball", "swim"]}
    #     # 接口调用
    #     self.get("http://httpbin.org/get", params=payload)
    #
    #     # 断言数据
    #     assert_data = {
    #         "hobby": ["swim", "basketball"],
    #         "name": "tom"
    #     }
    #     self.assertJSON(assert_data, self.response["args"])
    #
    # def test_assert_schema(self):
    #     # 接口参数
    #     payload = {"hobby": ["basketball", "swim"], "name": "tom", "age": "18"}
    #     # 调用接口
    #     self.get("/get", params=payload)
    #
    #     # 生成数据结构和类型
    #     schema = genson(self.response["args"])
    #     print("json Schema: \n", schema)
    #
    #     # 断言数据结构和类型
    #     assert_data = {
    #         "$schema": "http://json-schema.org/schema#",
    #         "type": "object",
    #         "properties": {
    #             "age": {
    #                 "type": "string"
    #             },
    #             "hobby": {
    #                 "type": "array", "items": {"type": "string"}
    #             },
    #             "name": {
    #                 "type": "string"
    #             }
    #         },
    #         "required":
    #             ["age", "hobby", "name"]
    #     }
    #     self.assertSchema(assert_data, self.response["args"])
    #


# class TestRequest(seldom.TestCase):
#     """
#     http api test demo
#     doc: https://requests.readthedocs.io/en/master/
#     """
#
#     def test_put_method(self):
#         """
#         test put request
#         """
#         self.put("/put", data={"key": "value"})
#         self.assertStatusCode(200)

#     def test_post_method(self):
#         """
#         test post request
#         """
#         self.post("/post", data={"key":"value"})
#         self.assertStatusCode(200)
#
#     def test_get_method(self):
#         """
#         test get request
#         """
#         payload = {"key1": "value1", "key2": "value2"}
#         self.get("/get", params=payload)
#         self.assertStatusCode(200)
#
#     def test_delete_method(self):
#         """
#         test delete request
#         """
#         self.delete("/delete")
#         self.assertStatusCode(300)
#
#
# class TestAssert(seldom.TestCase):
#
#     def test_data_assert(self):
#         """
#         The JSON data returned by the assertion
#         :return:
#         """
#         self.get("/get")
#         self.assertStatusCode(200)
#         assert_data = {"headers1": {"Host": "httpbin.org", "User-Agent": "python-requests/2.25.0"}}
#         self.assertJSON(assert_data)
#
#     def test_format_assert(self):
#         """
#         Assert json-schema
#         help doc: https://json-schema.org/
#         """
#         self.get("/get")
#         self.assertStatusCode(200)
#         # 数据校验
#         schema = {
#             "type": "object",
#             "properties": {
#                 "headers": {
#                     "Host": "httpbin.org",
#                     "User-Agent": "python-requests/2.22.0"
#                 },
#                 "origin": {"type": "string"},
#                 "url": {
#                     "type": "string",
#                     "minLength": 20
#                 }
#             },
#         }
#         self.assertSchema(schema)
#
# def test_path_assert(self):
#     """
#     assert jmesPath
#     help doc: https://jmespath.org/
#     """
#     payload = {"foot": "bread"}
#     self.get("/get", params=payload)
#     self.assertPath("args.foot.11", "bread")


# class TestRespData(seldom.TestCase):
#
#     def test_resp_data(self):
#         """
#         Get the returned data
#         """
#         payload = {"key1": "value1", "key2": "value2"}
#         self.post("/post", data=payload)
#         self.assertStatusCode(200)
#         self.assertEqual(self.response["form"]["key1"], "value1")
#         self.assertEqual(self.response["form"]["key2"], "value2")
#
#     def test_data_dependency(self):
#         """
#         Test for interface data dependencies
#         """
#         headers = {"X-Account-Fullname": "bugmaster"}
#         self.get("/get", headers=headers)
#         self.assertStatusCode(200)
#
#         username = self.response["headers"]["X-Account-Fullname"]
#         self.post("/post", data={"username": username})
#         self.assertStatusCode(200)
#
#
# class TestDDT(seldom.TestCase):
#
#     @data([
#         ("key1", "value1"),
#         ("key2", "value2"),
#         ("key3", "value3")
#     ])
#     def test_data(self, key, value):
#         """
#         Data-Driver Tests
#         """
#         payload = {key: value}
#         self.post("/post", data=payload)
#         self.assertStatusCode(200)
#         self.assertEqual(self.response["form"][key], value)
#


# if __name__ == "__main__":
#     # log.colorLog = False
#     print("what?")
#     seldom.main(base_url="http://httpbin.org", debug=True)
