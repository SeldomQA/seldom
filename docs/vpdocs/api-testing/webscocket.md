# WebSocket

> seldom > 3.6.0 支持该功能

有些时间我们需要通过`WebSocket`实现长连接，很高兴的告诉告诉你seldom支持`WebSocket`测试了。

### WebSocket 生命周期

WebSocket 生命周期中包含几个关键的事件，这些事件允许开发人员在连接的不同阶段执行代码。以下是WebSocket API中定义的主要事件：

* `open`: 当WebSocket连接成功建立时触发。这个事件表明客户端与服务器之间的连接已经打开，可以开始数据传输。

* `message`: 当客户端接收到服务器发送的消息时触发。这个事件用于处理从服务器接收到的所有消息。

* `error`: 当发生错误，导致WebSocket连接关闭之前或连接无法成功建立时触发。这个事件可以用来处理和响应WebSocket过程中出现的任何异常或错误情况。

* `close`: 当连接被关闭时触发，无论是客户端还是服务器端主动关闭连接，或是因为某种原因连接被迫关闭。这个事件表明WebSocket连接已经彻底关闭，可以进行清理和后续处理。

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