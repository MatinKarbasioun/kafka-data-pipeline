import asyncio
import json
from typing import Optional

import websockets
from websockets import connect
import logging

from src.application.kafka.consumer.consumer import logger

logger = logger.getLogger(__name__)


class WebsocketClient:
    def __inti__(self, ping_time: int, ping_interval: int):
        self.__max_retries = 5
        self.__retry_delay = 0.1
        self.__ping_timeout = ping_time
        self.__ping_interval = ping_interval
        self.__connected = True
        self.websocket: Optional[websockets.ClientConnection] = None


    async def connect(self, url: str):

        retry_attempts = 0

        while retry_attempts < self.__max_retries and self.__connected:
            async for websocket in connect(url, ping_timeout=600, ping_interval=180):
                try:
                    await consumer_handler(websocket)
                except websockets.exceptions.ConnectionClosed:
                    continue
            await asyncio.sleep(self.__retry_delay)

    async def listen(self, ws):
        try:
            async for message in self.websocket:
                data = json.loads(message)
                await self.handle_message(data)
        except websockets.ConnectionClosed:
            logger.warning("WebSocket connection lost. Reconnecting...")
            await self.connect()

async def consumer_handler(websocket):
    async for message in websocket:
        print(message)

async def ws_connect(url):
    async for websocket in connect(url, ping_timeout=600, ping_interval=180):
        try:
            await consumer_handler(websocket)
        except websockets.exceptions.ConnectionClosed:
            continue


if __name__ == '__main__':
    asyncio.run(ws_connect("wss://fstream.binance.com/ws/bnbusdt@aggTrade"))
