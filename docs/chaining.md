## 链式调用

方法链接是一种技术，用于对同一个对象进行多个方法调用，只使用一次对象引用。

### 基本例子

先来看一下如何通过seldom使用链式调用编写Web测试用例。

```python
import seldom
from seldom import Case


class BaiduTest(seldom.TestCase):

    def test_search1(self):
        """
        百度搜索
        """
        Case(url="http://www.baidu.com", desc="百度搜索")\
            .open().find("#kw").type("seldom").find("#su").click()
        self.assertInTitle("seldom")


    def test_search2(self):
        """
        百度搜索
        """
        c = Case(desc="百度搜索")
        c.open("http://www.baidu.com")
        c.find("#kw").type("seldom").enter()
        self.assertInTitle("seldom")

if __name__ == '__main__':
    seldom.main(browser="gc", tester="虫师")
```

用例像链条一样将整个测试过程串联起来，当然，如果你讨厌换行符`\`，也可以将用例分成多次调用，总之，只要你愿意，可以将所有步骤都串联起来。


```python
import seldom
from seldom import Case


class BaiduTest(seldom.TestCase):

    def test_search_setting(self):
        """百度搜索设置"""
        Case(url="http://www.baidu.com", desc="百度搜索设置")\
            .open()\
            .find("#s-usersetting-top").click()\
            .find("#s-user-setting-menu > div > a.setpref").click().sleep(2)\
            .find('[data-tabid="advanced"]').click().sleep(2)\
            .find("#q5_1").click().sleep(2)\
            .find('[data-tabid="general"]').click().sleep(2)\
            .find_text("保存设置").click()\
            .alert().accept()


if __name__ == '__main__':
    seldom.main(browser="gc", tester="虫师")
```

### CaseAPI 

`Case` 类所提供的API 大部分和`Webidrver` 类保持一致，但考虑掉到链式的特点，命名上更体现`动作`。

__查找元素__

```python
from seldom import Case

c = Case()
c.find("#id")
c.find(".class")
c.find("[name=password]")
c.find("div > tr > td")
c.find("div", 1)

c.find_text("新闻")
```

* find(): 只支持CSS定位，这几乎是最强大的定位方法了。 新的测试库`cypress`、`playwright` 默认也都是CSS定位。

* find_text(): 用于定位文本，对个`find()` 定位的补充。

__操作方法__

```python
import seldom
from seldom import Case

class TestCase(seldom.TestCase):

    def test_chaining_api(self):
        Case(desc="chaining api")\
            .open("https://www.baidu.com")\
            .max_window()\
            .set_window(800, 600)\
            .find("css").clear()\
            .find("css").type("seldom")\
            .find("css").enter()\
            .find("css").submit()\
            .find("css").click()\
            .find("css").double_click()\
            .find("css").move_to_click()\
            .find("css").click_and_hold()\
            .find("css").switch_to_frame()\
            .find("css").select(value="")\
            .find("css").select(text="每页显示20条")\
            .find("css").select(index=2)\
            .switch_to_frame_out()\
            .switch_to_window(1)\
            .refresh()\
            .alert().accept()\
            .alert().dismiss()\
            .screenshots()\
            .element_screenshot()\
            .sleep(1)\
            .close()\
            .quit()

```

1. 基于元素定位的操作先调用`find()/find_text()`, 例如`type()`, `click()` 等。

2. `accept()/dismiss()` 是基于alert的操作。
