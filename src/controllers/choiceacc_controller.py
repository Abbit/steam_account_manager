from controllers.confirm_conroller import ConfirmController
from controllers.controller import Controller
from controllers.editacc_controller import EditaccController
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
        self.account_model = SAMAccountModel()
        # Привязка кнопок к функциям
        self.view.ui.choiceAccButton.clicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.listView.doubleClicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.editAccButton.clicked.connect(self.EditBtnIsClicked)
        self.view.ui.deleteButton.clicked.connect(self.DeleteBtnIsClicked)
        # Запуск окна
        self.view.exec_()

    def ChoiceBtnIsClicked(self):
        data = self.view.ui.listView.selectedIndexes()[0].data()
        self.steamprocess.login(data)
        self.view.close()

    def EditBtnIsClicked(self):
        qmodelindex = self.view.ui.listView.selectedIndexes()[0]
        index = qmodelindex.row()
        data = qmodelindex.data()
        editacc_controller = EditaccController(model=self.model,
                                               index=index,
                                               data=data)

    def DeleteBtnIsClicked(self):
        error_message = strings.confirm_message
        error_controller = ConfirmController(error_message)
        btnvalue = error_controller.view.exec_()
        if btnvalue == 1:
            qmodelindex = self.view.ui.listView.selectedIndexes()[0]
            index = qmodelindex.row()
            data = qmodelindex.data()
            self.account_model.delete_acc(data)
            self.model.removeRows(index)
        else:
            return
