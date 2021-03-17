import seldom


class BaiduTest(seldom.TestCase):
    """Baidu search test case"""

    def test_case(self):
        """A simple test"""
        self.open("https://www.baidu.com/")
        self.max_window()
        self.click_and_hold(css="#s-usersetting-top")
        self.click(link_text="搜索设置")
        self.click(css="#SL_1")
        self.click(css="#se-setting-7 > a", index=1)
        self.sleep(2)
        self.assertAlertText("已经记录下您的使用偏好")
        self.accept_alert()


if __name__ == '__main__':
    seldom.main(debug=True)

