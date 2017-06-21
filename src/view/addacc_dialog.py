# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addacc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 175)
        Dialog.setMinimumSize(QtCore.QSize(320, 175))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 175))
        Dialog.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_label.setObjectName("login_label")
        self.verticalLayout_2.addWidget(self.login_label)
        self.login_lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.verticalLayout_2.addWidget(self.login_lineEdit)
        self.passwrd_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.passwrd_label.setFont(font)
        self.passwrd_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwrd_label.setObjectName("passwrd_label")
        self.verticalLayout_2.addWidget(self.passwrd_label)
        self.passwrd_lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.passwrd_lineEdit.setFont(font)
        self.passwrd_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwrd_lineEdit.setObjectName("passwrd_lineEdit")
        self.verticalLayout_2.addWidget(self.passwrd_lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление нового аккаунта"))
        self.login_label.setText(_translate("Dialog", "Введите логин: "))
        self.passwrd_label.setText(_translate("Dialog", "Введите пароль:"))
        self.pushButton.setText(_translate("Dialog", "Добавить аккаунт"))

