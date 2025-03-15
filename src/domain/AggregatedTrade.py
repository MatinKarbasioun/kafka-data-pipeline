from decimal import Decimal
from typing import NamedTuple


class AggregatedTrade(NamedTuple):
    event_type: str
    event_type: int
    symbol: str
    aggregate_trade_id: str
    price: Decimal
    quantity: Decimal
    first_trade_id: int
    last_trade_id: int
    trade_time: int
    is_market_maker: bool