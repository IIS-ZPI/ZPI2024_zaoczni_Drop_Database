import typing as t
from datetime import date

from data_types import *


class nbp_repository(object):

	@t.overload
	@staticmethod
	def get_exchange_rates(
		start_date: date,
		end_date: date,
		currency: currency_code,
	) -> exchange_rates | str:
		'''Retrieves from NBP API currency exchanges for given currency.

		As exchange rates are only kept for working days, exact range will be
		usually smaller that requested.

		:param start_date: Start date of exchange rates.
		       
			   Must be 2002-01-02 or later (not after ``end_date``).

		:param end_date: End date of exchange rates.
		       Must be before today (not before ``start_date``).

		:param currency: Code of retrieved currency.
		       Allowed values are:

			   - USD,
			   - EUR,
			   - GBP,
			   - NOK.

		:returns: t.Dict[date, float] | str
		:return: Exchange rates, in format of dictionary { date: float },
		         containing rates for days between specified dates, or string
				 with error message.
		'''
		pass


	@t.overload
	@staticmethod
	def get_exchange_rates(
		start_date: date,
		end_date: date,
		currency: currency_code,
		base_currency: currency_code,
	) -> exchange_rates | str:
		'''Retrieves from NBP API currency exchanges for given currency.

		As exchange rates are only kept for working days, exact range will be
		usually smaller that requested.

		:param start_date: Start date of exchange rates.
		       
			   Must be 2002-01-02 or later (not after ``end_date``).

		:param end_date: End date of exchange rates.
		       Must be before today (not before ``start_date``).

		:param currency: Code of retrieved currency.
		       Allowed values are:

			   - USD,
			   - EUR,
			   - GBP,
			   - NOK.

		:param base_currency: Code of base currency.
		       Must not be same as ``currency``.

		:returns: t.Dict[date, float] | str
		:return: Exchange rates, in format of dictionary { date: float },
		         containing rates for days between specified dates, or string
				 with error message.
		'''
		pass

	@staticmethod
	def get_exchange_rates(
		start_date: date,
		end_date: date,
		currency: currency_code,
		base_currency: t.Optional[currency_code] = None,
	) -> exchange_rates | str:	
		raise RuntimeError("Not implemented")

# Example usage
# nbp_repository.get_exchange_rates(date(2024, 1, 1), date(2025, 1, 1), "USD")

