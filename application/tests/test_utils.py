from datetime import datetime
from uuid import uuid4

from application.build_portfolio_and_get_profits import get_dates
from application.params import ComputePortfolioProfitsParams

portfolio_id = str(uuid4())
allocations = {"AAPL": 100}


def test_dates_should_return_original_dates_if_start_date_less_than_end_date():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 2, 1)
    params = ComputePortfolioProfitsParams(
        portfolio_id=portfolio_id,
        allocations=allocations,
        start_date=start_date,
        end_date=end_date,
    )

    result_start_date, result_end_date = get_dates(params=params)
    assert result_start_date == start_date
    assert result_end_date == end_date


def test_dates_should_return_swapped_dates_if_start_date_greater_than_end_date():
    start_date = datetime(2025, 2, 1)
    end_date = datetime(2025, 1, 1)
    params = ComputePortfolioProfitsParams(
        portfolio_id=portfolio_id,
        allocations=allocations,
        start_date=start_date,
        end_date=end_date,
    )

    result_start_date, result_end_date = get_dates(params=params)
    assert result_start_date == end_date
    assert result_end_date == start_date


def test_dates_should_work_if_dates_are_equal():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 1, 1)
    params = ComputePortfolioProfitsParams(
        portfolio_id=portfolio_id,
        allocations=allocations,
        start_date=start_date,
        end_date=end_date,
    )

    result_start_date, result_end_date = get_dates(params=params)
    assert result_start_date == start_date
    assert result_end_date == end_date
