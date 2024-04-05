import websocket
from threading import Thread
from seldom.logging import log


class WebSocketClient(Thread):

    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        self.ws = None
        self.running = False
        self.received_messages = []

    def run(self):
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
        try:
            if self.ws:
                self.ws.send(message)
        except Exception as e:
            self.on_error(e)

    def stop(self):
        self.running = False
        if self.ws:
            self.ws.close()

    def on_open(self):
        log.info("WebSocket connection opened.")

    def on_error(self, error):
        log.error(f"WebSocket error: {error}")

    def on_close(self):
        log.info("WebSocket connection closed.")
        self.running = False
