from nbp_repository import exchange_rates

from data_types import *

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
		raise RuntimeError("Not implemented")

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
		raise RuntimeError("Not implemented")
		
	@staticmethod
	def distribution_of_change(relative_exchange_rates: exchange_rates) -> str:
		'''Creates histogram with distribution of changes of given exchange rates.

		Result is image with plotted data.

		:param relative_exchange_rates: Exchange rates that session analysis 
		       should be performed for.
		       Exchange rates should be described for default base currency
		       of PLN.
		
		:returns: str
		:return: URL to created image with created figure.
		'''
		raise RuntimeError("Not implemented")
