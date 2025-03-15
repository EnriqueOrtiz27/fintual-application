from datetime import datetime

import pandas as pd

from domain.repositories import StockPriceAbstractRepository


class StockPriceCSVRepository(StockPriceAbstractRepository):
    def __init__(self, csv_path: str):
        """
        Initialize the repository with a CSV file.
        Assumes the CSV format:

        date        AAPL   FNTL
        2025-03-01  190.5  72.3
        2025-03-02  192.1  74.8
        ...

        - Date column **must be in YYYY-MM-DD format**.
        - Stock tickers (AAPL, FNTL) should be column names.
        """
        self.data = pd.read_csv(csv_path, parse_dates=["date"])

        # Ensure date format is YYYY-MM-DD and set as index
        self.data["date"] = self.data["date"].dt.strftime("%Y-%m-%d")
        self.data.set_index("date", inplace=True)

    def price(self, date: datetime, ticker: str) -> float:
        date_str = date.strftime("%Y-%m-%d")  # Convert date to YYYY-MM-DD

        if date_str not in self.data.index:
            raise ValueError(f"No price data available for {date_str}")

        if ticker not in self.data.columns:
            raise ValueError(
                f"Ticker '{ticker}' not found in data. Available: {list(self.data.columns)}"
            )

        return float(self.data.loc[date_str, ticker])
