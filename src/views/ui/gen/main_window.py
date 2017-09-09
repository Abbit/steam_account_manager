# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 250)
        Dialog.setMinimumSize(QtCore.QSize(530, 0))
        Dialog.setStyleSheet("background-color:  rgb(24, 24, 24);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SAM_label = QtWidgets.QLabel(Dialog)
        self.SAM_label.setAutoFillBackground(False)
        self.SAM_label.setStyleSheet("font: 75 48pt \"Roboto Condensed\";\n"
"color: rgb(255, 255, 255);")
        self.SAM_label.setTextFormat(QtCore.Qt.PlainText)
        self.SAM_label.setScaledContents(True)
        self.SAM_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SAM_label.setWordWrap(True)
        self.SAM_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.SAM_label.setObjectName("SAM_label")
        self.verticalLayout.addWidget(self.SAM_label)
        self.choice_acc_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.choice_acc_btn.setFont(font)
        self.choice_acc_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.choice_acc_btn.setObjectName("choice_acc_btn")
        self.verticalLayout.addWidget(self.choice_acc_btn)
        self.add_acc_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.add_acc_btn.setFont(font)
        self.add_acc_btn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.add_acc_btn.setToolTip("")
        self.add_acc_btn.setStatusTip("")
        self.add_acc_btn.setWhatsThis("")
        self.add_acc_btn.setAccessibleName("")
        self.add_acc_btn.setAccessibleDescription("")
        self.add_acc_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.add_acc_btn.setObjectName("add_acc_btn")
        self.verticalLayout.addWidget(self.add_acc_btn)
        self.settings_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.settings_btn.setFont(font)
        self.settings_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.settings_btn.setObjectName("settings_btn")
        self.verticalLayout.addWidget(self.settings_btn)
        self.quit_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.quit_btn.setObjectName("quit_btn")
        self.verticalLayout.addWidget(self.quit_btn)
        self.byAbbit_label = QtWidgets.QLabel(Dialog)
        self.byAbbit_label.setStyleSheet("color:  rgb(24, 24, 24);")
        self.byAbbit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.byAbbit_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.byAbbit_label.setObjectName("byAbbit_label")
        self.verticalLayout.addWidget(self.byAbbit_label)

        self.retranslateUi(Dialog)
        self.quit_btn.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Steam Acc Manager"))
        self.SAM_label.setText(_translate("Dialog", "Steam Acc Manager"))
        self.choice_acc_btn.setText(_translate("Dialog", "Выбрать аккаунт"))
        self.add_acc_btn.setText(_translate("Dialog", "Добавить новый аккаунт"))
        self.settings_btn.setText(_translate("Dialog", "Настройки"))
        self.quit_btn.setText(_translate("Dialog", "Выйти"))
        self.byAbbit_label.setText(_translate("Dialog", "by Abbit"))

