"""
This script is meant to help you understand this project.
"""

import logging
from datetime import datetime

from app.portfolio import Portfolio
from domain.business_entities import StockEntity, AllocationEntity, PortfolioEntity
from domain.enums import TickerSymbolCode, RiskToleranceLevel

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create sample stocks
apple = StockEntity(
    symbol=TickerSymbolCode.AAPL,
    official_name="Apple Inc.",
    display_name="Apple",
)

fintual = StockEntity(
    symbol=TickerSymbolCode.FNTL,
    official_name="Fintual Corporation",
    display_name="Fintual",
)


# Define allocations (must sum to 100%)
allocations = [
    AllocationEntity(stock=apple, weight=50),
    AllocationEntity(stock=fintual, weight=50),
]

# Create portfolio
portfolio_model = PortfolioEntity(
    description="Tech Growth Portfolio",
    risk_tolerance=RiskToleranceLevel.high,
    allocations=allocations,
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
