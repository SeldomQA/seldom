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
    markdown_to_rst("README.md", "index.rst")
