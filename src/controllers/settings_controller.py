from views.settings_view import SettingsView
from PyQt5 import QtWidgets
from utility.steamprocess import SteamProcess


class SAMSettingsController:
    def __init__(self):
        self.steamprocess = SteamProcess()
        self.view = SettingsView()
        self.view.show()

        self.view.ui.selectPathButton.clicked.connect(self.selectPathBtnIsClicked)

    def selectPathBtnIsClicked(self):
        steam_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.steamprocess.set_steam_path(steam_path + "/Steam.exe")
        self.view.close()
