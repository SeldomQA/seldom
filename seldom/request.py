"""
seldom requests
"""
import ast
import json
from typing import Any
import requests
from seldom.running.config import Seldom
from seldom.running.loader_hook import loader
from seldom.logging import log
from seldom.utils import jsonpath as utils_jsonpath
from seldom.utils import jmespath as utils_jmespath
from seldom.utils.curlify import to_curl


IMG = ["jpg", "jpeg", "gif", "bmp", "webp"]


class ResponseResult:
    status_code = 200
    response = None
    request = None


def formatting(msg):
    """formatted message"""
    if isinstance(msg, dict):
        return json.dumps(msg, indent=2, ensure_ascii=False)
    return msg


def request(func):

    def wrapper(*args, **kwargs):
        func_name = func.__name__
        log.info('-------------- Request -----------------[🚀]')
        try:
            url = list(args)[1]
        except IndexError:
            url = kwargs.get("url", "")
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url

        img_file = False
        file_type = url.split(".")[-1]
        if file_type in IMG:
            img_file = True

        log.info(f"[method]: {func_name.upper()}      [url]: {url} ")
        auth = kwargs.get("auth", None)
        headers = kwargs.get("headers", None)
        cookies = kwargs.get("cookies", None)
        params = kwargs.get("params", None)
        data = kwargs.get("data", None)
        json_ = kwargs.get("json", None)
        files = kwargs.get("files", None)
        if auth is not None:
            log.debug(f"[auth]:\n{auth}")
        if headers is not None:
            log.debug(f"[headers]:\n{formatting(headers)}")
        if cookies is not None:
            log.debug(f"[cookies]:\n{formatting(cookies)}")
        if params is not None:
            log.debug(f"[params]:\n{formatting(params)}")
        if data is not None:
            log.debug(f"[data]:\n{formatting(data)}")
        if json_ is not None:
            log.debug(f"[json]:\n{formatting(json_)}")
        if files is not None:
            log.debug(f"[files]:\n{files}")

        # running function
        r = func(*args, **kwargs)

        ResponseResult.request = r.request
        ResponseResult.status_code = r.status_code
        log.info("-------------- Response ----------------[🛬️]")
        if ResponseResult.status_code == 200 or ResponseResult.status_code == 304:
            log.info(f"successful with status {ResponseResult.status_code}")
        else:
            log.warning(f"unsuccessful with status {ResponseResult.status_code}")
        resp_time = r.elapsed.total_seconds()
        try:
            resp = r.json()
            log.debug(f"[type]: json      [time]: {resp_time}")
            log.debug(f"[response]:\n {formatting(resp)}")
            ResponseResult.response = resp
        except BaseException as msg:
            log.debug("[warning]: failed to convert res to json, try to convert to text")
            log.trace(f"[warning]: {msg}")
            if img_file is True:
                log.debug(f"[type]: {file_type}      [time]: {resp_time}")
                ResponseResult.response = r.content
            else:
                r.encoding = 'utf-8'
                log.debug(f"[type]: text      [time]: {resp_time}")
                log.debug(f"[response]:\n {r.text}")
                ResponseResult.response = r.text

        return r

    return wrapper


def mock_url(url: str) -> str:
    """
    If the mock hook is set, replace it with the mock url
    :param url:
    """
    configs = loader("mock_url") if loader("mock_url") is not None else None
    if configs is None:
        return url

    replace_url = configs.get(url, "")
    if replace_url == "":
        return url

    log.debug(f"mock url: {replace_url}")
    return replace_url


