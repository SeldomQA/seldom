"""
需要安装 uiautomator2: https://github.com/openatx/uiautomator2
> pip install uiautomator2
"""
import seldom
import uiautomator2 as u2


class MyAppTest(seldom.TestCase):

    def start(self):
        # 链接设备
        self.d = u2.connect('192.168.31.234')
        # 启动App
        self.d.app_start("com.meizu.mzbbs")

    def end(self):
        # 停止app
        self.d.app_stop("com.meizu.mzbbs")

    def test_app(self, user):
        """ 使用 uiautomator2 """
        # 搜索
        self.d(resourceId="com.meizu.flyme.flymebbs:id/nw").click()
        # 输入关键字
        self.d(resourceId="com.meizu.flyme.flymebbs:id/nw").set_text("flyme")
        # 搜索按钮
        self.d(resourceId="com.meizu.flyme.flymebbs:id/o1").click()
        self.sleep(2)


if __name__ == '__main__':
    seldom.main(debug=True)
