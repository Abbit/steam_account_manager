# coding=utf-8
from views.view import View
from .ui.gen.ui_editacc_dialog import Ui_Dialog


class EditAccView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(EditAccView, self).__init__(self.ui)
        self.ui.login_lineEdit.setReadOnly(True)
