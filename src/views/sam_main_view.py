from PyQt5 import QtWidgets
from .ui.gen.main_window import Ui_MainWindow


class MainView(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
