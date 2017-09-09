from controllers.controller import Controller
from views.settings_view import SettingsView
from PyQt5 import QtWidgets
from utility.steamprocess import SteamProcess


class SettingsController(Controller):
    def __init__(self):
        self.view = SettingsView()
        super(SettingsController, self).__init__(self.view)
        self.steamprocess = SteamProcess()
        # Привязка кнопок к функциям
        self.view.ui.selectPathButton.clicked.connect(self.selectPathBtnIsClicked)
        # Запуск окна
        self.view.exec_()

    def selectPathBtnIsClicked(self):
        steam_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.steamprocess.set_steam_path(steam_path + "/Steam.exe")
        self.view.close()
