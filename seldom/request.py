import requests
from seldom.running.config import Seldom


def request(func):
    def wrapper(*args, **kw):
        func_name = func.__name__
        print('\n----------- Request 🚀 ---------------')
        url = list(args)[1]
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + list(args)[1]
        print('url: {u}         method: {m}'.format(u=url, m=func_name.upper()))

        # running function
        r = func(*args, **kw)

        ResponseResult.status_code = r.status_code
        print("----------- Response 🛬️ -------------")
        try:
            print("type: {}".format("json"))
            print(r.json())
            ResponseResult.response = r.json()
        except BaseException as msg:
            print("warning: {}".format(msg))
            print("type: {}".format("text"))
            print(r.text)
            ResponseResult.response = {}

    return wrapper


class ResponseResult:
    status_code = 200
    response = None


class HttpRequest(object):

    @request
    def get(self, url, params=None, **kwargs):
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + url
        return requests.get(url, params=params, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + url
        return requests.post(url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + url
        return requests.put(url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + url
        return requests.delete(url, **kwargs)

    @property
    def response(self):
        """
        Returns the result of the response
        :return: response
        """
        return ResponseResult.response

    @property
    def session(self):
        """
        A Requests session.
        """
        s = requests.Session()
        return s

    @staticmethod
    def request(method=None, url=None, headers=None, files=None, data=None,
                params=None, auth=None, cookies=None, hooks=None, json=None):
        """
        A user-created :class:`Request <Request>` object.
        """
        req = requests.Request(method, url, headers, files, data,
                               params, auth, cookies, hooks, json)
        return req
