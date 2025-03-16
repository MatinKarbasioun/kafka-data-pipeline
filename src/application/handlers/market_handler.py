from src.domain.market_price import MarketPriceEntity
from src.repository.aggregated_trade_repo import IAggregatedTradeRepository
from src.repository.market_kline_repo import IMarketKLineRepository
from src.repository.market_price_repo import IMarketPriceRepository


class MarketHandler:
    def __init__(self, market_price_repo: IMarketPriceRepository,
                 aggregated_trade_repo: IAggregatedTradeRepository,
                 market_kline_repo: IMarketKLineRepository):
        self.__market_price_repo = market_price_repo
        self.__aggregated_trade_repo = aggregated_trade_repo
        self.__market_kline_repo = market_kline_repo

    async def add_market_price(self, market_price: MarketPriceEntity):
        self.__market_price_repo.add(market_price)

    async def get_market_price(self, ticker: str) -> MarketPriceEntity:
        return self.__market_price_repo.get(ticker)
