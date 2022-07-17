# import time
# import asyncio
# from arsenic import get_session, keys, browsers, services
#
#
# async def hello_world():
#     service = services.Chromedriver()
#     browser = browsers.Chrome()
#     async with get_session(service, browser) as session:
#         await session.get('http://www.baidu.com/')
#         search_box = await session.wait_for_element(5, '#kw')
#         await search_box.send_keys('seldom')
#         await search_box.send_keys(keys.ENTER)
#
#
# def main():
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(hello_world())
#
#
# if __name__ == '__main__':
#     start = time.time()
#     main()
#     print("running time:", time.time() - start)
import sys
from loguru import logger

fmt = "{time} | {level} |  {message}"
logger.add(sys.stderr, format=fmt)

logger.info("That's it, beautiful and simple logging!")

