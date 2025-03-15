from datetime import datetime

from pydantic import AfterValidator, BaseModel
from typing_extensions import Annotated

from domain.enums import Ticker


def allocation_validator(allocations: dict) -> dict:
    if not allocations:
        raise ValueError("Cannot set an empty portfolio")

    weight_sum = sum(allocations.values())
    if weight_sum != 100:
        raise ValueError("Portfolio weights must add to 100")

    return allocations


def date_validator(date: datetime) -> datetime:
    try:
        if datetime(2025, 1, 1) <= date <= datetime(2025, 12, 31):
            return date
    except Exception as e:
        print(f"Error comparing dates: {e}")
        raise ValueError("Dates must be between 2025-03-01, and 2025-12-31, inclusive")

    raise ValueError("Dates must be between 2025-03-01, and 2025-12-31, inclusive")


class ComputePortfolioProfitsParams(BaseModel):
    portfolio_id: str
    start_date: Annotated[datetime, AfterValidator(date_validator)]
    end_date: Annotated[datetime, AfterValidator(date_validator)]
    allocations: Annotated[dict[Ticker, int], AfterValidator(allocation_validator)]
