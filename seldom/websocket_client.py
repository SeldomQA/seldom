import websocket
from threading import Thread
from seldom.logging import log


class WebSocketClient(Thread):

    def __init__(self, url):
        Thread.__init__(self)
        self.ws = websocket.create_connection(url)
        self.running = True
        self.received_messages = []

    def run(self):
        while self.running:
            try:
                message = self.ws.recv()
                self.received_messages.append(message)
            except websocket.WebSocketConnectionClosedException:
                break
            except Exception as e:
                log.error(f"WebSocket error: {e}")
                break
        self.ws.close()

    def send_message(self, message):
        self.ws.send(message)

    def stop(self):
        self.running = False
