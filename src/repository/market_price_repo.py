from abc import ABC, abstractmethod
from datetime import datetime

from src.domain.market_price import MarketPriceEntity



class IMarketPriceRepository(ABC):

    @abstractmethod
    async def add(self, market_price: MarketPriceEntity):
        raise NotImplementedError

    @abstractmethod
    async def get(self, market_price: MarketPriceEntity):
        raise NotImplementedError

    @abstractmethod
    async def get_historical(self, from_date: datetime | None = None, to_date: datetime | None = None):
        raise NotImplementedError
