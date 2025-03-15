"""
This script is meant to help you understand this project.
"""

import logging
from datetime import datetime

from application.portfolio import Portfolio
from domain.entities import StockEntity, AllocationEntity, PortfolioEntity
from domain.enums import Ticker, RiskTolerance
from infrastructure.repositories import StockPriceCSVRepository

logging.basicConfig(level=logging.INFO)

apple = StockEntity(
    ticker=Ticker.AAPL,
    official_name="Apple Inc.",
    display_name="Apple",
)

fintual = StockEntity(
    ticker=Ticker.FNTL,
    official_name="Fintual Corporation",
    display_name="Fintual",
)


allocations = [
    AllocationEntity(stock=apple, weight=100),
    AllocationEntity(stock=fintual, weight=0),
]

portfolio = PortfolioEntity(
    description="Tech Growth Portfolio",
    risk_tolerance=RiskTolerance.high,
    allocations=allocations,
)

portfolio = Portfolio(
    portfolio=portfolio,
    stock_price_repo=StockPriceCSVRepository(
        csv_path="infrastructure/stock_prices.csv"
    ),
)

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 3, 1)

# Compute portfolio values and profit
start_value = portfolio.compute_portfolio_value_at_date(start_date)
end_value = portfolio.compute_portfolio_value_at_date(end_date)
profit = portfolio.profit(start_date, end_date)

# Display results
print(
    "==============================================================================================================="
)
print(f"Portfolio Value on {start_date.strftime('%Y-%m-%d')}: ${start_value:.2f}")
print(f"Portfolio Value on {end_date.strftime('%Y-%m-%d')}: ${end_value:.2f}")
print(f"Portfolio Profit: {profit}")
