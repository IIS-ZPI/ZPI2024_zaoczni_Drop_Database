import pytest
from datetime import date, timedelta, datetime
from src.nbp import *


def test_get_exchange_rates_bad_arguments():
    today = date.today()
    days = timedelta(days=5)
    today2 = today + days
    result = nbp_repository.get_exchange_rates(today2, date(2025, 1, 1), "USD")  
    assert result == "Start date must be before today"

    result = nbp_repository.get_exchange_rates(today, date(2025, 1, 1), "USD")  
    assert result == "Start date must be before end date"

    result = nbp_repository.get_exchange_rates(date(2001, 1, 1), date(2025, 1, 1), "USD")  
    assert result == "Start date must be after 2002-01-01"

    result = nbp_repository.get_exchange_rates(date(2025, 1, 1), date(2025, 1, 1), "USD")  
    assert result == "Start date must be before end date"

    result = nbp_repository.get_exchange_rates(date(2025, 1, 1), date(2025, 1, 10), "XYZ")
    assert result == "Currency data not found"



def test_get_exchange_rates_results():
    result = nbp_repository.get_exchange_rates(date(2025, 1, 1), date(2025, 1, 2), "USD")
    exp = {date(2025, 1, 2): 4.1219}
    print(f"res2 {result}  as  {exp}")
    assert result == exp

    result = nbp_repository.get_exchange_rates(date(2025, 1, 1), date(2025, 1, 10), "USD")
    exp = {date(2025, 1, 2): 4.1219,
           date(2025, 1, 3): 4.1512,
           date(2025, 1, 7): 4.077,
           date(2025, 1, 8): 4.1335,
           date(2025, 1, 9): 4.1523,
           date(2025, 1, 10): 4.1415}
    
    assert result == exp

    result = nbp_repository.get_exchange_rates(date(2024, 12, 1), date(2025, 1, 21), "USD")
    exp = 33
    assert exp == len(result)

    result = nbp_repository.get_exchange_rates(date(2024, 1, 1), date(2024, 12, 31), "USD")
    exp = 252
    assert exp == len(result)


    T1 = datetime.now()
    result = nbp_repository.get_exchange_rates(date(2002, 1, 1), date(2025, 1, 20), "USD")
    T2 = datetime.now()
    TimeFunc = T2 - T1
    assert TimeFunc < timedelta(seconds=15)


def test_get_exchange_rates_currency():
    rates = nbp_repository.get_exchange_rates(
        date(2024, 4, 4),
        date(2024, 4, 20),
        "NOK",
    )

    assert isinstance(rates, dict)
    
    expected_rates = {
        date(2024, 4, 4): 0.3699,
        date(2024, 4, 5): 0.3691,
        date(2024, 4, 8): 0.3691,
        date(2024, 4, 9): 0.3684,
        date(2024, 4, 10): 0.3683,
        date(2024, 4, 11): 0.3676,
        date(2024, 4, 12): 0.3683,
        date(2024, 4, 15): 0.3683,
        date(2024, 4, 16): 0.3702,
        date(2024, 4, 17): 0.3715,
        date(2024, 4, 18): 0.3685,
        date(2024, 4, 19): 0.3680,
    }

    eps = 1**-4

    for data in expected_rates.keys():
        assert rates[data] - expected_rates[data] < eps


def test_get_exchange_rates_with_base():

    rates = nbp_repository.get_exchange_rates(
        date(2023, 12, 1),
        date(2023, 12, 14),
        "USD",
        "EUR",
    )

    assert isinstance(rates, dict)

    expected_rates = {
        date(2023, 12, 1): 0.9175978295,
        date(2023, 12, 4): 0.9195375775,
        date(2023, 12, 5): 0.9231374181,
        date(2023, 12, 6): 0.9266977087,
        date(2023, 12, 7): 0.9276549591,
        date(2023, 12, 8): 0.9279033785,
        date(2023, 12, 11): 0.9287690817,
        date(2023, 12, 12): 0.9264448336,
        date(2023, 12, 13): 0.9270359509,
        date(2023, 12, 14): 0.9171021763,
    }

    eps = 1**-9

    for data in expected_rates.keys():
        assert rates[data] - expected_rates[data] < eps