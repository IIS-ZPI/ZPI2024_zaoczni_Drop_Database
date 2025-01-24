from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1024, 768)
                MainWindow.setStyleSheet("background-color:rgb(119, 196, 226)")
                
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(450, 270, 551, 311))
                self.frame.setPalette(self.create_palette())
                self.frame.setAutoFillBackground(False)
                self.frame.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                
                self.button_Analyze = QtWidgets.QPushButton(self.frame)
                self.button_Analyze.setGeometry(QtCore.QRect(200, 250, 150, 30))
                self.button_Analyze.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.button_Analyze.setStyleSheet("background-color: rgb(118, 196, 225);\nborder-radius: 15px;")
                self.button_Analyze.setObjectName("button_Analyze")
                
                self.widget = QtWidgets.QWidget(self.frame)
                self.widget.setGeometry(QtCore.QRect(0, 70, 551, 154))
                self.widget.setObjectName("widget")
                
                self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
                self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
                self.gridLayout_3.setObjectName("gridLayout_3")
                
                self.add_currency_icons()
                self.add_checkboxes()
                
                self.label_logo = QtWidgets.QLabel(self.centralwidget)
                self.label_logo.setGeometry(QtCore.QRect(0, 0, 251, 141))
                self.label_logo.setPixmap(QtGui.QPixmap("LOGO.jpg"))
                self.label_logo.setScaledContents(True)
                self.label_logo.setObjectName("label_logo")
                
                self.button_GoBack = QtWidgets.QPushButton(self.centralwidget)
                self.button_GoBack.setGeometry(QtCore.QRect(50, 700, 81, 41))
                self.button_GoBack.setFont(self.create_font("Leelawadee UI", 10, True, 75))
                self.button_GoBack.setStyleSheet("border-radius :20px;\nbackground-color: rgb(255, 255, 255);")
                self.button_GoBack.setObjectName("button_GoBack")
                
                self.label_SM2 = QtWidgets.QLabel(self.centralwidget)
                self.label_SM2.setGeometry(QtCore.QRect(610, 210, 231, 49))
                self.label_SM2.setFont(self.create_font("Leelawadee UI", 12))
                self.label_SM2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_SM2.setObjectName("label_SM2")
                
                self.label_SM = QtWidgets.QLabel(self.centralwidget)
                self.label_SM.setGeometry(QtCore.QRect(650, 70, 150, 150))
                self.label_SM.setFont(self.create_font("Leelawadee UI", 20, True, 75))
                self.label_SM.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(27, 151, 185);")
                self.label_SM.setAlignment(QtCore.Qt.AlignCenter)
                self.label_SM.setObjectName("label_SM")
                
                self.calendarFirst = QtWidgets.QCalendarWidget(self.centralwidget)
                self.calendarFirst.setGeometry(QtCore.QRect(20, 200, 400, 230))
                self.calendarFirst.setObjectName("calendarFirst")
                
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(10, 150, 421, 541))
                self.frame_2.setPalette(self.create_palette())
                self.frame_2.setAutoFillBackground(False)
                self.frame_2.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                
                self.label_PickDates = QtWidgets.QLabel(self.frame_2)
                self.label_PickDates.setGeometry(QtCore.QRect(10, 10, 131, 31))
                self.label_PickDates.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.label_PickDates.setObjectName("label_PickDates")
                
                self.calendarSecond = QtWidgets.QCalendarWidget(self.centralwidget)
                self.calendarSecond.setGeometry(QtCore.QRect(20, 450, 400, 230))
                self.calendarSecond.setObjectName("calendarSecond")
                
                self.raise_widgets()
                
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def create_palette(self):
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
                return palette

        def create_font(self, family, size, bold=False, weight=50):
                font = QtGui.QFont()
                font.setFamily(family)
                font.setPointSize(size)
                font.setBold(bold)
                font.setWeight(weight)
                return font

        def add_currency_icons(self):
                self.label_USD_icon = QtWidgets.QLabel(self.widget)
                self.label_USD_icon.setMaximumSize(QtCore.QSize(100, 100))
                self.label_USD_icon.setPixmap(QtGui.QPixmap("USD.jpg"))
                self.label_USD_icon.setScaledContents(True)
                self.label_USD_icon.setObjectName("label_USD_icon")
                self.gridLayout_3.addWidget(self.label_USD_icon, 0, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                
                self.label_CHF_icon = QtWidgets.QLabel(self.widget)
                self.label_CHF_icon.setMaximumSize(QtCore.QSize(100, 100))
                self.label_CHF_icon.setPixmap(QtGui.QPixmap("NOK.jpg"))
                self.label_CHF_icon.setScaledContents(True)
                self.label_CHF_icon.setObjectName("label_CHF_icon")
                self.gridLayout_3.addWidget(self.label_CHF_icon, 0, 2, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                
                self.label_EUR_icon = QtWidgets.QLabel(self.widget)
                self.label_EUR_icon.setMaximumSize(QtCore.QSize(100, 100))
                self.label_EUR_icon.setPixmap(QtGui.QPixmap("EUR.jpg"))
                self.label_EUR_icon.setScaledContents(True)
                self.label_EUR_icon.setObjectName("label_EUR_icon")
                self.gridLayout_3.addWidget(self.label_EUR_icon, 0, 3, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                
                self.label_GBP_icon = QtWidgets.QLabel(self.widget)
                self.label_GBP_icon.setMaximumSize(QtCore.QSize(100, 100))
                self.label_GBP_icon.setPixmap(QtGui.QPixmap("GBP.jpg"))
                self.label_GBP_icon.setScaledContents(True)
                self.label_GBP_icon.setObjectName("label_GBP_icon")
                self.gridLayout_3.addWidget(self.label_GBP_icon, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        def add_checkboxes(self):
                self.checkBox_GBP = QtWidgets.QCheckBox(self.widget)
                self.checkBox_GBP.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.checkBox_GBP.setObjectName("checkBox_GBP")
                self.gridLayout_3.addWidget(self.checkBox_GBP, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
                
                self.checkBox_CHF = QtWidgets.QCheckBox(self.widget)
                self.checkBox_CHF.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.checkBox_CHF.setObjectName("checkBox_CHF")
                self.gridLayout_3.addWidget(self.checkBox_CHF, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
                
                self.checkBox_USD = QtWidgets.QCheckBox(self.widget)
                self.checkBox_USD.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.checkBox_USD.setObjectName("checkBox_USD")
                self.gridLayout_3.addWidget(self.checkBox_USD, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
                
                self.checkBox_EUR = QtWidgets.QCheckBox(self.widget)
                self.checkBox_EUR.setFont(self.create_font("Leelawadee UI", 12, True, 75))
                self.checkBox_EUR.setObjectName("checkBox_EUR")
                self.gridLayout_3.addWidget(self.checkBox_EUR, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)

        def raise_widgets(self):
                self.frame_2.raise_()
                self.label_logo.raise_()
                self.frame.raise_()
                self.button_GoBack.raise_()
                self.label_SM2.raise_()
                self.label_SM.raise_()
                self.calendarFirst.raise_()
                self.calendarSecond.raise_()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.button_Analyze.setText(_translate("MainWindow", "Analyze"))
                self.checkBox_GBP.setText(_translate("MainWindow", "GBP"))
                self.checkBox_CHF.setText(_translate("MainWindow", "NOK"))
                self.checkBox_USD.setText(_translate("MainWindow", "USD"))
                self.checkBox_EUR.setText(_translate("MainWindow", "EUR"))
                self.button_GoBack.setText(_translate("MainWindow", "Go back"))
                self.label_SM2.setText(_translate("MainWindow", "Distribution of change"))
                self.label_SM.setText(_translate("MainWindow", "DC"))
                self.label_PickDates.setText(_translate("MainWindow", "Pick dates:"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
