import seldom
from seldom.logging import log
from seldom.websocket_client import WebSocketClient


class WebSocketTest(seldom.TestCase):

    def start(self):
        """创建WebSocket客户端线程"""
        self.client = WebSocketClient("ws://127.0.0.1:8765/echo")
        self.client.start()
        # 等待客户端连接建立
        self.sleep(1)

    def end(self):
        """发送关闭消息"""
        self.client.send_message("close")
        # 停止WebSocket客户端线程
        self.client.stop()
        self.client.join()

    def test_send_and_receive_message(self):
        """
        测试发送送消息用例
        """
        self.client.send_message("Hello, WebSocket!")
        self.client.join(1)
        self.client.send_message("How are you?")
        self.client.join(1)
        # 验证是否收到消息
        log.info(self.client.received_messages)
        self.assertEqual(len(self.client.received_messages), 2)
        self.assertIn("Hello, WebSocket!", self.client.received_messages[0])
        self.assertIn("How are you?", self.client.received_messages[1])


if __name__ == '__main__':
    seldom.main(debug=True)
