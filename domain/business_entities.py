from pydantic import BaseModel

from domain.enums import (
    TickerSymbolCode,
    StockExchangeCode,
    RiskToleranceLevel,
)


class StockModel(BaseModel):
    symbol: TickerSymbolCode
    exchange: StockExchangeCode
    official_name: str
    display_name: str


class AllocationModel(BaseModel):
    stock: StockModel
    percentage_allocation: float


class PortfolioModel(BaseModel):
    description: str
    risk_tolerance: RiskToleranceLevel
    expense_ratio_pct: float
    stock_allocations: list[AllocationModel]


class Profits(BaseModel):
    net_profit: float
    annualized_return: float

    def __repr__(self):
        return f"Net Profit: {self.net_profit}, Annualized Return: {self.annualized_return}"
