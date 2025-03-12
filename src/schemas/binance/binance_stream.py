from pydantic import BaseModel

from src.schemas.binance.binance_topic import IBinanceTopic


class BinanceStream(BaseModel):
    stream: str
    data: IBinanceTopic