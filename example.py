"""
This script is meant to help you understand this project.
"""

import logging
from datetime import datetime

from app.portfolio import Portfolio
from domain.business_entities import StockModel, AllocationModel, PortfolioModel
from domain.enums import TickerSymbolCode, StockExchangeCode, RiskToleranceLevel

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create sample stocks
apple = StockModel(
    symbol=TickerSymbolCode.AAPL,
    exchange=StockExchangeCode.Nasdaq,
    official_name="Apple Inc.",
    display_name="Apple",
)

nvidia = StockModel(
    symbol=TickerSymbolCode.NVDA,
    exchange=StockExchangeCode.Nasdaq,
    official_name="NVIDIA Corporation",
    display_name="NVIDIA",
)

amazon = StockModel(
    symbol=TickerSymbolCode.AMZN,
    exchange=StockExchangeCode.Nasdaq,
    official_name="Amazon.com, Inc.",
    display_name="Amazon",
)

# Define allocations (must sum to 100%)
allocations = [
    AllocationModel(stock=apple, percentage_allocation=50),
    AllocationModel(stock=nvidia, percentage_allocation=30),
    AllocationModel(stock=amazon, percentage_allocation=20),
]

# Create portfolio
portfolio_model = PortfolioModel(
    description="Tech Growth Portfolio",
    risk_tolerance=RiskToleranceLevel.high,
    expense_ratio_pct=0.2,
    stock_allocations=allocations,
)

# Initialize portfolio
portfolio = Portfolio(portfolio_model)

# Define dates
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 1)

# Compute portfolio values and profit
start_value = portfolio.compute_portfolio_value_at_date(start_date)
end_value = portfolio.compute_portfolio_value_at_date(end_date, randomize=True)
profit = portfolio.profit(start_date, end_date)

# Display results
print(
    "==============================================================================================================="
)
print(f"Portfolio Value on {start_date.strftime('%Y-%m-%d')}: ${start_value:.2f}")
print(f"Portfolio Value on {end_date.strftime('%Y-%m-%d')}: ${end_value:.2f}")
print(f"Portfolio Profit: {profit}")
