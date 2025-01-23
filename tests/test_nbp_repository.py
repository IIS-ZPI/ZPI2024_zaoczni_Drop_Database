import pytest
from datetime import date, timedelta
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
    exp = {'2025-01-02': 4.1219}
    assert result == exp

    result = nbp_repository.get_exchange_rates(date(2025, 1, 1), date(2025, 1, 10), "USD")
    exp = {'2025-01-02': 4.1219,
           '2025-01-03': 4.1512,
           '2025-01-07': 4.077,
           '2025-01-08': 4.1335,
           '2025-01-09': 4.1523,
           '2025-01-10': 4.1415}
    
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