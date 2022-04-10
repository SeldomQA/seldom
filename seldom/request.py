import requests
from seldom.running.config import Seldom
from seldom.logging import log
from seldom.utils import jsonpath

IMG = ["jpg", "jpeg", "gif", "bmp", "webp"]


def request(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print("\n")
        log.info('-------------- Request -----------------[🚀]')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")
        if (Seldom.base_url is not None) and ("http" not in url):
            url = Seldom.base_url + list(args)[1]

        img_file = False
        file_type = url.split(".")[-1]
        if file_type in IMG:
            img_file = True

        log.debug("[method]: {m}      [url]: {u} \n".format(m=func_name.upper(), u=url))
        auth = kwargs.get("auth", "")
        headers = kwargs.get("headers", "")
        cookies = kwargs.get("cookies", "")
        params = kwargs.get("params", "")
        data = kwargs.get("data", "")
        json = kwargs.get("json", "")
        if auth != "":
            log.debug(f"[auth]:\n {auth} \n")
        if headers != "":
            log.debug(f"[headers]:\n {headers} \n")
        if cookies != "":
            log.debug(f"[cookies]:\n {cookies} \n")
        if params != "":
            log.debug(f"[params]:\n {params} \n")
        if data != "":
            log.debug(f"[data]:\n {data} \n")
        if json != "":
            log.debug(f"[json]:\n {json} \n")

        # running function
        r = func(*args, **kwargs)

        ResponseResult.status_code = r.status_code
        log.info("-------------- Response ----------------[🛬️]")
        resp_time = r.elapsed.total_seconds()
        try:
            resp = r.json()
            log.debug(f"[type]: json      [time]: {resp_time} \n")
            log.debug(f"[response]:\n {resp} \n")
            ResponseResult.response = resp
        except BaseException as msg:
            log.debug(f"[warning]: {msg} \n")
            if img_file is True:
                log.debug(f"[type]: {file_type}      [time]: {resp_time}")
                ResponseResult.response = r.content
            else:
                log.debug(f"[type]: text      [time]: {resp_time}\n")
                log.debug(f"[response]:\n {r.text} \n")
                ResponseResult.response = r.text

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

    def jresponse(self, expr):
        """
        jsonpath
        doc:
        https://goessner.net/articles/JsonPath/
        """
        ret = jsonpath(ResponseResult.response, expr)
        log.debug(f"[jresponse]:\n {str(ret)}")
        return ret

    class Session(requests.Session):

        @request
        def get(self, url, **kwargs):
            r"""Sends a GET request. Returns :class:`Response` object.

            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and ("http" not in url):
                url = Seldom.base_url + url
            kwargs.setdefault('allow_redirects', True)
            return self.request('GET', url, **kwargs)

        @request
        def post(self, url, data=None, json=None, **kwargs):
            r"""Sends a POST request. Returns :class:`Response` object.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and ("http" not in url):
                url = Seldom.base_url + url
            return self.request('POST', url, data=data, json=json, **kwargs)

        @request
        def put(self, url, data=None, **kwargs):
            r"""Sends a PUT request. Returns :class:`Response` object.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and ("http" not in url):
                url = Seldom.base_url + url
            return self.request('PUT', url, data=data, **kwargs)

        @request
        def delete(self, url, **kwargs):
            r"""Sends a DELETE request. Returns :class:`Response` object.

            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and ("http" not in url):
                url = Seldom.base_url + url
            return self.request('DELETE', url, **kwargs)
