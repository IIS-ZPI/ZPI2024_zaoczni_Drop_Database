import pytest
from datetime import date, timedelta
from nbp_repository import nbp_repository


def test_get_exchange_rates():
    today = date.today()
    days = timedelta(days=5)
    today2 = today + days
    result = nbp_repository.get_exchange_rates(today2, date(2025, 1, 1), "USD")  
    assert result == "Start date must be before today"

    result = nbp_repository.get_exchange_rates(today, date(2025, 1, 1), "USD")  
    assert result == "Start date must be before end date"

    result = nbp_repository.get_exchange_rates(date(2001, 1, 1), date(2025, 1, 1), "USD")  
    assert result == "Start date must be after 2002-01-01"
