from PyQt5 import QtWidgets
from .ui.gen.editacc_dialog import Ui_Dialog


class EditAccView(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EditAccView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login_lineEdit.setReadOnly(True)