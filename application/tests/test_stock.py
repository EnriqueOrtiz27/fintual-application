from datetime import datetime

from application.stock import build_stock_entity, Stock
from application.tests.mocks import MockStockPriceRepository, get_fintual_stock
from domain.enums import Ticker

fintual_stock = get_fintual_stock()


def test_build_stock_entity():
    assert build_stock_entity(Ticker.FNTL) == fintual_stock


def test_stock_class_should_call_stock_price_repo():
    fintual_price = 3243
    apple_price = 100
    stock = Stock(
        stock=fintual_stock,
        stock_price_repo=MockStockPriceRepository(
            fintual_price=fintual_price, apple_price=apple_price
        ),
    )
    assert stock.price(datetime.today()) == fintual_price
