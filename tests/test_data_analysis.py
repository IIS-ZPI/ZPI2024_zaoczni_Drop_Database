from datetime import date
from src.nbp import *
import numpy as np
import os
import pytest



def test_session_analysis_results():
    
    rates: exchange_rates = {
    date(2022, 1, 1): 4.5,
    date(2022, 1, 2): 4.6,
    date(2022, 1, 3): 4.7,
    date(2022, 1, 4): 4.8,
    date(2022, 1, 5): 4.8,
    date(2022, 1, 6): 4.8,
    }
    result = data_analysis.session_analysis(rates)

    assert result.number_of_falling_sessions == 0

    assert result.number_of_rising_sessions == 3
    
    assert result.number_of_unchanged_sessions == 2


    rates: exchange_rates = {
    date(2022, 1, 1): 4.5,
    date(2022, 1, 2): 4.5,
    date(2022, 1, 3): 4.4,
    date(2022, 1, 4): 4.3,
    date(2022, 1, 5): 4.8,
    date(2022, 1, 6): 4.9,
    }
    result = data_analysis.session_analysis(rates)

    assert result.number_of_falling_sessions == 2

    assert result.number_of_rising_sessions == 2
    
    assert result.number_of_unchanged_sessions == 1


    rates: exchange_rates = {
    date(2022, 1, 1): 4.5
    }
    result = data_analysis.session_analysis(rates)

    assert result.number_of_falling_sessions == 0

    assert result.number_of_rising_sessions == 0
    
    assert result.number_of_unchanged_sessions == 0


    rates: exchange_rates = {
    }
    result = data_analysis.session_analysis(rates)

    assert result.number_of_falling_sessions == 0

    assert result.number_of_rising_sessions == 0
    
    assert result.number_of_unchanged_sessions == 0
    


def test_statistical_analysis_results():

    rates: exchange_rates = {
    date(2025, 1, 19): 3.0,
    date(2025, 1, 20): 4.0,
    date(2025, 1, 21): 5.0,
    date(2025, 1, 22): 6.0
    }
    result = data_analysis.statistical_analysis(rates)

    assert result.median == 4.5

    assert result.dominant.mode == 3.0

    assert result.standard_deviation == pytest.approx(1.118033, abs=1e-6)

    assert result.coefficient_of_variation == pytest.approx(0.248451, abs=1e-6)



    rates: exchange_rates = {
    }
    result = data_analysis.statistical_analysis(rates)

    assert np.isnan(result.median)

    assert np.isnan(result.dominant)

    assert np.isnan(result.standard_deviation)

    assert np.isnan(result.coefficient_of_variation)


    rates: exchange_rates = {
        date(2025, 1, 19): 3.0
    }
    result = data_analysis.statistical_analysis(rates)

    assert result.median == 3.0

    assert result.dominant == 3.0

    assert result.standard_deviation == 0

    assert result.coefficient_of_variation == 0
    



def test_distribution_of_change_image():
    
    rates: exchange_rates = {
    date(2025, 1, 19): 3.0,
    date(2025, 1, 20): 4.0,
    date(2025, 1, 21): 5.0,
    date(2025, 1, 22): 6.0
    }
    result = data_analysis.distribution_of_change(rates)
    assert os.path.exists(result[0])


def test_distribution_of_change_results():
    
    rates: exchange_rates = {
    date(2025, 1, 19): 3.0,
    date(2025, 1, 20): 4.0,
    date(2025, 1, 21): 5.0,
    date(2025, 1, 22): 6.0
    }

    expected = {
        0.5: 0.0,
        0.5666666666666667: 0.0,
        0.6333333333333333: 0.0,
        0.7: 0.0,
        0.7666666666666666: 0.0,
        0.8333333333333333: 0.0,
        0.9: 0.0,
        0.9666666666666667: 3.0,
        1.0333333333333332: 0.0,
        1.1: 0.0,
        1.1666666666666665: 0.0,
        1.2333333333333334: 0.0,
        1.3: 0.0,
        1.3666666666666667: 0.0,
        1.4333333333333333: 0.0
    }

    filename, hist = data_analysis.distribution_of_change(rates)
    for key, result in expected.items():
        assert hist[key] == pytest.approx(result, abs=1e-6)


    expected = {
        0.0: 0.0,
        0.06666666666666667: 0.0,
        0.13333333333333333: 0.0,
        0.2: 0.0, 0.26666666666666666: 0.0,
        0.3333333333333333: 0.0,
        0.4: 0.0,
        0.4666666666666667: 0.0,
        0.5333333333333333: 0.0,
        0.6: 0.0,
        0.6666666666666666: 0.0,
        0.7333333333333333: 0.0,
        0.8: 0.0,
        0.8666666666666667: 0.0,
        0.9333333333333333: 0.0}

    rates: exchange_rates = {
    }
    filename, hist = data_analysis.distribution_of_change(rates)
    for key, result in expected.items():
        assert hist[key] == pytest.approx(result, abs=1e-6)



    
