from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1024, 768)
                MainWindow.setStyleSheet("background-color:rgb(119, 196, 226)")
                
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(250, 270, 700, 231))
                self.frame.setStyleSheet("border-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                
                self.button_CS = QtWidgets.QPushButton(self.frame)
                self.button_CS.setGeometry(QtCore.QRect(50, 20, 150, 150))
                self.button_CS.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                self.button_CS.setFont(QtGui.QFont("Leelawadee UI", 20, QtGui.QFont.Bold))
                self.button_CS.setStyleSheet("background-color: rgb(39, 180, 233);")
                self.button_CS.setObjectName("button_CS")
                
                self.button_DC = QtWidgets.QPushButton(self.frame)
                self.button_DC.setGeometry(QtCore.QRect(275, 20, 150, 150))
                self.button_DC.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
                self.button_DC.setFont(QtGui.QFont("Leelawadee UI", 20, QtGui.QFont.Bold))
                self.button_DC.setStyleSheet("background-color: rgb(27, 151, 185);")
                self.button_DC.setObjectName("button_DC")
                
                self.button_SM = QtWidgets.QPushButton(self.frame)
                self.button_SM.setGeometry(QtCore.QRect(500, 20, 150, 150))
                self.button_SM.setFont(QtGui.QFont("Leelawadee UI", 20, QtGui.QFont.Bold))
                self.button_SM.setStyleSheet("background-color: rgb(5, 117, 189);")
                self.button_SM.setObjectName("button_SM")
                
                self.label_DC = QtWidgets.QLabel(self.frame)
                self.label_DC.setGeometry(QtCore.QRect(240, 170, 221, 49))
                self.label_DC.setFont(QtGui.QFont("Leelawadee UI", 12))
                self.label_DC.setAlignment(QtCore.Qt.AlignCenter)
                self.label_DC.setObjectName("label_DC")
                
                self.label_SM = QtWidgets.QLabel(self.frame)
                self.label_SM.setGeometry(QtCore.QRect(460, 170, 231, 49))
                self.label_SM.setFont(QtGui.QFont("Leelawadee UI", 12))
                self.label_SM.setAlignment(QtCore.Qt.AlignCenter)
                self.label_SM.setObjectName("label_SM")
                
                self.label_CS = QtWidgets.QLabel(self.frame)
                self.label_CS.setGeometry(QtCore.QRect(-1, 170, 241, 49))
                self.label_CS.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
                self.label_CS.setFont(QtGui.QFont("Leelawadee UI", 12))
                self.label_CS.setAlignment(QtCore.Qt.AlignCenter)
                self.label_CS.setObjectName("label_CS")
                
                self.label_logo = QtWidgets.QLabel(self.centralwidget)
                self.label_logo.setGeometry(QtCore.QRect(0, 0, 271, 161))
                self.label_logo.setPixmap(QtGui.QPixmap("LOGO.jpg"))
                self.label_logo.setScaledContents(True)
                self.label_logo.setObjectName("label_logo")
                
                self.label_TypeOfAnalysis = QtWidgets.QLabel(self.centralwidget)
                self.label_TypeOfAnalysis.setGeometry(QtCore.QRect(250, 230, 171, 31))
                self.label_TypeOfAnalysis.setFont(QtGui.QFont("Leelawadee UI", 12))
                self.label_TypeOfAnalysis.setObjectName("label_TypeOfAnalysis")
                
                self.button_GoBack = QtWidgets.QPushButton(self.centralwidget)
                self.button_GoBack.setGeometry(QtCore.QRect(50, 700, 81, 41))
                self.button_GoBack.setFont(QtGui.QFont("Leelawadee UI", 10, QtGui.QFont.Bold))
                self.button_GoBack.setStyleSheet("border-radius :20px;\nbackground-color: rgb(255, 255, 255);\n")
                self.button_GoBack.setObjectName("button_GoBack")
                
                self.label_logo.raise_()
                self.frame.raise_()
                self.label_TypeOfAnalysis.raise_()
                self.button_GoBack.raise_()
                
                MainWindow.setCentralWidget(self.centralwidget)
                
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.button_CS.setText(_translate("MainWindow", "CS"))
                self.button_DC.setText(_translate("MainWindow", "DC"))
                self.button_SM.setText(_translate("MainWindow", "SM"))
                self.label_DC.setText(_translate("MainWindow", "Distribution of change"))
                self.label_SM.setText(_translate("MainWindow", "Statistical measures"))
                self.label_CS.setText(_translate("MainWindow", "Session analysis"))
                self.label_TypeOfAnalysis.setText(_translate("MainWindow", "Type of analysis:"))
                self.button_GoBack.setText(_translate("MainWindow", "Go back"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
