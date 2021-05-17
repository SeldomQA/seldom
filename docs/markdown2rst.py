import requests


def markdown_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    :param from_file: markdown文件的路径
    :param to_file: rst文件的路径
    """
    resp = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if resp.ok:
        with open(to_file, "wb") as f:
            f.write(resp.content)


if __name__ == '__main__':
    # markdown_to_rst("installation.md", "rst_docs/installation.rst")
    # markdown_to_rst("create_project.md", "rst_docs/create_project.rst")
    # markdown_to_rst("quick_start.md", "rst_docs/quick_start.rst")
    # markdown_to_rst("seldom_api.md", "rst_docs/seldom_api.rst")
    # markdown_to_rst("advanced.md", "rst_docs/advanced.rst")
    # markdown_to_rst("other.md", "rst_docs/other.rst")
    # markdown_to_rst("http.md", "rst_docs/http.rst")
    markdown_to_rst("db_operation.md", "rst_docs/db_operation.rst")
