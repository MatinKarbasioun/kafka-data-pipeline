from typing import NamedTuple


class MarketPriceEntity:
    event_type: str
    event_time: int
    symbol: str
    market_price: str
    index_price: str
    estimated_settlement_price: str
    funding_rate: str
    next_funding_time: int