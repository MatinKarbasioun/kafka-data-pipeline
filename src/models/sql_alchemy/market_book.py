from sqlalchemy import Column, BIGINT, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB

from src.infrastructure.db_management.base_model import Base


class MarketBook(Base):
    __tablename__ = 'market_price'
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    ticker = Column(String, nullable=False)
    event_time = Column(TIMESTAMP, nullable=False)
    transaction_time = Column(TIMESTAMP, nullable=False)
    orderbook = Column(JSONB, nullable=False)