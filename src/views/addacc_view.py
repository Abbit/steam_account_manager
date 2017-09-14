from views.view import View
from .ui.gen.ui_addacc_dialog import Ui_Dialog


class AddAccView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(AddAccView, self).__init__(self.ui)
