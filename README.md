# ZPI2024_zaoczni_Drop_Database

## Project Description

The ZPI2024_zaoczni_Drop_Database project is a currency data analysis application that allows users to view and analyze exchange rates. The application uses the National Bank of Poland (NBP) API to fetch exchange rate data.

## Project Structure

```
.github/
	workflows/
		test_module_1.yml
.gitignore
.vscode/
	settings.json
pytest.ini
README.md
requirements.txt
src/
	__init__.py
	nbp/
		__init__.py
		__pycache__/
		data_analysis.py
		data_types.py
		nbp_repository.py
	UI/
		__pycache__/
		AnalysisScreen.py
		AnalysisScreen.ui
		AnalysisSelection.py
		AnalysisSelection.ui
		Control.py
		MainScreen.py
		MainScreen.ui
		WindowCS.py
		WindowCS.ui
		WindowDC.py
		WindowDC.ui
		WindowSM.py
		WindowSM.ui
tests/
	__init__.py
	test_data_analysis.py
	test_nbp_repository.py
```

## Key Files and Functions

### 

nbp_repository.py



The nbp_repository.py file contains functions for fetching exchange rates from the NBP API. Example function:

```python
def get_exchange_rates(start_date: date, end_date: date, currency: str, base_currency: str = None) -> dict:
    # This function fetches exchange rates for the given date range
    # and returns them as a dictionary.
```

### UI

The `UI` folder contains user interface files, including `.ui` files and their corresponding `.py` files.

### Tests

The tests folder contains unit tests for the application. 


## Requirements

To run the project, you need to install the required libraries listed in the 

requirements.txt

 file:

```sh
pip install -r requirements.txt
```

## Running Tests

To run the unit tests, use the following command:

```sh
pytest
```

## Authors

The project was created by the ZPI2024_zaoczni_Drop_Database team.