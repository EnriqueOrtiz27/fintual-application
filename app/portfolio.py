import logging
from datetime import datetime

from app.profit import compute_profits
from app.stock import Stock
from domain.business_entities import PortfolioModel, Profits

logger = logging.getLogger(__name__)


class Portfolio:
    def __init__(self, portfolio: PortfolioModel):
        self.description = portfolio.description
        self.risk_tolerance = portfolio.risk_tolerance
        self.expense_ratio_pct = portfolio.expense_ratio_pct
        self.stock_allocations = [
            (Stock(allocation.stock), allocation.percentage_allocation)
            for allocation in portfolio.stock_allocations
        ]

    def compute_portfolio_value_at_date(
        self, date: datetime, randomize: bool = False
    ) -> float:
        """
        Get the total value of a portfolio on a given date.

        :param date: date on which to get the total portfolio value
        :param randomize: true if you want a different answer every day
        :return: portfolio market value
        """
        total_value = 0.0
        logger.info(f"Calculating portfolio value on {date.strftime('%Y-%m-%d')}")

        for stock, allocation in self.stock_allocations:
            stock_price = stock.price(date=date, randomize=randomize)
            stock_value = (allocation / 100) * stock_price
            total_value += stock_value
            logger.info(
                f"{stock.symbol}: Price={stock_price}, Allocation={allocation}%, Contribution={stock_value}\n"
            )

        logger.info(f"Portfolio value on {date.strftime('%Y-%m-%d')}: {total_value}")
        return total_value

    def profit(self, start_date: datetime, end_date: datetime) -> Profits:
        """
        Calculate the profit of the portfolio from start_date to end_date.
        """
        start_value = self.compute_portfolio_value_at_date(date=start_date)
        end_value = self.compute_portfolio_value_at_date(date=end_date, randomize=True)

        profit_percentage = ((end_value - start_value) / start_value) * 100
        logger.info(
            f"Portfolio Profit from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}: {profit_percentage:.2f}%"
        )

        return compute_profits(
            start_value=start_value,
            end_value=end_value,
            start_date=start_date,
            end_date=end_date,
        )
