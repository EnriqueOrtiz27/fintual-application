from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from application.build_portfolio_and_get_profits import BuildPortfolioAndGetProfits
from application.params import ComputePortfolioProfitsParams
from infrastructure.middleware import (
    catch_exceptions_middleware,
    validation_exception_handler,
)

app = FastAPI()
app.middleware("http")(catch_exceptions_middleware)
app.add_exception_handler(ValidationError, validation_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.post("/portfolios/{portfolio_id}/profits")
def compute_portfolio_profits(
    portfolio_id: str,
    params: ComputePortfolioProfitsParams,
):
    return BuildPortfolioAndGetProfits.call(params=params, portfolio_id=portfolio_id)
