# coding=utf-8
from controllers.controller import Controller
from controllers.editacc_controller import EditaccController
from controllers.message_controller import MessageController
from views.choiceacc_view import ChoiceAccView
from utility.steamprocess import SteamProcess
from models.account_model import SAMAccountModel

from resourses import strings


class ChoiceaccController(Controller):
    def __init__(self, model):
        self.model = model
        self.view = ChoiceAccView(self.model)
        super(ChoiceaccController, self).__init__(self.view)
        self.steamprocess = SteamProcess()
        # Привязка кнопок к функциям
        self.view.ui.choiceAccButton.clicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.listView.doubleClicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.editAccButton.clicked.connect(self.EditBtnIsClicked)
        self.view.ui.deleteButton.clicked.connect(self.DeleteBtnIsClicked)
        # Запуск окна
        self.view.exec_()

    def take_data(self):
        return self.view.ui.listView.selectedIndexes()[0].data()

    def take_index(self):
        return self.view.ui.listView.selectedIndexes()[0].row()

    def ChoiceBtnIsClicked(self):
        self.steamprocess.login(self.take_data())
        self.view.close()

    def EditBtnIsClicked(self):
        editacc_controller = EditaccController(model=self.model,
                                               index=self.take_index(),
                                               data=self.take_data())

    def DeleteBtnIsClicked(self):
        confirm_message = strings.confirm_message
        message_controller = MessageController('confirm', confirm_message)
        btnvalue = message_controller.view.exec_()
        if btnvalue == 1:
            SAMAccountModel.delete_acc(self.take_data())
            self.model.removeRows(self.take_index())
