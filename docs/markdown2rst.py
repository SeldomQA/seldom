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
    # markdown_to_rst("driver.md", "rst_docs/driver.rst")
    # markdown_to_rst("run_test.md", "rst_docs/run_test.rst")
    # markdown_to_rst("main.md", "rst_docs/main.rst")
    # markdown_to_rst("reports.md", "rst_docs/reports.rst")

    # markdown_to_rst("find_element.md", "rst_docs/find_element.rst")
    # markdown_to_rst("seldom_api.md", "rst_docs/seldom_api.rst")
    # markdown_to_rst("assertion.md", "rst_docs/assertion.rst")

    # markdown_to_rst("rerun_screenshot.md", "rst_docs/rerun_screenshot.rst")
    markdown_to_rst("parameterized.md", "rst_docs/parameterized.rst")
    markdown_to_rst("poium.md", "rst_docs/poium.rst")
    markdown_to_rst("testdata.md", "rst_docs/testdata.rst")
    markdown_to_rst("skip.md", "rst_docs/skip.rst")
    markdown_to_rst("send_mail.md", "rst_docs/send_mail.rst")
    markdown_to_rst("depend.md", "rst_docs/depend.rst")
