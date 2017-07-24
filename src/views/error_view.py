from PyQt5 import QtWidgets
from .ui.gen.error_dialog import Ui_Dialog


class ErrorView(QtWidgets.QDialog):
    def __init__(self, message, parent=None):
        super(ErrorView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(message)
