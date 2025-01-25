from threading import Thread

import websocket

from seldom.logging import log


class WebSocketClient(Thread):
    """
    WebSocket Client class
    """

    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        self.ws = None
        self.running = False
        self.received_messages = []

    def run(self):
        """
        Run WebSocket.
        Returns:
        """
        self.running = True
        try:
            self.ws = websocket.create_connection(self.url)
            self.on_open()
        except Exception as e:
            self.on_error(e)
            self.running = False
            return

        while self.running:
            try:
                message = self.ws.recv()
                if message is None:
                    self.on_close()
                    break
                self.received_messages.append(message)
            except websocket.WebSocketConnectionClosedException as e:
                log.error(e)
                self.on_close()
                break
            except Exception as e:
                self.on_error(e)
                break

    def send_message(self, message):
        """
        send message.
        :param message:
        :return:
        """
        try:
            if self.ws:
                self.ws.send(message)
        except Exception as e:
            self.on_error(e)

    def stop(self):
        """
        stop and close WebSocket.
        """
        self.running = False
        if self.ws:
            self.ws.close()

    @staticmethod
    def on_open():
        """
        Open WebSocket connection.
        :return:
        """
        log.info("WebSocket connection opened.")

    @staticmethod
    def on_error(error):
        """
        WebSocket error info.
        :param error:
        :return:
        """
        log.error(f"WebSocket error: {error}")

    def on_close(self):
        """
        Close WebSocket connection.
        :return:
        """
        log.info("WebSocket connection closed.")
        self.running = False
