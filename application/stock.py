import logging
from datetime import datetime

from domain.entities import StockEntity
from domain.enums import Ticker
from domain.repositories import StockPriceAbstractRepository

logger = logging.getLogger(__name__)


def build_stock_entity(ticker: Ticker) -> StockEntity:
    mapping = {
        Ticker.AAPL: {
            "official_name": "Apple Inc. Common Stock",
            "display_name": "Apple",
        },
        Ticker.FNTL: {
            "official_name": "Fintual Corporation Common Stock",
            "display_name": "Fintual",
        },
    }

    return StockEntity(
        ticker=ticker,
        official_name=mapping[ticker]["official_name"],
        display_name=mapping[ticker]["display_name"],
    )


class Stock:
    def __init__(
        self, stock: StockEntity, stock_price_repo: StockPriceAbstractRepository
    ):
        self.ticker = stock.ticker
        self.official_name = stock.official_name
        self.display_name = stock.display_name
        self.repo = stock_price_repo

    def __repr__(self):
        return f"{self.ticker.value} - ({self.display_name})"

    def price(self, date: datetime) -> float:
        logger.info(f"Getting price for {self.ticker} on {date}")
        stock_price = self.repo.price(date=date, ticker=self.ticker.value)
        logger.info(
            f"Stock {self.ticker} was worth {stock_price} on {date.strftime('%Y-%m-%d')}"
        )
        return stock_price
