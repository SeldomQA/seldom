import aiohttp
from aiohttp import web


async def websocket_handler(request):
    """
    WebSocket handler
    :param request:
    :return:
    """
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(f"Message text was: {msg.data}")
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')

    print('websocket connection closed')

    return ws


app = web.Application()
app.router.add_get('/echo', websocket_handler)

if __name__ == '__main__':
    web.run_app(app, port=8765)
