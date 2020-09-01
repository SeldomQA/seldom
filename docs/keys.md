### 键盘操作

有时候我们需要用到键盘操作，比如enter，Backspace，TAB键，或者全选（ctrl/command + a）、复制（ctrl/command + c）组合键操作。

```py
import seldom


class Test(seldom.TestCase):

    def test_key(self):
        self.open("https://www.baidu.com")

        # 输入 seldomm
        self.Keys(css="#kw").input("seldomm")

        # 删除多输入的一个m
        self.Keys(id_="kw").backspace()

        # 输入“教程”
        self.Keys(id_="kw").input("教程")

        # ctrl+a 全选输入框内容
        self.Keys(id_="kw").select_all()

        # ctrl+x 剪切输入框内容
        self.Keys(id_="kw").cut()

        # ctrl+v 粘贴内容到输入框
        self.Keys(id_="kw").paste()

        # 通过回车键来代替单击操作
        self.Keys(id_="kw").enter()


if __name__ == '__main__':
    seldom.main(browser="firefox", debug=True)

```
