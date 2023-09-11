from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VideoCaptureButton = QtWidgets.QPushButton(self.centralwidget)
        self.VideoCaptureButton.setGeometry(QtCore.QRect(750, 110, 75, 23))
        self.VideoCaptureButton.setObjectName("VideoCaptureButton")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(290, 0, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 90, 381, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(680, 108, 61, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.VideoCaptureLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoCaptureLabel.setGeometry(QtCore.QRect(590, 110, 91, 21))
        self.VideoCaptureLabel.setObjectName("VideoCaptureLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 80, 291, 21))
        self.label.setObjectName("label")
        self.EyetrackingFrame = QtWidgets.QFrame(self.centralwidget)
        self.EyetrackingFrame.setGeometry(QtCore.QRect(420, 150, 600, 450))
        self.EyetrackingFrame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.EyetrackingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EyetrackingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EyetrackingFrame.setObjectName("EyetrackingFrame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VideoCaptureButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label1.setText(_translate("MainWindow", "EYE MOUSE HANDLER"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.VideoCaptureLabel.setText(_translate("MainWindow", "Camera Number"))
        self.label.setText(_translate("MainWindow", "If default camera is installed then choose camera number 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
