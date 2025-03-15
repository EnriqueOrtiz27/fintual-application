from enum import Enum, unique


@unique
class TickerSymbolCode(Enum):
    # NYSE
    FNTL = "FNTL"  # Fintual, #Believe

    # Nasdaq
    AAPL = "AAPL"  # Apple Inc. Common Stock


@unique
class RiskToleranceLevel(Enum):
    low = "low"
    moderate = "moderate"
    high = "high"
