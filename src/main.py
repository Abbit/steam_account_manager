import sys

import controller
from view.main_window import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Здесь прописываем событие нажатия на кнопку
        self.ui.choice_acc_btn.clicked.connect(controller.show_choice_acc_dialog)
        self.ui.new_acc_btn.clicked.connect(controller.show_create_acc_dialog)
        self.ui.settings_btn.clicked.connect(controller.show_setting_dialog)

if __name__ == "__main__":
    # create application
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('Steam Acc Manager')

    # create widget
    widget = MainWindow()
    widget.show()

    # execute application
    sys.exit(app.exec_())