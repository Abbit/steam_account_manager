from PyQt5 import QtWidgets
from .ui.gen.choice_acc_dialog import Ui_Dialog


class ChoiceAccView(QtWidgets.QDialog):
    def __init__(self, model,  parent=None):
        self.model = model
        super(ChoiceAccView, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listView.setModel(self.model)
