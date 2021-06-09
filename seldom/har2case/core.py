import json
import os
from seldom.logging import log
from seldom.har2case import utils


class HarParser(object):

    def __init__(self, har_file_path):
        self.har_file_path = har_file_path
        self.case_template = """
import seldom


class TestRequest(seldom.TestCase):

    def start(self):
        self.url = "{url}"

    def test_case(self):
        headers = {header}
        cookies = {cookie}
        self.{method}(self.url, {params}, headers=headers, cookies=cookies)
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main()
"""

    def list_to_dict_str(self, data: list) -> str:
        """
        list -> dict -> string
        """
        data_dict = {}
        for param in data:
            data_dict[param["name"]] = param["value"]

        if len(data_dict) == 0:
            data_dict_str = "{}"
        else:
            data_dict_str = json.dumps(data_dict)
        return data_dict_str

    def _make_testcase(self):
        """
        make test case.
        test case are parsed from HAR log entries list.
        """
        testcase = ""
        log_entries = utils.load_har_log_entries(self.har_file_path)

        for entry_json in log_entries:
            url = entry_json["request"].get("url")
            method = entry_json["request"].get("method").lower()
            headers = entry_json["request"].get("headers")
            cookies = entry_json["request"].get("cookies")

            headers_str = self.list_to_dict_str(headers)
            cookies_str = self.list_to_dict_str(cookies)
            data_str = "data={}"
            if method == "post":
                # from-data
                params = entry_json["request"]["postData"].get("params")
                if params is not None:
                    params_dict = self.list_to_dict_str(params)
                    data_str = "data=" + params_dict

                # json
                text = entry_json["request"]["postData"].get("text")
                mime_type = entry_json["request"]["postData"].get("mimeType")
                if mime_type is not None:
                    if mime_type == "application/json":
                        data_str = "json=" + text

            elif method == "get":
                # developing
                pass
            elif method == "put":
                # developing
                pass
            elif method == "delete":
                # developing
                pass

            testcase = self.case_template.format(header=headers_str, cookie=cookies_str,method=method, url=url, params=data_str)

        return testcase

    def create_file(self, save_path, file_content=""):
        """
        create test case file
        """
        with open(save_path, 'w') as f:
            f.write(file_content)
        msg = "created file: {}".format(save_path)
        log.info(msg)

    def gen_testcase(self):
        har_file = os.path.splitext(self.har_file_path)[0]
        output_testcase_file = "{}.py".format(har_file)
        print(output_testcase_file)

        log.info("Start to generate testcase.")
        testcase = self._make_testcase()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.create_file(os.path.join(BASE_DIR, output_testcase_file), testcase)


if __name__ == '__main__':

    hp = HarParser("./post_json.har")
    hp.gen_testcase()

