from datetime import datetime
from decimal import Decimal
from typing import NamedTuple

from src.domain.value_objects.interval import Interval


class CandleStickEntity(NamedTuple):
    ticker: str
    interval: Interval
    event_datetime: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    base_volumes: Decimal
    quote_volumes: Decimal
    trade_numbers: int
