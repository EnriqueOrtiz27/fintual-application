from pydantic import BaseModel

from domain.enums import (
    TickerSymbolCode,
    RiskToleranceLevel,
)


class StockEntity(BaseModel):
    symbol: TickerSymbolCode
    official_name: str
    display_name: str


class AllocationEntity(BaseModel):
    stock: StockEntity
    weight: float


class PortfolioEntity(BaseModel):
    description: str
    risk_tolerance: RiskToleranceLevel
    allocations: list[AllocationEntity]


class ProfitsPresenter(BaseModel):
    net_profit: float
    annualized_return: float

    def __repr__(self):
        return f"Net Profit: {self.net_profit}, Annualized Return: {self.annualized_return}"
