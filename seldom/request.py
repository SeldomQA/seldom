import json
import unittest
import requests
from jsonschema import validate


def logger(func):
    def wrapper(*args, **kw):
        print('Start sending the request: 👉 {} '.format(func.__name__))

        # running function
        r = func(*args, **kw)

        ResponseResult.status_code = r.status_code
        print("🛬️ Result: --------------------------")
        try:
            print("(json)", r.json())
            ResponseResult.response = json.loads(r.json())
        except BaseException as msg:
            print(msg)
            print("(text)", r.text)
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
        return requests.get(url, params=params, **kwargs)

    @logger
    def post(self, url, data=None, json=None, **kwargs):
        return requests.post(url, data=data, json=json, **kwargs)

    @logger
    def put(self, url, data=None, **kwargs):
        return requests.put(url, data=data, **kwargs)

    @logger
    def delete(self, url, **kwargs):
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
        validate(instance=ResponseResult.response, schema=schema)


if __name__ == '__main__':
    req = HttpRequest("https://httpbin.org/get")
    req.get().params().auth()
