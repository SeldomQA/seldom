import json
import requests
from seldom.logging import log
from seldom.utils.file_extend import file


class SwaggerParser:

    def __init__(self,  swagger: str, online=False):
        """
        :param swagger: file path or http address
        :param online: is online
        """
        self.swagger = swagger
        if online:
            self.doc = self.online_swagger_doc(self.swagger)
        else:
            self.doc = self.read_swagger_file(self.swagger)

    @staticmethod
    def read_swagger_file(file_path: str) -> dict:
        """
        read swagger file
        :param file_path:
        :return:
        """
        with open(file_path, "r+", encoding="utf-8") as json_file:
            doc = json.load(json_file)
            return doc

    @staticmethod
    def online_swagger_doc(url: str) -> dict:
        """
        read swagger file
        :param url:
        :return:
        """
        doc = requests.get(url).json()
        return doc

    @staticmethod
    def create_file(save_path: str, code: str = "") -> None:
        """
        create test case file
        """
        with open(save_path, 'w', encoding="utf8") as file:
            file.write(code)
        log.info(f"created file: {save_path}")

    def swagger_to_seldom_code(self, swagger_doc: dict) -> str:
        """
        swagger to seldom code
        :param swagger_doc: swagger doc
        :return:
        """

        paths = swagger_doc['paths']
        seldom_code = '''import seldom


class TestRequest(seldom.TestCase): 
    '''
        for path, methods in paths.items():
            api_name = path.replace('/', '_').replace('{', '').replace('}', '') + "_api"

            for method, opts in methods.items():

                func_code = f"\n    def test{api_name}_{method}(self):"

                # 参数处理
                parameters = opts.get('parameters', [])
                form_params = []
                path_params = []
                query_params = []
                header_params = []

                for param in parameters:
                    name = param['name']
                    if param['in'] == 'path':
                        path_params.append(name)
                    elif param['in'] == 'query':
                        query_params.append(name)
                    elif param['in'] == 'header':
                        header_params.append(name)
                    elif param['in'] == 'formData':
                        form_params.append(name)

                # request params
                func_code += f'\n        url = f"{swagger_doc["schemes"][0]}://{swagger_doc["host"]}{path}"'

                query_dict = ", ".join([f"\"{p}\": {p}" for p in query_params])
                if query_dict:
                    func_code += f'\n        params = {{{query_dict}}}'
                else:
                    func_code += f'\n        params = {{}}'

                if header_params:
                    headers_dict = ", ".join([f"\"{p}\": {p}" for p in header_params])
                    func_code += f'\n        headers = {{{headers_dict}}}'
                else:
                    func_code += f'\n        headers = {{}}'

                consumes = opts.get('consumes', ['application/json'])
                func_code += f'\n        headers["Content-Type"] = "{consumes[0]}"'

                if form_params:
                    form_dict = ", ".join([f"\"{p}\": {p}" for p in form_params])
                    func_code += f'\n        data = {{{form_dict}}}'
                else:
                    func_code += f'\n        data = {{}}'

                # request send
                req_method = method.lower()
                func_code += f'\n        r = self.{req_method}(url, headers=headers, params=params, data=data)'
                func_code += f"\n        print(r.status_code)"

                # add test method
                seldom_code += func_code + "\n\n"

        seldom_code += '''
if __name__ == '__main__':
    seldom.main()
    '''

        return seldom_code

    def gen_testcase(self) -> None:
        """
        generate test case
        """
        if "\\" in  self.swagger:
            swagger_file = self.swagger.split("\\")[-1]
        elif "/" in self.swagger:
            swagger_file = self.swagger.split("/")[-1]
        else:
            swagger_file = self.swagger
        if "." in swagger_file:
            swagger_file = swagger_file.split(".")[0]

        output_testcase_file = f"{swagger_file}.py"

        log.info("Start to generate testcase.")
        testcase = self.swagger_to_seldom_code(self.doc)

        self.create_file(file.join(file.dir, output_testcase_file), testcase)



if __name__ == '__main__':
    # online swagger doc
    # sp = SwaggerParser(swagger="https://petstore.swagger.io/v2/swagger.json", online=True)
    # sp.gen_testcase()
    # local swagger doc
    swagger_file_path = file.join(file.dir, "swagger.json")
    sp = SwaggerParser(swagger=swagger_file_path)
    sp.gen_testcase()
