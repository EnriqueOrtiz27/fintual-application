from fastapi import FastAPI, Response, status
from pydantic import ValidationError

from application.build_portfolio_and_get_profits import BuildPortfolioAndGetProfits
from application.params import ComputePortfolioProfitsParams

app = FastAPI()


def handle_validation_error(exception: ValidationError):
    # Format the error into a simpler, user-friendly output
    error_messages = []

    for error in exception.errors():
        loc = ".".join(
            str(x) for x in error["loc"]
        )  # Get the location of the error (e.g., field name)
        msg = error["msg"]  # The error message
        error_messages.append(f"Field '{loc}': {msg}")

    # You can log these errors for internal use or display them as needed
    return "\n".join(error_messages)


@app.post("/portfolios/{portfolio_id}/profits")
def compute_portfolio_profits(portfolio_id: str, params: dict, response: Response):
    try:
        params = ComputePortfolioProfitsParams(**params, portfolio_id=portfolio_id)
    except ValidationError as e:
        message = handle_validation_error(e)
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "code": "bad_request",
            "message": f"{message}.",
        }

    return BuildPortfolioAndGetProfits.call(params=params)
