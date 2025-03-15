import logging
from datetime import datetime

from application.presenters import ProfitsPresenter
from application.stock import Stock
from domain.entities import PortfolioEntity
from domain.repositories import StockPriceAbstractRepository

logger = logging.getLogger(__name__)


def format_profits(
    start_value: float, end_value: float, start_date: datetime, end_date: datetime
) -> ProfitsPresenter:
    """
    Compute profit and annualized return given two portfolio values.
    :param start_value: Portfolio value at start date
    :param end_value: Portfolio value at end date
    :param start_date: Start date of investment
    :param end_date: End date of investment
    :return: Profits object containing net profit and annualized return
    """
    profit_percentage = ((end_value - start_value) / start_value) * 100

    # Compute annualized return
    days_held = (end_date - start_date).days
    years_held = days_held / 365.0  # Convert days to years

    if years_held > 0:
        annualized_return = ((end_value / start_value) ** (1 / years_held)) - 1
        annualized_return *= 100  # Convert to percentage
    else:
        annualized_return = 0  # Avoid division errors for same-day calculations

    return ProfitsPresenter(
        net_profit=profit_percentage, annualized_return_pct=annualized_return
    )


class Portfolio:
    def __init__(
        self, portfolio: PortfolioEntity, stock_price_repo: StockPriceAbstractRepository
    ):
        self.description = portfolio.description
        self.risk_tolerance = portfolio.risk_tolerance
        self.allocations = [
            (
                Stock(stock=allocation.stock, stock_price_repo=stock_price_repo),
                allocation.weight,
            )
            for allocation in portfolio.allocations
        ]

    def compute_portfolio_value_at_date(
        self,
        date: datetime,
    ) -> float:
        """
        Get the total value of a portfolio on a given date.
        """
        total_value = 0.0
        logger.info(f"Calculating portfolio value on {date.strftime('%Y-%m-%d')}")

        for stock, allocation in self.allocations:
            stock_price = stock.price(date=date)
            stock_value = (allocation / 100) * stock_price
            total_value += stock_value
            logger.info(
                f"{stock.ticker}: Price={stock_price}, Allocation={allocation}%, Contribution={stock_value}\n"
            )

        logger.info(f"Portfolio value on {date.strftime('%Y-%m-%d')}: {total_value}")
        return total_value

    @staticmethod
    def get_annualized_return(
        start_date: datetime,
        end_date: datetime,
        start_value: float,
        end_value: float,
    ):
        days_held = (end_date - start_date).days
        if days_held == 0:
            return 0

        total_return = (end_value - start_value) / start_value
        years_held = days_held / 365
        annualized_return = (1 + total_return) ** (1 / years_held) - 1
        annualized_return *= 100  # Convert to percentage

        return round(annualized_return, 2)

    def profit(self, start_date: datetime, end_date: datetime) -> ProfitsPresenter:
        if start_date > end_date:
            # we can fix this for users, no need to get angry
            start_date, end_date = end_date, start_date

        start_value = self.compute_portfolio_value_at_date(date=start_date)
        end_value = self.compute_portfolio_value_at_date(date=end_date)
        net_profits = round(end_value - start_value, 2)
        annualized_return = self.get_annualized_return(
            start_date=start_date,
            end_date=end_date,
            start_value=start_value,
            end_value=end_value,
        )
        return ProfitsPresenter(
            net_profits=net_profits,
            annualized_return_pct=annualized_return,
            portfolio_start_value=round(start_value, 2),
            portfolio_end_value=round(end_value, 2),
        )
