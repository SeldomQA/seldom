import unittest
from seldom.extend_lib.jsonpath2 import jsonpath

json_data = {
    "args": {
        "id": "1",
        "name": "tom",
        "hobby": ["code", "sleep", "eat"],
        "child": [
            {
                "id": "2",
                "name": "jack",
                "hobby": ["play"],
            },
            {
                "id": "3",
                "name": "blue",
                "hobby": ["sleep"],
            }
        ]
    },
    "name": "user-list"
}


class JSONPathTest(unittest.TestCase):

    def test_case(self):
        ret = jsonpath(json_data, "name")
        self.assertEqual(ret, ['user-list'])

    def test_case1(self):
        ret = jsonpath(json_data, "args.id")
        self.assertEqual(ret, ['1'])

    def test_case2(self):
        ret = jsonpath(json_data, "args.hobby[0]")
        self.assertEqual(ret, ['code'])

    def test_case3(self):
        ret = jsonpath(json_data, "args.child[1].id")
        self.assertEqual(ret, ['3'])
        # self.assertEqual(ret, "1")

    def test_case4(self):
        ret = jsonpath(json_data, "args.child[1].hobby[0]")
        self.assertEqual(ret, ['sleep'])


if __name__ == '__main__':
    unittest.main()
