# coding=utf-8
from PyQt5 import QtCore

from views.view import View
from .ui.gen.ui_settings_dialog import Ui_Dialog


class SettingsView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(SettingsView, self).__init__(self.ui)

        self.setMaximumSize(QtCore.QSize(16777215, self.height()))
