import requests


def swagger_to_seldom_case(swagger_doc_url):
    # 从Swagger文档URL获取Swagger文档
    swagger_doc = requests.get(swagger_doc_url).json()

    # 提取路径和方法信息
    paths = swagger_doc['paths']
    for path, methods in paths.items():
        for method, details in methods.items():
            # 提取请求信息
            http_method = method.upper()
            url = 'https://petstore.swagger.io/v2' + path
            parameters = details.get('parameters', [])
            query_params = {}
            body_param = {}
            headers = {}

            for param in parameters:
                if param['in'] == 'query':
                    query_params[param['name']] = 'example_value'
                elif param['in'] == 'body':
                    body_param = {'data': 'example_data'}
                elif param['in'] == 'header':
                    headers[param['name']] = 'example_header_value'

            # 生成requests库的代码
            request_code = f"response = requests.{http_method}('{url}', params={query_params}, json={body_param}, headers={headers})"
            print(request_code)


if __name__ == '__main__':
    # 使用示例
    swagger_to_seldom_case('https://petstore.swagger.io/v2/swagger.json')
