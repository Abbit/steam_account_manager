from PyQt5 import QtWidgets
from .ui.gen.confirm_dialog import Ui_Dialog


class ConfirmView(QtWidgets.QDialog):
    def __init__(self, message, parent=None):
        super(ConfirmView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText(message)
