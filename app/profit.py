from datetime import datetime

from domain.business_entities import ProfitsPresenter


def compute_profits(
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
        net_profit=profit_percentage, annualized_return=annualized_return
    )
