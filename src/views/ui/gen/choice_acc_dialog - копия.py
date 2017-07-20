# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice_acc_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 264)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(260, 0))
        Dialog.setStyleSheet("background-color:  rgb(24, 24, 24);")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget.setStyleSheet("QListWidget::item {margin: 2px 0; color: rgb(255, 255, 255); }; background-color:  rgb(24, 24, 24);\n"
"\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.choiceAccButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.choiceAccButton.setFont(font)
        self.choiceAccButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.choiceAccButton.setObjectName("choiceAccButton")
        self.verticalLayout.addWidget(self.choiceAccButton)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.backButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)

        self.retranslateUi(Dialog)
        self.backButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выбор аккаунта"))
        self.choiceAccButton.setText(_translate("Dialog", "Выбрать аккаунт"))
        self.deleteButton.setText(_translate("Dialog", "Удалить аккаунт"))
        self.backButton.setText(_translate("Dialog", "Назад"))