class HttpRequest:
    """seldom http request class"""

    @request
    def get(self, url, params=None, **kwargs):
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url
        url = mock_url(url)
        return requests.get(url, params=params, **kwargs)

    @request
    def post(self, url, data=None, json=None, **kwargs):
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url
        url = mock_url(url)
        return requests.post(url, data=data, json=json, **kwargs)

    @request
    def put(self, url, data=None, **kwargs):
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url
        url = mock_url(url)
        return requests.put(url, data=data, **kwargs)

    @request
    def delete(self, url, **kwargs):
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url
        url = mock_url(url)
        return requests.delete(url, **kwargs)

    @request
    def patch(self, url, data=None, **kwargs):
        if (Seldom.base_url is not None) and (url.startswith("http") is False):
            url = Seldom.base_url + url
        url = mock_url(url)
        return requests.patch(url, data=data, **kwargs)

    @property
    def response(self) -> dict:
        """
        Returns the result of the response
        :return: response
        """
        return ResponseResult.response

    @staticmethod
    def jsonpath(expr, index: int = None, response=None) -> Any:
        """
        Extract the data in response
        mode:
         * jsonpath: https://goessner.net/articles/JsonPath/
         * jmespath: https://jmespath.org/
        """
        if response is None:
            response = ResponseResult.response

        ret = utils_jsonpath(response, expr)
        if index is not None:
            ret = ret[index]
        return ret

    @staticmethod
    def jmespath(expr, response=None) -> Any:
        """
        Extract the data in response
        * jmespath: https://jmespath.org/
        """
        if response is None:
            response = ResponseResult.response

        ret = utils_jmespath(response, expr)
        return ret

    @property
    def status_code(self) -> int:
        """
        Returns the result of the status code
        :return: status_code
        """
        return ResponseResult.status_code

    @staticmethod
    def curl(request=None, compressed: bool = False, verify: bool = True) -> str:
        """
        requests to cURL command
        :param request: request object
        :param compressed:
        :param verify:
        :return:
        """
        if request is None:
            return to_curl(ResponseResult.request, compressed, verify)

        return to_curl(request, compressed, verify)

    class Session(requests.Session):

        @request
        def get(self, url, **kwargs):
            r"""Sends a GET request. Returns :class:`Response` object.
            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and (url.startswith("http") is False):
                url = Seldom.base_url + url
            url = mock_url(url)
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
            if (Seldom.base_url is not None) and (url.startswith("http") is False):
                url = Seldom.base_url + url
            url = mock_url(url)
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
            if (Seldom.base_url is not None) and (url.startswith("http") is False):
                url = Seldom.base_url + url
            url = mock_url(url)
            return self.request('PUT', url, data=data, **kwargs)

        @request
        def delete(self, url, **kwargs):
            r"""Sends a DELETE request. Returns :class:`Response` object.

            :param url: URL for the new :class:`Request` object.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :rtype: requests.Response
            """
            if (Seldom.base_url is not None) and (url.startswith("http") is False):
                url = Seldom.base_url + url
            url = mock_url(url)
            return self.request('DELETE', url, **kwargs)

    @staticmethod
    def json_to_dict(data: str, replace_quotes: bool = True) -> dict:
        """
        json to dict
        :param data: json data.
        :param replace_quotes: whether to replace single quotes.
        """
        if isinstance(data, dict):
            return data
        elif isinstance(data, str):
            try:
                data_dict = ast.literal_eval(data)
            except ValueError:
                try:
                    if replace_quotes:
                        data = data.replace('\'', '\"')
                    data_dict = json.loads(data)
                except json.decoder.JSONDecodeError:
                    log.error(f"json to dict error. --> {data}")
                    return {}
                else:
                    return data_dict
            else:
                return data_dict
        else:
            log.error(f"type error --> {data}")
            return {}


def check_response(describe: str = "", status_code: int = 200, ret: str = None, check: dict = None, debug: bool = False):
    """
    checkout response data
    :param describe: interface describe
    :param status_code: http status code
    :param ret: return data
    :param check: check data
    :param debug: debug Ture/False
    :return:
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if debug is True:
                log.debug(f"Execute {func_name} - args: {args}")
                log.debug(f"Execute {func_name} - kwargs: {kwargs}")

            r = func(*args, **kwargs)
            flat = True
            if r.status_code != status_code:
                log.error(f"Execute {func_name} - {describe} failed: {r.status_code}")
                flat = False

            try:
                r.json()
            except json.decoder.JSONDecodeError:
                log.error(f"Execute {func_name} - {describe} failed：Not in JSON format")
                flat = False

            if debug is True:
                log.debug(f"Execute {func_name} - response:\n {r.json()}")

            if flat is True:
                log.info(f"Execute {func_name} - {describe} success!")

            if check is not None:
                for expr, value in check.items():
                    data = utils_jmespath(r.json(), expr)
                    if data != value:
                        log.error(f"Execute {func_name} - check data failed：{expr} = {value}")
                        log.error(f"Execute {func_name} - response：{r.json()}")
                        raise ValueError(f"{data} != {value}")

            if ret is not None:
                data = utils_jmespath(r.json(), ret)
                if data is None:
                    log.error(f"Execute {func_name} - return {ret} is None")
                return data

            return r.json()

        return wrapper

    return decorator
