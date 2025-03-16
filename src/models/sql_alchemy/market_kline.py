from sqlalchemy import Column, BIGINT, Numeric, String, TIMESTAMP

from src.infrastructure.db_management.base_model import Base


class MarketKLines(Base):
    __tablename__ = 'market_klines'
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    ticker = Column(String, nullable=False)
    event_time = Column(TIMESTAMP, nullable=False)
    interval = Column(String, nullable=False)
    open = Column(Numeric(20, 10), nullable=False)
    high = Column(Numeric(20, 10), nullable=False)
    low = Column(Numeric(20, 10), nullable=False)
    close = Column(Numeric(20, 10), nullable=False)
    base_asset_volume = Column(Numeric(40, 10), nullable=False)
    quote_asset_volume = Column(Numeric(40, 10), nullable=False)
    trade_numbers = Column(BIGINT, nullable=False)