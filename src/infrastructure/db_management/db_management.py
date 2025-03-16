from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from .base_model import Base


class AsyncEngine:
    engine: AsyncEngine | None = None

    def __init__(self, db_url):
        self.__db_url = db_url
        self.__engine: None | AsyncEngine = None
        AsyncEngine.Engine = create_async_engine(self.__db_url)

    def create_all(self):
        async with self.__engine.connect() as connection:
            connection.run_sync(Base.metadata.create_all)

    def drop_all(self):
        async with self.__engine.connect() as connection:
            connection.run_sync(Base.metadata.drop_all)