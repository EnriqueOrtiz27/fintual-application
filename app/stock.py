import logging
from datetime import datetime

from domain.business_entities import StockModel

logger = logging.getLogger(__name__)


class Stock:
    def __init__(self, stock: StockModel):
        self.symbol = stock.symbol
        self.exchange = stock.exchange
        self.official_name = stock.official_name
        self.display_name = stock.display_name

    def __repr__(self):
        return f"{self.symbol.value} - ({self.display_name})"

    def price(self, date: datetime, randomize: bool = False) -> int:
        """
        Get the price of the stock on a given date.
        To keep things simple, we will return 100 unless one wants
        to simulate a random change.

        :param date: date on which to get the price
        :param randomize: true if you want to add some change to the stock price;
        this change will be the same on a given day, but will change between days.
        :return: stock price
        """
        logger.info(f"Getting price for {self.symbol} on {date}")
        stock_value = 100
        if randomize:
            day = date.day
            sign = 1 if day % 2 == 0 else -1
            stock_value = 100 + (day * sign)

        logger.info(
            f"Stock {self.symbol} was worth {stock_value} on {date.strftime('%Y-%m-%d')}"
        )
        return stock_value
