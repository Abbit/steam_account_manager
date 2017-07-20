from PyQt5 import QtWidgets
from .ui.gen.addacc_dialog import Ui_Dialog

class AddAccView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AddAccView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)