from enum import Enum, unique


@unique
class Ticker(Enum):
    FNTL = "FNTL"  # Fintual, #Believe
    AAPL = "AAPL"  # Apple Inc. Common Stock


@unique
class RiskTolerance(Enum):
    low = "low"
    moderate = "moderate"
    high = "high"
