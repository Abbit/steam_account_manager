# coding=utf-8
from views.view import View
from .ui.gen.ui_main_window import Ui_Dialog


class MainView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(MainView, self).__init__(self.ui)
