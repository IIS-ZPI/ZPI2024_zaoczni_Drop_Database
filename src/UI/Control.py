import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QMessageBox, QLabel, QPushButton, QInputDialog, QFileDialog
)
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from nbp.data_analysis import data_analysis
from nbp.nbp_repository import nbp_repository
from MainScreen import Ui_MainWindow as MainScreen
from AnalysisSelection import Ui_MainWindow as AnalysisSelection
from WindowCS import Ui_MainWindow as WindowCS
from WindowSM import Ui_MainWindow as WindowSM
from WindowDC import Ui_MainWindow as WindowDC
from AnalysisScreen import Ui_MainWindow as AnalysisScreen


class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Analysis App")
        self.setGeometry(100, 100, 1024, 768)

        # Containers for data
        self.selected_dates = {'start': None, 'end': None}
        self.selected_currency = None  # Stores the selected currency
        self.analysis_type = None  # Stores the selected analysis type

        # Stacked widget to hold all screens
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Initialize screens
        self.main_screen = self.setup_main_screen()
        self.analysis_selection = self.setup_analysis_selection()
        self.window_cs = self.setup_window_cs()
        self.window_sm = self.setup_window_sm()
        self.window_dc = self.setup_window_dc()
        self.analysis_screen = self.setup_analysis_screen()

        # Add all screens to the stack
        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.analysis_selection)
        self.stack.addWidget(self.window_cs)
        self.stack.addWidget(self.window_sm)
        self.stack.addWidget(self.window_dc)
        self.stack.addWidget(self.analysis_screen)

        
        self.show()
    def reset_data(self):
        """Reset selected data to default values."""
        self.selected_dates = {'start': None, 'end': datetime.today().date()}
        self.selected_currency = None
        self.analysis_type = None
        
    def toggle_currency_selection(self, state, currency):
        """Add or remove currency from the selected_currency list based on checkbox state."""
        if self.selected_currency is None:
            self.selected_currency = []
        if state:
            if currency not in self.selected_currency:
                self.selected_currency.append(currency)
        else:
            if currency in self.selected_currency:
                self.selected_currency.remove(currency)    
                
    def validate_and_analyze(self, analysis_type):
        """Set the analysis type and navigate to the appropriate screen."""
        self.analysis_type = analysis_type
        if analysis_type == 'CS':
            self.stack.setCurrentWidget(self.window_cs)
        elif analysis_type == 'SM':
            self.stack.setCurrentWidget(self.window_sm)
        elif analysis_type == 'DC':
            self.stack.setCurrentWidget(self.window_dc)

    def process_analysis(self):
        """Perform the analysis after validating all inputs."""
        if not self.selected_dates['start'] and not self.selected_dates['end']:
            QMessageBox.warning(self, "Input Error", "Please select a valid date range.")
            return
        if not self.selected_dates['start']:
            QMessageBox.warning(self, "Input Error", "Please select a valid date range - start date.")
            return
        if not self.selected_dates['end']:
            QMessageBox.warning(self, "Input Error", "Please select a valid date range - end date.")
            return
        if not self.selected_currency:
            QMessageBox.warning(self, "Input Error", "Please select a currency.")
            return
        if self.selected_dates['start'] >= self.selected_dates['end']:
            QMessageBox.warning(self, "Input Error", "Start date must be before end date.")
            return
        if self.selected_dates['start']< QDate(2002, 1, 1) or self.selected_dates['end'] < QDate(2002, 1, 1):
            QMessageBox.warning(self, "Input Error", "Dates cannot be earlier than 2002-01-01.")
            return
        if self.analysis_type == 'DC':
            if not isinstance(self.selected_currency, list) or len(self.selected_currency) != 2:
                QMessageBox.warning(self, "Input Error", "Please select exactly two currencies for Distribution of Change analysis." + str(self.selected_currency))
                return

        try:
            # Call the corresponding analysis method based on type
            self._perform_selected_analysis()
            self.stack.setCurrentWidget(self.analysis_screen)
        except Exception as e:
            QMessageBox.critical(self, "Analysis Error", f"An error occurred during analysis: {str(e)}")

    def _perform_selected_analysis(self):
        """Delegate analysis processing based on the selected type."""
        start_date = self.selected_dates['start'].toPyDate()
        end_date = self.selected_dates['end'].toPyDate()
        currencies = self.selected_currency

        exchange_rates = nbp_repository.get_exchange_rates(start_date, end_date, currencies)
        if isinstance(exchange_rates, str):
            raise ValueError(f"Failed to fetch exchange rates: {exchange_rates}")

        if self.analysis_type == 'CS':
            result = data_analysis.session_analysis(exchange_rates)
            self.display_cs_result(result)
        elif self.analysis_type == 'SM':
            result = data_analysis.statistical_analysis(exchange_rates)
            self.display_sm_result(result)
        elif self.analysis_type == 'DC':
            # Ensure exactly two currencies are selected
            if len(currencies) != 2:
                raise ValueError("Exactly two currencies must be selected for DC analysis.")

            currency_1, currency_2 = currencies

        # Ensure data exists for both currencies
            if currency_1 not in exchange_rates or currency_2 not in exchange_rates:
                raise ValueError(f"Missing exchange rate data for selected currencies: {currencies}")

        # Compute the relative exchange rate changes
            relative_exchange_rates = {
                date: exchange_rates[currency_1][date] / exchange_rates[currency_2][date]
                for date in exchange_rates[currency_1]
                if date in exchange_rates[currency_2]
            }

            img_path, histogram = data_analysis.distribution_of_change(relative_exchange_rates)
            self.display_dc_result(img_path, histogram)


    def update_selected_date(self, calendar, date_type):
        """Update the selected start or end date based on user input."""
        selected_date = calendar.selectedDate()
        if date_type == 'start':
            self.selected_dates['start'] = selected_date
        elif date_type == 'end':
            self.selected_dates['end'] = selected_date

    def update_selected_currency(self, currency):
        """Update the selected currency based on user input."""
        self.selected_currency = currency

    # Methods for displaying results
    def display_cs_result(self, result):
        """Display Session Analysis results on the AnalysisScreen."""
        screen = self.analysis_screen.findChild(QLabel, "result_label")
        screen.setText(
            f"Rising Sessions: {result.number_of_rising_sessions}\n"
            f"Falling Sessions: {result.number_of_falling_sessions}\n"
            f"Unchanged Sessions: {result.number_of_unchanged_sessions}"
        )

    def display_sm_result(self, result):
        """Display Statistical Measures results on the AnalysisScreen."""
        screen = self.analysis_screen.findChild(QLabel, "result_label")
        screen.setText(
            f"Median: {result.median}\n"
            f"Dominant: {result.dominant}\n"
            f"Standard Deviation: {result.standard_deviation}\n"
            f"Coefficient of Variation: {result.coefficient_of_variation}"
        )

    def display_dc_result(self, img_path, histogram):
        """Display Distribution of Change results on the AnalysisScreen."""
        if self.analysis_type != 'DC':
            # Clear the image label and return if not DC analysis
            img_label = self.analysis_screen.findChild(QLabel, "image_label")
            img_label.clear()
            hist_label = self.analysis_screen.findChild(QLabel, "result_label")
            hist_label.setText("No data available for this analysis type.")
            return

        # Display the image if the analysis type is DC
        img_label = self.analysis_screen.findChild(QLabel, "image_label")
        img_label.setPixmap(QPixmap(img_path))

        # Display histogram data
        hist_label = self.analysis_screen.findChild(QLabel, "result_label")
        hist_text = "\n".join([f"{k}: {v}" for k, v in histogram.items()])
        hist_label.setText(hist_text)



    def save_analysis_data(self):
        """Save the current analysis data to a file, prompting if the file exists."""
        # Default file path
        default_file_path = os.path.join(os.path.dirname(__file__), "data.txt")

        # Check if the default file exists
        if os.path.exists(default_file_path):
            # Create a custom message box with labeled buttons
            message_box = QMessageBox(self)
            message_box.setWindowTitle("File Exists")
            message_box.setText("The file 'data.txt' already exists. What would you like to do?")
            override_button = message_box.addButton("Override File", QMessageBox.AcceptRole)
            new_file_button = message_box.addButton("Create New File", QMessageBox.RejectRole)

            # Show the dialog and wait for user response
            message_box.exec()

            if message_box.clickedButton() == override_button:
                # Overwrite the existing file
                file_path = default_file_path
            elif message_box.clickedButton() == new_file_button:
                # Ask for a new filename
                new_file_name, ok = QInputDialog.getText(
                    self,
                    "New File Name",
                    "Enter a new filename (with .txt extension):",
                )
                if not ok or not new_file_name:
                    QMessageBox.warning(self, "Save Cancelled", "No file was saved.")
                    return

                file_path = os.path.join(os.path.dirname(__file__), new_file_name)
            else:
                # If no valid option is chosen, cancel the operation
                QMessageBox.warning(self, "Save Cancelled", "No file was saved.")
                return
        else:
            # If the file does not exist, proceed with the default file
            file_path = default_file_path

        # Retrieve analysis results
        result_label = self.analysis_screen.findChild(QLabel, "result_label")
        analysis_data = result_label.text()

        try:
            # Save analysis data to the chosen file path
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(analysis_data)

            # Display success message
            QMessageBox.information(
            self, "File Created", f"File '{os.path.basename(file_path)}' successfully created"
            )
        except Exception as e:
            # Display error message in case of failure
            QMessageBox.critical(
            self, "Save Error", f"An error occurred while saving the file: {str(e)}"
        )

            
    # Screen navigation methods
    def setup_main_screen(self):
        screen = QMainWindow()
        ui = MainScreen()
        ui.setupUi(screen)
        ui.button_GetAnalysis.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.analysis_selection)
        )
        self.set_logo(ui.label_logo)
        return screen

    def setup_analysis_selection(self):
        screen = QMainWindow()
        ui = AnalysisSelection()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(lambda: (self.stack.setCurrentWidget(self.main_screen), self.reset_data()))
        ui.button_CS.clicked.connect(lambda: self.validate_and_analyze('CS'))
        ui.button_SM.clicked.connect(lambda: self.validate_and_analyze('SM'))
        ui.button_DC.clicked.connect(lambda: self.validate_and_analyze('DC'))
        self.set_logo(ui.label_logo)
        return screen

    def setup_window_cs(self):
        screen = QMainWindow()
        ui = WindowCS()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(lambda: (self.stack.setCurrentWidget(self.main_screen), self.reset_data()))
        ui.button_Analyze.clicked.connect(lambda: self.process_analysis())

        # Connect currency radio buttons
        ui.radioButton_EUR.toggled.connect(lambda: self.update_selected_currency('EUR'))
        ui.radioButton_USD.toggled.connect(lambda: self.update_selected_currency('USD'))
        ui.radioButton_GBP.toggled.connect(lambda: self.update_selected_currency('GBP'))
        ui.radioButton_CHF.toggled.connect(lambda: self.update_selected_currency('NOK'))

        # Connect calendar signals
        ui.calendarFirst.clicked.connect(lambda: self.update_selected_date(ui.calendarFirst, 'start'))
        ui.calendarSecond.clicked.connect(lambda: self.update_selected_date(ui.calendarSecond, 'end'))
        self.set_logo(ui.label_logo)
        return screen

    def setup_window_sm(self):
        screen = QMainWindow()
        ui = WindowSM()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(lambda: (self.stack.setCurrentWidget(self.main_screen), self.reset_data()))
        ui.button_Analyze.clicked.connect(lambda: self.process_analysis())

        # Connect currency radio buttons
        ui.radioButton_EUR.toggled.connect(lambda: self.update_selected_currency('EUR'))
        ui.radioButton_USD.toggled.connect(lambda: self.update_selected_currency('USD'))
        ui.radioButton_GBP.toggled.connect(lambda: self.update_selected_currency('GBP'))
        ui.radioButton_CHF.toggled.connect(lambda: self.update_selected_currency('NOK'))

        # Connect calendar signals
        ui.calendarFirst.clicked.connect(lambda: self.update_selected_date(ui.calendarFirst, 'start'))
        ui.calendarSecond.clicked.connect(lambda: self.update_selected_date(ui.calendarSecond, 'end'))
        self.set_logo(ui.label_logo)
        return screen

    def setup_window_dc(self):
        screen = QMainWindow()
        ui = WindowDC()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(lambda: (self.stack.setCurrentWidget(self.main_screen), self.reset_data()))
        ui.button_Analyze.clicked.connect(lambda: self.process_analysis())

        # Connect currency radio buttons
        ui.checkBox_EUR.toggled.connect(lambda state: self.toggle_currency_selection(state, 'EUR'))
        ui.checkBox_USD.toggled.connect(lambda state: self.toggle_currency_selection(state, 'USD'))
        ui.checkBox_GBP.toggled.connect(lambda state: self.toggle_currency_selection(state, 'GBP'))
        ui.checkBox_CHF.toggled.connect(lambda state: self.toggle_currency_selection(state, 'NOK'))

        # Connect calendar signals
        ui.calendarFirst.clicked.connect(lambda: self.update_selected_date(ui.calendarFirst, 'start'))
        ui.calendarSecond.clicked.connect(lambda: self.update_selected_date(ui.calendarSecond, 'end'))
        self.set_logo(ui.label_logo)
        return screen

    def setup_analysis_screen(self):
        screen = QMainWindow()
        ui = AnalysisScreen()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(lambda: (self.stack.setCurrentWidget(self.main_screen), self.reset_data()))
        ui.button_save.clicked.connect(self.save_analysis_data)
        
        self.set_logo(ui.label_logo)
        return screen

    def set_logo(self, label: QLabel):
        """Sets the logo image in a QLabel widget."""
        logo_path = os.path.join(os.path.dirname(__file__), "LOGO.jpg")
        if os.path.exists(logo_path):
            label.setPixmap(QPixmap(logo_path))
            label.setScaledContents(True)
        else:
            print(f"Warning: LOGO.jpg not found at {logo_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())
