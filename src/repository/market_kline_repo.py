from abc import ABC, abstractmethod
from datetime import datetime

from src.domain.market_price import MarketPriceEntity


class IMarketKLineRepository(ABC):

    @abstractmethod
    def add(self, market_price: MarketPriceEntity):
        raise NotImplementedError

    @abstractmethod
    def get(self, market_price: MarketPriceEntity):
        raise NotImplementedError

    @abstractmethod
    def get_historical(self, from_date: datetime | None = None, to_date: datetime | None = None):
        raise NotImplementedError
