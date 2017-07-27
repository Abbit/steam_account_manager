from views.main_view import MainView
from controllers.choiceacc_controller import SAMChoiceaccController
from controllers.addacc_controller import SAMAddaccController
from controllers.settings_controller import SAMSettingsController


class SAMMainController:
    def __init__(self):
       self.view = MainView()
       self.view.show()

       self.view.ui.choice_acc_btn.clicked.connect(self.choiceaccBtnIsClicked)
       self.view.ui.add_acc_btn.clicked.connect(self.addaccBtnIsClicked)
       self.view.ui.settings_btn.clicked.connect(self.settingsBtnIsClicked)

    def choiceaccBtnIsClicked(self):
        choiceacc_controller = SAMChoiceaccController()
        choiceacc_controller.view.exec_()

    def addaccBtnIsClicked(self):
        addacc_controller = SAMAddaccController()
        addacc_controller.view.exec_()

    def settingsBtnIsClicked(self):
        settings_controller = SAMSettingsController()
        settings_controller.view.exec_()
