from datetime import datetime

import pytest

from application.portfolio import Portfolio
from application.tests.mocks import (
    get_fintual_stock,
    get_apple_stock,
    MockStockPriceRepository,
)
from domain.entities import PortfolioEntity, AllocationEntity
from domain.enums import RiskTolerance

"""
Replicating results from:
Days calculator: https://www.timeanddate.com/date/durationresult.html?m1=1&d1=1&y1=2025&m2=7&d2=1&y2=2025
Annualized Return Calculator: https://www.buyupside.com/calculators/annualizedreturn.htm
"""


data = [
    # (start_date, end_date, start_value, end_value, expected_annualized_return)
    # 1. start_value == end_value should return zero always
    (datetime(2025, 1, 1), datetime(2025, 1, 1), 1, 1, 0),
    (datetime(2025, 1, 1), datetime(2025, 11, 23), 1, 1, 0),
    # 2. Replicating examples with the links above
    # years held = 365/365, or 1
    (datetime(2025, 1, 1), datetime(2026, 1, 1), 200.59, 205.47, 2.43),
    # years held = 364/365
    (datetime(2025, 1, 1), datetime(2025, 12, 31), 100, 220, 120.48),
    # years held = 181/365
    (datetime(2025, 1, 1), datetime(2025, 7, 1), 100, 220, 390.37),
]


@pytest.mark.parametrize(
    "start_date, end_date, start_value, end_value, expected_annualized_return", data
)
def test_get_annualized_return(
    start_date, end_date, start_value, end_value, expected_annualized_return
):
    assert (
        Portfolio.get_annualized_return(
            start_date=start_date,
            end_date=end_date,
            start_value=start_value,
            end_value=end_value,
        )
        == expected_annualized_return
    )


def test_compute_portfolio_value_at_date():
    fintual_stock = get_fintual_stock()
    apple_stock = get_apple_stock()
    date = datetime.today()
    fintual_price = 100
    fintual_weight = 40
    apple_price = 200
    apple_weight = 60

    repo = MockStockPriceRepository(
        fintual_price=fintual_price, apple_price=apple_price
    )
    allocations = [
        AllocationEntity(stock=fintual_stock, weight=fintual_weight),
        AllocationEntity(stock=apple_stock, weight=apple_weight),
    ]
    portfolio = Portfolio(
        portfolio=PortfolioEntity(
            description="Portfolio to run tests",
            risk_tolerance=RiskTolerance.high,
            allocations=allocations,
        ),
        stock_price_repo=repo,
    )

    result = portfolio.compute_portfolio_value_at_date(date=date)

    assert result == (fintual_price * fintual_weight / 100) + (
        apple_price * apple_weight / 100
    )
