# coding=utf-8
from controllers.controller import Controller
from utility.sam_cfg import SAMCfg
from views.settings_view import SettingsView
from PyQt5 import QtWidgets


class SettingsController(Controller):
    def __init__(self):
        self.view = SettingsView()
        super(SettingsController, self).__init__(self.view)
        self.sam_cfg = SAMCfg()
        # Привязка кнопок к функциям
        self.view.ui.selectPathButton.clicked.connect(self.selectPathBtnIsClicked)
        # Запуск окна
        self.view.exec_()

    def selectPathBtnIsClicked(self):
        steam_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.sam_cfg.set_steam_path(steam_path + "/Steam.exe")
        self.view.close()
