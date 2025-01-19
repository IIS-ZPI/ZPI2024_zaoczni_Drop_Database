from src.data_analysis import session_analysis, statistical_analysis, distribution_of_change
import pytest

def test_session_analysis():
    try: 
	session_analysis()
    except Exception as e: 
	pytest.fail(f"Funkcja rzuciła wyjątek: {e}")

def test_statistical_analysis():
    try: 
	statistical_analysis()
    except Exception as e: 
	pytest.fail(f"Funkcja rzuciła wyjątek: {e}")

def test_distribution_of_change():
    try: 
	distribution_of_change()
    except Exception as e: 
	pytest.fail(f"Funkcja rzuciła wyjątek: {e}")