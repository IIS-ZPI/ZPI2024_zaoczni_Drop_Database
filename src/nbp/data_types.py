from dataclasses import dataclass
from datetime import date
import typing as t

exchange_rates = t.Dict[date, float]

currency_code = t.Literal["USD", "EUR", "GBP", "NOK"]

@dataclass
class session_analysis_result:
	number_of_rising_sessions: int
	number_of_falling_sessions: int
	number_of_unchanged_sessions: int

@dataclass
class statistical_analysis_result:
	median: float
	dominant: float
	standard_deviation: float
	coefficient_of_variation: float
