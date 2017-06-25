from PyQt5 import QtCore, QtWidgets

import model
from view import addacc_dialog, choice_acc_dialog, settings_dialog


def show_choice_acc_dialog():
    dialog = QtWidgets.QDialog()
    ui = choice_acc_dialog.Ui_Dialog()
    ui.setupUi(dialog)
    accounts = model.read_accs()
    ui.listWidget.addItems(accounts)
    ui.listWidget.itemDoubleClicked.connect(lambda: model.login(accounts[ui.listWidget.currentItem().text()]))
    ui.listWidget.itemDoubleClicked.connect(dialog.close)
    ui.choiceAccButton.clicked.connect(lambda: model.login(accounts[ui.listWidget.currentItem().text()]))
    ui.deleteButton.clicked.connect(lambda: model.delete_acc(ui.listWidget.currentItem().text()))
    ui.deleteButton.clicked.connect(lambda: ui.listWidget.takeItem(ui.listWidget.currentRow()))
    dialog.exec_()


def show_create_acc_dialog():
    dialog = QtWidgets.QDialog()
    ui = addacc_dialog.Ui_Dialog()
    ui.setupUi(dialog)
    ui.pushButton.clicked.connect(lambda: model.add_acc(ui.login_lineEdit.text(),
                                                        ui.passwrd_lineEdit.text(),
                                                        ui.steamlink_lineEdit.text()))
    ui.pushButton.clicked.connect(dialog.close)
    dialog.exec_()


def show_setting_dialog():
    dialog = QtWidgets.QDialog()
    ui = settings_dialog.Ui_Dialog()
    ui.setupUi(dialog)
    ui.selectPathButton.clicked.connect(show_selectPath_dialog)
    ui.selectPathButton.clicked.connect(dialog.close)
    ui.backButton.clicked.connect(dialog.close)
    dialog.setMaximumSize(QtCore.QSize(16777215, dialog.height()))
    dialog.exec_()


def show_selectPath_dialog():
    steam_path = QtWidgets.QFileDialog.getExistingDirectory()
    model.set_steam_path(steam_path + "/Steam.exe")