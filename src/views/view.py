# coding=utf-8
from PyQt5 import QtWidgets


class View(QtWidgets.QDialog):
    def __init__(self, ui, parent=None):
        super(View, self).__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
