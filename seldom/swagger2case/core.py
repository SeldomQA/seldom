import json
import requests


def swagger_to_requests(swagger_doc):
    paths = swagger_doc['paths']
    # definitions = swagger_doc.get('definitions', {})
    seldom_code = '''from seldom.request import HttpRequest

class Common(HttpRequest):

'''
    api_modules = {}
    for path, methods in paths.items():
        api_name = path.replace('/', '_') + "_api"
        api_modules[api_name] = {}

        for method, opts in methods.items():

            func_code = f"    def test_{api_name}_{method}(self"

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

            func_params = path_params + query_params + header_params
            if len(func_params) > 0:
                func_code += ", "
            func_code += ", ".join(func_params) + "):"

            # 请求处理
            func_code += f'\n        url = "{swagger_doc["schemes"][0]}://{swagger_doc["host"]}{path}"'

            query_dict = ", ".join([f"{p}={p}" for p in query_params])
            if query_dict:
                func_code += f'\n        params = {{{query_dict}}}'

            func_code += f'\n        headers = {{}}'
            if header_params:
                headers_dict = ", ".join([f"'{p}': {p}" for p in header_params])
                func_code += f'\n        headers = {{{headers_dict}}}'

            consumes = opts.get('consumes', ['application/json'])
            func_code += f'\n        headers["Content-Type"] = "{consumes[0]}"'

            if form_params:
                form_dict = ", ".join([f"'{p}': {p}" for p in form_params])
                func_code += f'\n        data = {{{form_dict}}}'

            # 请求发送
            req_method = method.lower()
            func_code += f'\n        r = self.{req_method}(url, headers=headers, params=params, data=data)'
            func_code += f"\n        print(r.status_code)"

            # 添加函数定义
            # print(func_code)
            seldom_code += func_code + "\n\n"

    print("\n", seldom_code)
    return api_modules


if __name__ == '__main__':
    # 从Swagger文档URL获取Swagger文档
    swagger_doc = requests.get("https://petstore.swagger.io/v2/swagger.json").json()
    apis = swagger_to_requests(swagger_doc)
