# 支持Excel测试用例

> seldom > 3.8.0

在编写接口测试用例的时候，有时候测试用例非常简单，比如单接口的测试，不需要登录token，不存在用例数据依赖，也不需要参数加密，此时，使用`Excel`
文件编写用例更为高效。

seldom支持了这种用例的编写。

### 编写Excel用例

首先，创建一个Excel文件，格式如下。

| name            | api   | method | headers | param_type | params | assert | exclude |
|-----------------|-------|--------|---------|------------|--------|--------|---------|
| 简单GET接口         | /get  | GET    | {}      | data       | {}     | {}     | []      |
| 简单POST接口-json参数 | /post | POST   | {}      | json       | {}     | {}     | []      |
| ...             |       |        |         |            |        |        |         |

__参数说明__

| 字段           | 说明                                                    | 列子                                                   | 
|--------------|-------------------------------------------------------|------------------------------------------------------|
| `name`       | 用例的名称，会在测试报告中展示。                                      |                                                      | 
| `api`        | 接口的地址，可以写完整的URL地址, 也可以只定义路径，`base_url` 在 `confrun.py` | 例如：`http://www.httpbin.org/get` or `/get`            |
| `method`     | 接口的请求方法，必须大写，不允许为空                                    | 支持：`GET`、`POST`、`PUT`、`DELETE`                       |
| `headers`    | 请求头，不允许为空，默认为 `{}`，字段必须双引号`"`。                        | 例如：`{"user-agent": "my-app/0.0.1"}`                  |
| `param_type` | 接口参数类型，必须小写，不允许为空。                                    | 例如：`data`、 `json`                                    |
| `params`     | 接口参数，不允许为空，默认为 `{}`，字段必须双引号`"`。                       | 例如：`{"id": 1, "name": "jack"}`                       |
| `assert`     | 断言接口返回，允许为空 或 `{}`，                                   | 例如：`{"status": 200, "success": True, "data": [...]}` |
| `exclude`    | 断言过滤字段，一些特殊的字段会导致断言失败，需要过滤掉。                          | 例如：`["X-Amzn-Trace-Id", "timestamp"]`                |

__confrun.py配置__

```python

def base_url():
    """
    http test
    api base url
    """
    return "http://www.httpbin.org"

```

### seldom测试WebSocket

在seldom中测试WebSocket非常简单。

* 首先，需要一个WebSocket服务。

通过`aiohttp`实现`websocket_server.py`。

```shell
# websocket_server.py
from aiohttp import web
import aiohttp


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            print("message", msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(f"Message text was: {msg.data}")
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws


app = web.Application()
app.router.add_get('/ws', websocket_handler)

web.run_app(app, port=8765)
```

* 然后，通过seldom编写WebSocket测试用例。

```shell
import seldom
from seldom.logging import log
from seldom.websocket_client import WebSocketClient


class WebSocketTest(seldom.TestCase):

    def start(self):
        # 创建WebSocket客户端线程
        self.client = WebSocketClient("ws://0.0.0.0:8765/ws")
        self.client.start()
        # 等待客户端连接建立
        self.sleep(1)  # 这里假设服务器可以在1秒内响应连接

    def tearDown(self):
        # 发送关闭消息
        self.client.send_message("close")
        # 停止WebSocket客户端线程
        self.client.stop()
        self.client.join()

    def test_send_and_receive_message(self):
        # 发送消息
        self.client.send_message("Hello, WebSocket!")
        self.client.join(1)  # 等待接收消息
        self.client.send_message("How are you?")
        self.client.join(1)  # 等待接收消息
        # 验证是否收到消息
        log.info(self.client.received_messages)
        self.assertEqual(len(self.client.received_messages), 2)
        self.assertIn("Hello, WebSocket!", self.client.received_messages[0])
        self.assertIn("How are you?", self.client.received_messages[1])


if __name__ == '__main__':
    seldom.main(debug=True)
```

* 运行日志

```shell
> python test_websocket.py

test_send_and_receive_message (test_websocket.WebSocketTest.test_send_and_receive_message) ... 
2024-04-05 23:36:33 | INFO     | case.py | 💤️ sleep: 1s.
2024-04-05 23:36:33 | INFO     | websocket_client.py | WebSocket connection opened.
2024-04-05 23:36:36 | INFO     | test_websocket.py | ['Message text was: Hello, WebSocket!', 'Message text was: How are you?']
ok

----------------------------------------------------------------------
Ran 1 test in 3.006s

OK
2024-04-05 23:36:36 | SUCCESS  | runner.py | A run the test in debug mode without generating HTML report!

```