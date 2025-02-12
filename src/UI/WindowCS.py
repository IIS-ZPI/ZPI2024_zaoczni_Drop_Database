import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("./src/UI/"), relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color:rgb(119, 196, 226)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 270, 551, 311))
        self._set_palette()
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self._setup_buttons()
        self._setup_layout()
        self._setup_labels()
        self._setup_calendars()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _set_palette(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(24, 36, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)

    def _setup_buttons(self):
        self.button_Analyze = QtWidgets.QPushButton(self.frame)
        self.button_Analyze.setGeometry(QtCore.QRect(200, 250, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_Analyze.setFont(font)
        self.button_Analyze.setStyleSheet("background-color: rgb(118, 196, 225);\nborder-radius: 15px;")
        self.button_Analyze.setObjectName("button_Analyze")
        self.button_GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.button_GoBack.setGeometry(QtCore.QRect(50, 700, 81, 41))
        font.setPointSize(10)
        self.button_GoBack.setFont(font)
        self.button_GoBack.setStyleSheet("border-radius :20px;\nbackground-color: rgb(255, 255, 255);")
        self.button_GoBack.setObjectName("button_GoBack")

    def _setup_layout(self):
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 70, 551, 154))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self._setup_radio_buttons()
        self._setup_icons()

    def _setup_radio_buttons(self):
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_NOK = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_NOK.setFont(font)
        self.radioButton_NOK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_NOK.setObjectName("radioButton_NOK")
        self.gridLayout_3.addWidget(self.radioButton_NOK, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_GBP = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_GBP.setFont(font)
        self.radioButton_GBP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_GBP.setObjectName("radioButton_GBP")
        self.gridLayout_3.addWidget(self.radioButton_GBP, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_USD = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_USD.setFont(font)
        self.radioButton_USD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_USD.setObjectName("radioButton_USD")
        self.gridLayout_3.addWidget(self.radioButton_USD, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioButton_EUR = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_EUR.setFont(font)
        self.radioButton_EUR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_EUR.setObjectName("radioButton_EUR")
        self.gridLayout_3.addWidget(self.radioButton_EUR, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)

    def _setup_icons(self):
        self.label_EUR_icon = QtWidgets.QLabel(self.layoutWidget)
        self.label_EUR_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.label_EUR_icon.setPixmap(QtGui.QPixmap(resource_path("./images/EUR.jpg")))
        self.label_EUR_icon.setScaledContents(True)
        self.label_EUR_icon.setObjectName("label_EUR_icon")
        self.gridLayout_3.addWidget(self.label_EUR_icon, 0, 3, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_NOK_icon = QtWidgets.QLabel(self.layoutWidget)
        self.label_NOK_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.label_NOK_icon.setPixmap(QtGui.QPixmap(resource_path("./images/NOK.jpg")))
        self.label_NOK_icon.setScaledContents(True)
        self.label_NOK_icon.setObjectName("label_NOK_icon")
        self.gridLayout_3.addWidget(self.label_NOK_icon, 0, 2, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_USD_icon = QtWidgets.QLabel(self.layoutWidget)
        self.label_USD_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.label_USD_icon.setPixmap(QtGui.QPixmap(resource_path("./images/USD.jpg")))
        self.label_USD_icon.setScaledContents(True)
        self.label_USD_icon.setObjectName("label_USD_icon")
        self.gridLayout_3.addWidget(self.label_USD_icon, 0, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_GBP_icon = QtWidgets.QLabel(self.layoutWidget)
        self.label_GBP_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.label_GBP_icon.setPixmap(QtGui.QPixmap(resource_path("./images/GBP.jpg")))
        self.label_GBP_icon.setScaledContents(True)
        self.label_GBP_icon.setObjectName("label_GBP_icon")
        self.gridLayout_3.addWidget(self.label_GBP_icon, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def _setup_labels(self):
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(0, 0, 251, 141))
        self.label_logo.setPixmap(QtGui.QPixmap(resource_path("./images/LOGO.jpg")))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_SM2 = QtWidgets.QLabel(self.centralwidget)
        self.label_SM2.setGeometry(QtCore.QRect(610, 210, 231, 49))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_SM2.setFont(font)
        self.label_SM2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SM2.setObjectName("label_SM2")
        self.label_SM = QtWidgets.QLabel(self.centralwidget)
        self.label_SM.setGeometry(QtCore.QRect(650, 70, 150, 150))
        font.setPointSize(20)
        self.label_SM.setFont(font)
        self.label_SM.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(39, 180, 233);")
        self.label_SM.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SM.setObjectName("label_SM")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 421, 541))
        self._set_palette()
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_PickDates = QtWidgets.QLabel(self.frame_2)
        self.label_PickDates.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font.setPointSize(12)
        self.label_PickDates.setFont(font)
        self.label_PickDates.setObjectName("label_PickDates")

    def _setup_calendars(self):
        self.calendarFirst = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarFirst.setGeometry(QtCore.QRect(20, 200, 400, 230))
        self.calendarFirst.setObjectName("calendarFirst")
        self.calendarSecond = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarSecond.setGeometry(QtCore.QRect(20, 450, 400, 230))
        self.calendarSecond.setObjectName("calendarSecond")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Analyze.setText(_translate("MainWindow", "Analyze"))
        self.radioButton_NOK.setText(_translate("MainWindow", "NOK"))
        self.radioButton_GBP.setText(_translate("MainWindow", "GBP"))
        self.radioButton_USD.setText(_translate("MainWindow", "USD"))
        self.radioButton_EUR.setText(_translate("MainWindow", "EUR"))
        self.button_GoBack.setText(_translate("MainWindow", "Go back"))
        self.label_SM2.setText(_translate("MainWindow", "Session analysis"))
        self.label_SM.setText(_translate("MainWindow", "CS"))
        self.label_PickDates.setText(_translate("MainWindow", "Pick dates:"))

    def load_icons(self, base_path):
        """Dynamically load icons for currency labels and the main logo."""
        icon_paths = {
            "GBP": "GBP.png",
            "USD": "USD.png",
            "NOK": "NOK.png",
            "EUR": "EUR.png",
        }

        labels = {
            "GBP": self.label_GBP_icon,
            "USD": self.label_USD_icon,
            "NOK": self.label_NOK_icon,
            "EUR": self.label_EUR_icon,
        }

        # Load currency icons
        for currency, file_name in icon_paths.items():
            file_path = QtCore.QFileInfo(QtCore.QDir(base_path), file_name).absoluteFilePath()
            if QtCore.QFile.exists(file_path):
                labels[currency].setPixmap(QtGui.QPixmap(file_path))
            else:
                print(f"Warning: Icon for {currency} not found at {file_path}")

        # Load the main logo
        logo_path = QtCore.QFileInfo(QtCore.QDir(base_path), "LOGO.jpg").absoluteFilePath()
        if QtCore.QFile.exists(logo_path):
            self.label_logo.setPixmap(QtGui.QPixmap(logo_path))
        else:
            print(f"Warning: Logo not found at {logo_path}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    icon_base_path = os.path.abspath("./ICONS")  # Adjust to the actual path of your icons folder
    ui.load_icons(icon_base_path)
    MainWindow.show()
    sys.exit(app.exec_())