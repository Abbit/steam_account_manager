from PyQt5 import QtGui, QtWidgets

from controllers.controller import Controller
from models.account_model import SAMAccountModel
from models.sam_list_model import AccountListModel
from views.main_view import MainView
from controllers.choiceacc_controller import ChoiceaccController
from controllers.addacc_controller import AddaccController
from controllers.settings_controller import SettingsController

import resourses.images_rc


class MainController(Controller):
    def __init__(self):
        self.view = MainView()
        self.account_model = SAMAccountModel()
        # Создаём заставку до загрузки данных
        pixmap = QtGui.QPixmap(':images/splashscreen.jpg')
        splash = QtWidgets.QSplashScreen(pixmap)
        splash.show()
        # Загружаем данные
        self.model = AccountListModel(self.account_model.take_accs())
        super(MainController, self).__init__(self.view)
        # Заставка ичезнет при загрузке view
        splash.finish(self.view)
        # Привязка кнопок к функциям
        self.view.ui.choice_acc_btn.clicked.connect(self.choiceaccBtnIsClicked)
        self.view.ui.add_acc_btn.clicked.connect(self.addaccBtnIsClicked)
        self.view.ui.settings_btn.clicked.connect(self.settingsBtnIsClicked)

    def choiceaccBtnIsClicked(self):
        self.model.accounts = self.account_model.take_accs()
        choiceacc_controller = ChoiceaccController(self.model)

    def addaccBtnIsClicked(self):
        addacc_controller = AddaccController()

    def settingsBtnIsClicked(self):
        settings_controller = SettingsController()
