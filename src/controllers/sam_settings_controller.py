from views.sam_settings_view import SettingsView
from PyQt5 import QtWidgets
from applogic.applogic import AppLogic


class SAMSettingsController:
    def __init__(self):
        self.applogic = AppLogic()
        self.view = SettingsView()
        self.view.show()

        self.view.ui.selectPathButton.clicked.connect(self.selectPathBtnIsClicked)

    def selectPathBtnIsClicked(self):
        steam_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.applogic.set_steam_path(steam_path + "/Steam.exe")
        self.view.close()
