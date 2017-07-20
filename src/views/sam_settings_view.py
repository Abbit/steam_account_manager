from PyQt5 import QtWidgets
from .ui.gen.settings_dialog import Ui_Dialog


class SettingsView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SettingsView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
