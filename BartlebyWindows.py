# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BartlebyWindows.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 389)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -1, 771, 391))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 6, 173, 255), stop:1 rgba(48, 83, 237, 255));\n"
"border-radius:3px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 40, 481, 71))
        self.label.setStyleSheet("background-color:none;\n"
"color: rgb(241, 241, 241);\n"
"font: 63 25pt \"Segoe UI Semibold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 481, 31))
        self.label_2.setStyleSheet("background-color:none;\n"
"color: rgb(241, 241, 241);\n"
"font: 25 14pt \"Segoe UI Light\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 180, 441, 41))
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: rgb(241, 241, 241);\n"
"border-radius:3px;\n"
"font: 9pt \"Nirmala UI\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 260, 441, 41))
        self.pushButton.setStyleSheet("QPushButton{border:none;\n"
"background-color: rgb(44, 76, 231);\n"
"color: rgb(235, 235, 235);\n"
"font: 28 14pt \"Segoe UI Light\";\n"
"border-radius:3px;}\n"
"QPushButton::hover{\n"
"border:0.5px solid rgb(220, 220, 220);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 16, 16))
        self.pushButton_2.setStyleSheet("QPushButton{border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(216, 10, 13);}\n"
"QPushButton::hover{\n"
"     background-color: rgb(127, 5, 13);\n"
"\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 20, 16, 16))
        self.pushButton_3.setStyleSheet("QPushButton{border:none;\n"
"border-radius:8px;\n"
"background-color: rgb(115, 213, 23);}\n"
"QPushButton::hover{\n"
"     background-color: rgb(55, 148, 22);\n"
"\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(80, 340, 641, 31))
        self.label_3.setStyleSheet("background-color:none;\n"
"color: rgb(241, 241, 241);\n"
"font: 8pt \"Nirmala UI\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BartlebySolution"))
        self.label.setText(_translate("MainWindow", "Bartleby Free Answers"))
        self.label_2.setText(_translate("MainWindow", "This is free tool don\'t sell it "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Put your Bartleby Url here . . ."))
        self.pushButton.setText(_translate("MainWindow", "Get Answer"))
        self.label_3.setText(_translate("MainWindow", "Copyright © 2021 Abdulrahman Ghazi technologies co. ltd. all rights reserved"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
