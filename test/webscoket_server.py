import asyncio
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
