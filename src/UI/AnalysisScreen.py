from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("background-color:rgb(119, 196, 226)")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Frame for results display
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 150, 924, 500))
        self.frame.setStyleSheet("border-radius: 15px; background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # QLabel for displaying analysis text results
        self.result_label = QtWidgets.QLabel(self.frame)
        self.result_label.setGeometry(QtCore.QRect(20, 20, 400, 460))
        self.result_label.setStyleSheet("font: 14pt 'Leelawadee UI';")
        self.result_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.result_label.setWordWrap(True)
        self.result_label.setObjectName("result_label")

        # QLabel for displaying analysis images
        self.image_label = QtWidgets.QLabel(self.frame)
        self.image_label.setGeometry(QtCore.QRect(450, 20, 450, 450))
        self.image_label.setStyleSheet("border: 1px solid gray;")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")

        # Back button
        self.button_GoBack = QtWidgets.QPushButton(self.centralwidget)
        self.button_GoBack.setGeometry(QtCore.QRect(50, 700, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_GoBack.setFont(font)
        self.button_GoBack.setStyleSheet("border-radius :20px; background-color: rgb(255, 255, 255);")
        self.button_GoBack.setObjectName("button_GoBack")

        # Logo
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(0, 0, 251, 141))
        self.label_logo.setPixmap(QtGui.QPixmap("LOGO.jpg"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analysis Results"))
        self.result_label.setText(_translate("MainWindow", "Results will be displayed here."))
        self.image_label.setText(_translate("MainWindow", "Histogram will appear here."))
        self.button_GoBack.setText(_translate("MainWindow", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
