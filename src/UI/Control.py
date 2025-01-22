import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox, QCalendarWidget, QCheckBox, QRadioButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate
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

        # Get the current script directory
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # Containers for data
        self.selected_dates = {'start': None, 'end': None}
        self.selected_currencies = []
        self.selected_currency = None

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
        ui.button_GoBack.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main_screen)
        )
        ui.button_CS.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.window_cs)
        )
        ui.button_SM.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.window_sm)
        )
        ui.button_DC.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.window_dc)
        )
        self.set_logo(ui.label_logo)
        return screen

    def setup_window_cs(self):
        screen = QMainWindow()
        ui = WindowCS()
        ui.setupUi(screen)
        earliest_date = QDate(2002, 1, 1)
        ui.calendarFirst.setMinimumDate(earliest_date)
        ui.calendarSecond.setMinimumDate(earliest_date)
        ui.button_GoBack.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main_screen)
        )
        ui.button_Analyze.clicked.connect(self.validate_and_analyze_cs)

        self.set_logo(ui.label_logo)
        return screen

    def setup_window_sm(self):
        screen = QMainWindow()
        ui = WindowSM()
        ui.setupUi(screen)
        earliest_date = QDate(2002, 1, 1)
        ui.calendarFirst.setMinimumDate(earliest_date)
        ui.calendarSecond.setMinimumDate(earliest_date)
        ui.button_GoBack.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main_screen)
        )
        ui.button_Analyze.clicked.connect(self.validate_and_analyze_sm)
        self.set_logo(ui.label_logo)
        return screen

    def setup_window_dc(self):
        screen = QMainWindow()
        ui = WindowDC()
        ui.setupUi(screen)
        earliest_date = QDate(2002, 1, 1)
        ui.calendarFirst.setMinimumDate(earliest_date)
        ui.calendarSecond.setMinimumDate(earliest_date)
        ui.button_GoBack.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main_screen)
        )
        ui.button_Analyze.clicked.connect(self.validate_and_analyze_dc)
        self.set_logo(ui.label_logo)
        return screen

    def setup_analysis_screen(self):
        screen = QMainWindow()
        ui = AnalysisScreen()
        ui.setupUi(screen)
        ui.button_GoBack.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.main_screen)
        )
        self.set_logo(ui.label_logo)
        return screen

    def set_logo(self, label: QLabel):
        """Sets the logo image in a QLabel widget."""
        logo_path = os.path.join(self.base_path, "LOGO.jpg")
        if os.path.exists(logo_path):
            label.setPixmap(QPixmap(logo_path))
            label.setScaledContents(True)
        else:
            print(f"Warning: LOGO.jpg not found at {logo_path}")

    def validate_and_analyze_sm(self):
        """Validation for WindowSM - Ensures both dates and one radio button are selected."""
        screen = self.stack.currentWidget()
        calendar_first = screen.findChild(QCalendarWidget, "calendarFirst")
        calendar_second = screen.findChild(QCalendarWidget, "calendarSecond")

        if not calendar_first or not calendar_second:
            QMessageBox.critical(self, "Error", "Calendar widgets not found.")
            return

        start_date = calendar_first.selectedDate()
        end_date = calendar_second.selectedDate()
        
        if start_date < QDate(2002, 1, 1) or end_date < QDate(2002, 1, 1):
            QMessageBox.warning(self, "Input Error", "Dates cannot be earlier than 2002-01-01.")
            return

        if start_date >= end_date:
            QMessageBox.warning(self, "Input Error", "The first date must be earlier than the second date.")
            return
        
        currency_buttons = {
            "NOK": screen.findChild(QRadioButton, "radioButton_CHF"),
            "USD": screen.findChild(QRadioButton, "radioButton_USD"),
            "EUR": screen.findChild(QRadioButton, "radioButton_EUR"),
            "GBP": screen.findChild(QRadioButton, "radioButton_GBP"),
        }
        selected_currency = next((key for key, btn in currency_buttons.items() if btn and btn.isChecked()), None)

        if not start_date or not end_date or not selected_currency:
            QMessageBox.warning(self, "Input Error", "Not enough data selected.")
            return
        
        print("SM Analysis:")
        print(f"Currency: {selected_currency}")
        print(f"Start Date: {start_date.toString('yyyy-MM-dd')}")
        print(f"End Date: {end_date.toString('yyyy-MM-dd')}")
        self.selected_dates['start'] = start_date
        self.selected_dates['end'] = end_date
        self.selected_currency = selected_currency
        self.stack.setCurrentWidget(self.analysis_screen)
        
    def validate_and_analyze_cs(self):
        """Validation for WindowSM - Ensures both dates and one radio button are selected."""
        screen = self.stack.currentWidget()
        calendar_first = screen.findChild(QCalendarWidget, "calendarFirst")
        calendar_second = screen.findChild(QCalendarWidget, "calendarSecond")

        if not calendar_first or not calendar_second:
            QMessageBox.critical(self, "Error", "Calendar widgets not found.")
            return

        start_date = calendar_first.selectedDate()
        end_date = calendar_second.selectedDate()

        if start_date < QDate(2002, 1, 1) or end_date < QDate(2002, 1, 1):
            QMessageBox.warning(self, "Input Error", "Dates cannot be earlier than 2002-01-01.")
            return

        if start_date >= end_date:
            QMessageBox.warning(self, "Input Error", "The first date must be earlier than the second date.")
            return
        
        currency_buttons = {
            "NOK": screen.findChild(QRadioButton, "radioButton_CHF"),
            "USD": screen.findChild(QRadioButton, "radioButton_USD"),
            "EUR": screen.findChild(QRadioButton, "radioButton_EUR"),
            "GBP": screen.findChild(QRadioButton, "radioButton_GBP"),
        }
        selected_currency = next((key for key, btn in currency_buttons.items() if btn and btn.isChecked()), None)

        if not start_date or not end_date or not selected_currency:
            QMessageBox.warning(self, "Input Error", "Not enough data selected.")
            return
        print("CS Analysis:")
        print(f"Currency: {selected_currency}")
        print(f"Start Date: {start_date.toString('yyyy-MM-dd')}")
        print(f"End Date: {end_date.toString('yyyy-MM-dd')}")
        self.selected_dates['start'] = start_date
        self.selected_dates['end'] = end_date
        self.selected_currency = selected_currency
        self.stack.setCurrentWidget(self.analysis_screen)

    def validate_and_analyze_dc(self):
        """Validation for WindowDC - Ensures both dates and at least two checkboxes are selected."""
        screen = self.stack.currentWidget()
        calendar_first = screen.findChild(QCalendarWidget, "calendarFirst")
        calendar_second = screen.findChild(QCalendarWidget, "calendarSecond")

        if not calendar_first or not calendar_second:
            QMessageBox.critical(self, "Error", "Calendar widgets not found.")
            return

        start_date = calendar_first.selectedDate()
        end_date = calendar_second.selectedDate()
        
        if start_date < QDate(2002, 1, 1) or end_date < QDate(2002, 1, 1):
            QMessageBox.warning(self, "Input Error", "Dates cannot be earlier than 2002-01-01.")
            return

        if start_date >= end_date:
            QMessageBox.warning(self, "Input Error", "The first date must be earlier than the second date.")
            return
        currency_checkboxes = {
            "NOK": screen.findChild(QCheckBox, "checkBox_CHF"),
            "USD": screen.findChild(QCheckBox, "checkBox_USD"),
            "EUR": screen.findChild(QCheckBox, "checkBox_EUR"),
            "GBP": screen.findChild(QCheckBox, "checkBox_GBP"),
        }
        selected_currencies = [key for key, cb in currency_checkboxes.items() if cb and cb.isChecked()]

        if not start_date or not end_date or len(selected_currencies) < 2 :
            QMessageBox.warning(self, "Input Error", "Not enough data selected.")
            return
        if not start_date or not end_date or len(selected_currencies) > 2 :
            QMessageBox.warning(self, "Input Error", "Too  much data selected.")
            return
        
        print("DC Analysis:")
        print(f"Currencies: {', '.join(selected_currencies)}")
        print(f"Start Date: {start_date.toString('yyyy-MM-dd')}")
        print(f"End Date: {end_date.toString('yyyy-MM-dd')}")
        self.selected_dates['start'] = start_date
        self.selected_dates['end'] = end_date
        self.selected_currencies = selected_currencies
        self.stack.setCurrentWidget(self.analysis_screen)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())