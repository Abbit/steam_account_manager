from controllers.controller import Controller
from views.main_view import MainView
from controllers.choiceacc_controller import ChoiceaccController
from controllers.addacc_controller import AddaccController
from controllers.settings_controller import SettingsController


class MainController(Controller):
    def __init__(self, model):
        self.view = MainView()
        self.model = model
        super(MainController, self).__init__(self.view)
        # Привязка кнопок к функциям
        self.view.ui.choice_acc_btn.clicked.connect(self.choiceaccBtnIsClicked)
        self.view.ui.add_acc_btn.clicked.connect(self.addaccBtnIsClicked)
        self.view.ui.settings_btn.clicked.connect(self.settingsBtnIsClicked)
        # # Запуск окна
        # self.view.exec_()

    def choiceaccBtnIsClicked(self):
        choiceacc_controller = ChoiceaccController(self.model)

    def addaccBtnIsClicked(self):
        addacc_controller = AddaccController()

    def settingsBtnIsClicked(self):
        settings_controller = SettingsController()
