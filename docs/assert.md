## seldom 断言

seldom 提供了更加简单的断言方法。

断言方法如下：

```python
# 断言标题是否等于"title"
self.assertTitle("title")

# 断言标题是否包含"title"
self.assertInTitle("title")

# 断言URL是否等于
self.assertURL("url")

# 断言URL是否包含
self.assertInURL("url")

# 断言页面是否存在“text”
self.assertText("text")

# 断言警告是否存在"text" 提示信息
self.assertAlertText("text")
```
