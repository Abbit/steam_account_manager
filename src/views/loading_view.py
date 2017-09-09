from PyQt5 import QtCore

from views.view import View
from .ui.gen.loading_dialog import Ui_Dialog


class LoadingView(View):
    def __init__(self):
        self.ui = Ui_Dialog()
        super(LoadingView, self).__init__(self.ui)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
