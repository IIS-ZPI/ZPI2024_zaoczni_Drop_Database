from datetime import date
from src.nbp import *
import pytest



def test_session_analysis():
    try:
        rates = [4.5, 4.6, 4.7]
        data_analysis.session_analysis(rates)
    except Exception as e:
        pytest.fail(f"Rzucono wyjatek: {e}")


def test_statistical_analysis():
    try:
        rates: exchange_rates = {
        date(2025, 1, 19): 3.0,
        date(2025, 1, 20): 4.0,
        date(2025, 1, 21): 5.0,
        date(2025, 1, 22): 6.0
    }
        data_analysis.statistical_analysis(rates)
    except Exception as e:
        pytest.fail(f"Rzucono wyjatek: {e}")


def test_distribution_of_change():
    try:
        rates: exchange_rates = {
        date(2025, 1, 19): 3.0,
        date(2025, 1, 20): 4.0,
        date(2025, 1, 21): 5.0,
        date(2025, 1, 22): 6.0
    }
        data_analysis.distribution_of_change(rates)
    except Exception as e:
        pytest.fail(f"Rzucono wyjatek: {e}")
