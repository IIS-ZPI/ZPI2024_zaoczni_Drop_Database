import typing as t
from datetime import date, timedelta
import requests
from .data_types import currency_code, exchange_rates

rate = t.TypedDict(
    "rate",
    {
        "currency": str,
        "code": currency_code,
        "mid": float,
    }
)

table_day = t.TypedDict(
    "table_day",
    {
        "table": t.Literal["A"],
        "no": str,
        "effectiveDate": str,
        "rates": list[rate],
    }
)


class nbp_repository(object):
    nbp_api_url = "https://api.nbp.pl/api/exchangerates/tables/A/{startDate}/{endDate}/?format=json"

    @t.overload
    @staticmethod
    def get_exchange_rates(
        start_date: date,
        end_date: date,
        currency: currency_code,
    ) -> exchange_rates | str:
        """Retrieves from NBP API currency exchanges for given currency.

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
        """
        pass

    @t.overload
    @staticmethod
    def get_exchange_rates(
        start_date: date,
        end_date: date,
        currency: currency_code,
        base_currency: currency_code,
    ) -> exchange_rates | str:
        """Retrieves from NBP API currency exchanges for given currency.

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
        """
        pass

    @staticmethod
    def get_exchange_rates(
        start_date: date,
        end_date: date,
        currency: currency_code,
        base_currency: t.Optional[currency_code] = None,
    ) -> exchange_rates | str:
        today = date.today()
        if start_date > today:
            return "Start date must be before today"
        if start_date > end_date:
            return "Start date must be before end date"
        if start_date < date(2002, 1, 2):
            return "Start date must be after 2002-01-01"
        if end_date > today:
            return "End date must be before today"
        if end_date < start_date:
            return "End date must be after start date"
        if base_currency is not None and base_currency == currency:
            return "Base currency must be different than currency"
        
        rates: exchange_rates
        
        if currency not in ["USD", "EUR", "GBP", "NOK"] or (
            base_currency is not None and base_currency not in ["USD", "EUR", "GBP", "NOK"]
        ):
            return "Currency not supported"

        # if time between dates is greated than 93 days, split dates into smaller 93 days ranges
        if (end_date - start_date).days > 93:
            rates = {}
            current_date = start_date
            while current_date < end_date:
                next_date = current_date + timedelta(days=93)
                if next_date > end_date:
                    next_date = end_date
                more_rates = nbp_repository.get_exchange_rates(
                    current_date, next_date, currency, base_currency
                )
                if isinstance(more_rates, str):
                    return more_rates
                else:
                    rates.update(
                        nbp_repository.get_exchange_rates(
                            current_date, next_date, currency, base_currency
                        )
                    )
                    current_date = next_date
            return rates

        response = requests.get(
            nbp_repository.nbp_api_url.format(
                startDate=start_date, endDate=end_date
            )
        )
        if response.status_code != 200:
            return "Error while fetching data from NBP API"

        # extract currencies data from response with dates

        data: list[table_day] = response.json()
        if base_currency is None:
            rates = {}
            for entry in data:
                edate = date.fromisoformat(entry["effectiveDate"])
                for rate in entry["rates"]:
                    if rate["code"] == currency:
                        rates[edate] = rate["mid"]
            return rates
        else:
            rates = {}
            for entry in data:
                edate = date.fromisoformat(entry["effectiveDate"])
                value: float
                base: float
                for rate in entry["rates"]:
                    if rate["code"] == currency:
                        value = rate["mid"]
                    if rate["code"] == base_currency:
                        base = rate["mid"]
                rates[edate] = value / base
            return rates
