# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 280)
        Dialog.setMinimumSize(QtCore.QSize(360, 280))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 280))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SAM_label = QtWidgets.QLabel(Dialog)
        self.SAM_label.setStyleSheet("font: 75 48pt \"Roboto Condensed\";\n"
"color: rgb(255, 255, 255);")
        self.SAM_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SAM_label.setWordWrap(True)
        self.SAM_label.setObjectName("SAM_label")
        self.verticalLayout.addWidget(self.SAM_label)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(66, 66, 66);\n"
"    width: 15px;\n"
"    margin:1px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SAM_label.setText(_translate("Dialog", "Steam Acc Manager"))

