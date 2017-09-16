# coding=utf-8
from views.view import View


class MessageView(View):
    def __init__(self, message_type):
        if message_type == 'confirm':
            from .ui.gen.ui_confirm_dialog import Ui_Dialog
            self.ui = Ui_Dialog()
        if message_type == 'error':
            from .ui.gen.ui_error_dialog import Ui_Dialog
            self.ui = Ui_Dialog()
        super(MessageView, self).__init__(self.ui)

    def set_message(self, message):
        self.ui.label.setText(message)
