from application.params import ComputePortfolioProfitsParams
from application.portfolio import Portfolio
from application.presenters import ProfitsPresenter, PortfolioResultsPresenter
from application.stock import build_stock_entity
from domain.entities import AllocationEntity, PortfolioEntity
from domain.enums import RiskTolerance
from infrastructure.repositories import StockPriceCSVRepository


class BuildPortfolioAndGetProfits:
    @staticmethod
    def call(params: ComputePortfolioProfitsParams) -> ProfitsPresenter:
        start_date = params.start_date
        end_date = params.end_date
        if start_date > end_date:
            # we can fix this for users, no need to get angry
            start_date, end_date = params.end_date, params.start_date

        allocations = params.allocations
        portfolio_allocations = []
        for key, value in allocations.items():
            stock = build_stock_entity(ticker=key)
            portfolio_allocations.append(AllocationEntity(stock=stock, weight=value))

        portfolio = Portfolio(
            portfolio=PortfolioEntity(
                description="Fintual Demo",
                allocations=portfolio_allocations,
                risk_tolerance=RiskTolerance.low,
            ),
            stock_price_repo=StockPriceCSVRepository(
                csv_path="infrastructure/stock_prices.csv"
            ),
        )

        portfolio_profits = portfolio.profit(start_date=start_date, end_date=end_date)

        return PortfolioResultsPresenter(
            portfolio_id=params.portfolio_id,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            allocations=[
                {item.stock.ticker.value: item.weight for item in portfolio_allocations}
            ],
            profits=portfolio_profits,
        )
