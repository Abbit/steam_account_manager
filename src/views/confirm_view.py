from PyQt5 import QtWidgets

from views.view import View
from .ui.gen.confirm_dialog import Ui_Dialog


class ConfirmView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(ConfirmView, self).__init__(self.ui)

    def set_message(self, message):
        self.ui.label.setText(message)
