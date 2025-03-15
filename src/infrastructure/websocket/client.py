import asyncio
import json
from typing import Optional
from websockets import connect, ClientConnection, ConnectionClosed
import logging

from src.application.websocket.handler import IWebSocketHandler

logger = logging.getLogger(__name__)

"""
Parameters:
open_timeout (float | None) – Timeout for opening the connection in seconds. None disables the timeout.

ping_interval (float | None) – Interval between keepalive pings in seconds. None disables keepalive.

ping_timeout (float | None) – Timeout for keepalive pings in seconds. None disables timeouts.

close_timeout (float | None) – Timeout for closing the connection in seconds. None disables the timeout.
"""

class WebsocketClient:
    def __init__(self, ping_time: int, ping_interval: int):
        self.__ping_timeout = ping_time # 600
        self.__ping_interval = ping_interval # 180
        self.__connected = True
        self.websocket: Optional[ClientConnection] = None
        self.__ws_handler: IWebSocketHandler = None

    async def add_handler(self, ws_handler: IWebSocketHandler):
        self.__ws_handler = ws_handler

    async def connect(self, url: str):
        async for websocket in connect(url, ping_timeout=self.__ping_timeout, ping_interval=self.__ping_interval):
            try:
                if self.__connected:
                    await self.__listen(websocket)

                else:
                    break

            except ConnectionClosed:
                continue

    async def __listen(self, ws):
        try:
            async for message in ws:
                data = json.loads(message)
                await self.consumer_handler(data)

        except Exception as e:
            logger.error('ws client raised error', exc_info=e)

    async def consumer_handler(self, msg: dict):
        self.__ws_handler.on_receive(msg)



if __name__ == '__main__':
    ws = WebsocketClient(ping_time=600, ping_interval=180)
    asyncio.run(ws.connect("wss://fstream.binance.com/stream?streams=bnbusdt@aggTrade/btcusdt@markPrice"))
