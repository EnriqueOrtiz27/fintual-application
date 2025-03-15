from abc import ABC, abstractmethod
from datetime import datetime

from domain.enums import Ticker


class StockPriceAbstractRepository(ABC):
    @abstractmethod
    def price(self, date: datetime, ticker: Ticker) -> float:
        pass
