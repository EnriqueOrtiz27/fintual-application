from datetime import datetime

from domain.entities import StockEntity
from domain.enums import Ticker
from domain.repositories import StockPriceAbstractRepository


class MockStockPriceRepository(StockPriceAbstractRepository):
    def __init__(self, fintual_price: int, apple_price: int):
        self.fintual_price = fintual_price
        self.apple_price = apple_price

    def price(self, date: datetime, ticker: str) -> float:
        return self.fintual_price if ticker == Ticker.FNTL.value else self.apple_price


def get_fintual_stock():
    return StockEntity(
        ticker=Ticker.FNTL,
        official_name="Fintual Corporation Common Stock",
        display_name="Fintual",
    )


def get_apple_stock():
    return StockEntity(
        ticker=Ticker.AAPL,
        official_name="Apple Inc. Common Stock",
        display_name="Apple",
    )
