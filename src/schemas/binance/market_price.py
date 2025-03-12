from src.schemas.binance.binance_topic import IBinanceTopic


class MarketPrice(IBinanceTopic):
    e: str
    E: int
    s: str
    p: str
    i: str
    P: str
    r: str
    T: int