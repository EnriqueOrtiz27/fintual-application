from enum import Enum, unique


@unique
class TickerSymbolCode(Enum):
    # NYSE
    ABNB = "ABNB"  # AIRBNB INC
    ACGL = "ACGL"  # ARCH CAPITAL GROUP
    ADBE = "ADBE"  # ADOBE INC

    # Nasdaq
    AAPL = "AAPL"  # Apple Inc. Common Stock
    NVDA = "NVDA"  # NVIDIA Corporation Common Stock
    AMZN = "AMZN"  # Amazon.com, Inc. Common Stock


@unique
class StockExchangeCode(Enum):
    NYSE = "NYSE"
    Nasdaq = "Nasdaq"


@unique
class RiskToleranceLevel(Enum):
    low = "low"
    moderate = "moderate"
    high = "high"
