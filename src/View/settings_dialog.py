# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 96)
        Dialog.setMinimumSize(QtCore.QSize(260, 96))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.selectPathButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.selectPathButton.setFont(font)
        self.selectPathButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.selectPathButton.setObjectName("selectPathButton")
        self.gridLayout.addWidget(self.selectPathButton, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.backButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.selectPathButton.setText(_translate("Dialog", "Установить путь до Steam"))
        self.backButton.setText(_translate("Dialog", "Назад"))

