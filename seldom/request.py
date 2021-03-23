import json
import unittest
import requests
from jsonschema import validate
from jsonschema.exceptions import SchemaError
from seldom.utils import diff_json, AssertInfo
from seldom.running.config import Seldom


def logger(func):
    def wrapper(*args, **kw):
        func_name = func.__name__
        print('\n👉 Request:-------------------------')
        print('method: {}'.format(func_name.upper()))
        print('path: {}'.format(list(args)[1]))

        # running function
        r = func(*args, **kw)

        ResponseResult.status_code = r.status_code
        print("🛬️ Response:------------------------")
        try:
            print("type: {}".format("json"))
            print(r.json())
            ResponseResult.response = r.json()
        except BaseException as msg:
            print("warning: {}".format(msg))
            print("type: {}".format("json"))
            print(r.text)
            ResponseResult.response = {}

    return wrapper


class ResponseResult:
    status_code = None
    response = None


class HttpRequest(unittest.TestCase):

    def setUp(self) -> None:
        ResponseResult.status_code = 200

    @logger
    def get(self, url, params=None, **kwargs):
        if Seldom.base_url is not None:
            url = Seldom.base_url + url
        return requests.get(url, params=params, **kwargs)

    @logger
    def post(self, url, data=None, json=None, **kwargs):
        if Seldom.base_url is not None:
            url = Seldom.base_url + url
        return requests.post(url, data=data, json=json, **kwargs)

    @logger
    def put(self, url, data=None, **kwargs):
        if Seldom.base_url is not None:
            url = Seldom.base_url + url
        return requests.put(url, data=data, **kwargs)

    @logger
    def delete(self, url, **kwargs):
        if Seldom.base_url is not None:
            url = Seldom.base_url + url
        return requests.delete(url, **kwargs)

    @property
    def resp(self):
        """
        Returns the result of the response
        :return:
        """
        return ResponseResult.response

    def assertStatusCode(self, status_code, msg=None):
        self.assertEqual(ResponseResult.status_code, status_code, msg=msg)

    def assertSchema(self, schema):
        try:
            validate(instance=ResponseResult.response, schema=schema)
        except SchemaError as msg:
            self.assertEqual("Response data", "Schema data", msg=msg)
        else:
            self.assertEqual(1, 1)

    def assertJSON(self, assert_json):
        AssertInfo.data = []
        diff_json(ResponseResult.response, assert_json)
        if len(AssertInfo.data) == 0:
            self.assertEqual(1, 1)
        else:
            self.assertEqual("Response data", "Assert data", msg=AssertInfo.data)


if __name__ == '__main__':
    req = HttpRequest("https://httpbin.org/get")
    req.get().params().auth()
