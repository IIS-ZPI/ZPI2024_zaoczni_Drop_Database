from datetime import datetime
import math
import os
import typing as t

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from .data_types import *
from .nbp_repository import exchange_rates


class data_analysis(object):

    @staticmethod
    def session_analysis(exchange_rates: exchange_rates) -> session_analysis_result:
        '''Performs session analysis of given exchange rates.

        Result of analysis is a number of raising, falling and unchanged sessions.

        :param: exchange_rates: Exchange rates that session analysis should be 
                performed for.
                Exchange rates should be described for default base currency
                of PLN.

        :returns: session_analysis_result
        :return: Analysis record.
        '''
        if (len(exchange_rates) <= 1):
            return session_analysis_result(
                0,
                0,
                0
            )

        sessions = [
            v for _, v
            in sorted(exchange_rates.items(), key=lambda e: e[0])
        ]

        changes = np.diff(sessions)

        return session_analysis_result(
            # casting necessary, as numpy typings do not know dimensions of output
            t.cast(int, np.sum(changes > 0)),
            t.cast(int, np.sum(changes < 0)),
            t.cast(int, np.sum(changes == 0)),
        )

    @staticmethod
    def statistical_analysis(exchange_rates: exchange_rates) -> statistical_analysis_result:
        '''Performs statistical analysis of given exchange rates.

        Result of analysis are basic statistical aggregations:

        * median,
        * dominant,
        * standard_deviation,
        * coefficient_of_variation.

        :param exchange_rates: Exchange rates that session analysis should be
               performed for.
               Exchange rates should be described for default base currency
               of PLN.

        :returns: statistical_analysis_result
        :return: Analysis record.
        '''
        if (len(exchange_rates) == 0):
            return statistical_analysis_result(
                float('nan'),
                float('nan'),
                float('nan'),
                float('nan'),
            )

        rates = [
            v 
            for _, v
            in exchange_rates.items()
        ]

        if (len(exchange_rates) == 1):
            return statistical_analysis_result(
                rates[0],
                rates[0],
                0,
                0,
            )

        return statistical_analysis_result(
            # casting necessary, as numpy typings do not know dimensions of output
            t.cast(float, np.median(rates)),
            t.cast(float, stats.mode(rates)),
            t.cast(float, np.std(rates)),
            t.cast(float, np.std(rates) / np.mean(rates)),
        )

    @staticmethod
    def distribution_of_change(
        relative_exchange_rates: exchange_rates,
        *,
        bar_count: int = 15,
        output_location: str = "./hist_out",
        img_size_px: tuple[int, int] = (420, 400),
    ) -> tuple[str, dict[float, float]]:
        '''Creates histogram with distribution of changes of given exchange rates.

        Result is image with plotted data, as well as histogram dict.

        Output location, number of bars, as well as size of resulting image
        can be customized.

        :param relative_exchange_rates: Exchange rates that session analysis 
               should be performed for.
               Exchange rates should be described for default base currency
               of PLN.

        :returns: str
        :return: URL to created image with created figure.
        '''
        os.makedirs(output_location, exist_ok=True)

        rates = [
            v
            for _, v
            in relative_exchange_rates.items()
        ]

        changes = np.diff(rates)

        # Very primitive pixel => inch conversion
        plt.figure(figsize=(img_size_px[0] / 100, img_size_px[1] / 100))
        counts, bins, _ = plt.hist(changes, bins=bar_count)
        plt.xlabel("Zmiana względem sesji poprzedniej")
        plt.ylabel("Liczba sesji")
        plt.title("Rozkład zmian sesji")

        current_datetime = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        filename = f"hist_{current_datetime}.png"
        filepath = os.path.join(output_location, filename)
        plt.savefig(filepath)
        plt.close()

        hist = {
            float(bins[i]): float(counts[i]) 
            for i
            in range(len(counts))
        }

        return filepath, hist
