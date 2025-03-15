from pydantic import BaseModel

from domain.enums import (
    Ticker,
    RiskTolerance,
)


class StockEntity(BaseModel):
    ticker: Ticker
    official_name: str
    display_name: str


class AllocationEntity(BaseModel):
    stock: StockEntity
    weight: float


class PortfolioEntity(BaseModel):
    description: str
    risk_tolerance: RiskTolerance
    allocations: list[AllocationEntity]
