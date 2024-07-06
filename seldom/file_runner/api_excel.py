import seldom
from seldom import file_data
import json
from seldom.logging import log
from seldom.running.config import FileRunningConfig


class APITest(seldom.TestCase):

    @file_data(FileRunningConfig.api_excel_file_name, line=2)
    def test_api_excel(self, name, url, method, headers, param_type, param, assert_resp, exclude):
        """
        case name
        """
        log.info(f"execute api case: [{name}]")

        param_dict = json.loads(param)
        headers_dict = json.loads(headers)

        if method == "GET":
            self.get(url=url, params=param_dict, headers=headers_dict)
        elif method == "POST":
            if param_type == "data":
                self.post(url=url, data=param_dict, headers=headers_dict)
            elif param_type == "json":
                self.post(url=url, json=param_dict, headers=headers_dict)
            else:
                raise ValueError("param_typ error")
        elif method == "PUT":
            if param_type == "data":
                self.put(url=url, data=param_dict, headers=headers_dict)
            elif param_type == "json":
                self.put(url=url, json=param_dict, headers=headers_dict)
            else:
                raise ValueError("param_typ error")
        elif method == "DELETE":
            if param_type == "data":
                self.delete(url=url, data=param_dict, headers=headers_dict)
            elif param_type == "json":
                self.delete(url=url, json=param_dict, headers=headers_dict)
            else:
                raise ValueError("param_typ error")
        else:
            raise ValueError("method error")

        if assert_resp != "" or assert_resp != "{}":
            assert_resp = json.loads(assert_resp)
            self.assertJSON(assert_resp, exclude=exclude)
