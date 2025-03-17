import asyncio

from websockets.asyncio.server import serve, ServerConnection


class WebSocketServer:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__handler = None
        self.__server: serve | None = None

    def add_handler(self, handler):
        self.__handler = handler

    async def __listen(self, websocket: ServerConnection):
        print(websocket)
        await websocket.send('hello from websocket')

    async def start(self):
        # set this future to exit the server
        self.__server = await serve(self.__listen, self.__host, self.__port)
        await self.__server.serve_forever()

    async def one_call_start(self):
        stop = await asyncio.get_running_loop().create_future()

        async with serve(self.__listen, self.__host, self.__port):
            await stop

    async def stop(self):
        await self.__server.create_server