from pydantic import BaseModel


class ProfitsPresenter(BaseModel):
    portfolio_start_value: float
    portfolio_end_value: float
    net_profits: float
    annualized_return: float

    def __repr__(self):
        return f"Net Profits: {self.net_profits}, Annualized Return: {self.annualized_return}"


class PortfolioResultsPresenter(BaseModel):
    portfolio_id: str
    start_date: str
    end_date: str
    allocations: list
    profits: ProfitsPresenter
