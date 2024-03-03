# API Object

API Object Models，简称AOM，AOM是一种设计模式，它围绕着将API、路由或功能交互及其相关行为封装在结构良好的对象中。AOM旨在增强API测试和集成的直观性和弹性。在实践中，AOM需要精心设计专门的API对象，以有效地保护用户免受与API 请求、响应、端点交互和身份验证过程相关的复杂性的影响。


seldom 支持AOM, 并且提供了一些好用的功能，辅助你使用AOM.

* 目录结构如下

```shell
mypro/
├── api/
│   ├── __init__.py
│   ├── auth_object.py
│   └── xxx_object.py
├── test_dir/
│   └── test_case.py
│  ...
```

* 创建 API Object

```python
# api/auth_object.py
from seldom.testdata import get_int
from seldom.request import HttpRequest
from seldom.request import check_response


class AuthAPIObject(HttpRequest):

    def __init__(self, api_key):
        self.api_key = api_key

    @check_response(ret="form.token")
    def get_token(self, user_id:str) -> str:
        """
        模拟：根据用户ID生成登录token
        :param user_id:
        :return:
        """
        data = {"user_id": user_id, "token": "t" + str(get_int(10000, 99999))}
        r = self.post("/post?key=" + self.api_key, data=data)
        return r
```

* 创建测试用例

```python
# test_dir/test_case.py
import seldom
from api.auth_object import AuthAPIObject


class TestAPI(seldom.TestCase):

    def test_case(self):
        auth_object = AuthAPIObject(api_key="abc123")
        token = auth_object.get_token(user_id="123")
        print("token", token)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
```

* AOM 原则

首先，接口只允许通过的APIObject进行封装，那么在封装之前可以检索一下是否有封装了，如果有，进一步确认是否满足自己的调用需求，我们一般在测试接口的时候一般各种参数验证，当API作为依赖接口调用的时候，一般参数比较少且固定，所以，API在封装的时候要兼顾到这两种情况。

其次，用例层只能通过APIObject的封装调用接口，像登录token这种大部分接口会用到的信息，可以通过类初始化时传入，后续调用类下面方法的时候就不需要关心的。如果是多个接口组成一个场景，也可以再进行一层业务层的封装。
