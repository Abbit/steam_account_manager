from views.view import View
from .ui.gen.error_dialog import Ui_Dialog


class ErrorView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(ErrorView, self).__init__(self.ui)

    def set_message(self, message):
        self.ui.label.setText(message)
