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
