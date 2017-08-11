from controllers.confirm_conroller import SAMConfirmController
from controllers.editacc_controller import SAMEditaccController
from views.choiceacc_view import ChoiceAccView
from utility.steamprocess import SteamProcess
from models.account_model import SAMAccountModel

from resourses import strings


class SAMChoiceaccController:
    def __init__(self, model):
        self.steamprocess = SteamProcess()
        self.account_model = SAMAccountModel()
        self.model = model
        self.view = ChoiceAccView(self.model)
        self.view.show()

        self.view.ui.choiceAccButton.clicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.listView.doubleClicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.editAccButton.clicked.connect(self.EditBtnIsClicked)
        self.view.ui.deleteButton.clicked.connect(self.DeleteBtnIsClicked)

    def ChoiceBtnIsClicked(self):
        data = self.view.ui.listView.selectedIndexes()[0].data()
        self.steamprocess.login(data)
        self.view.close()

    def EditBtnIsClicked(self):
        qmodelindex = self.view.ui.listView.selectedIndexes()[0]
        index = qmodelindex.row()
        data = qmodelindex.data()
        editacc_controller = SAMEditaccController(model=self.model,
                                                  index=index,
                                                  data=data)
        editacc_controller.view.exec_()

    def DeleteBtnIsClicked(self):
        error_message = strings.confirm_message
        error_controller = SAMConfirmController(error_message)
        btnvalue = error_controller.view.exec_()
        if btnvalue == 1:
            qmodelindex = self.view.ui.listView.selectedIndexes()[0]
            index = qmodelindex.row()
            data = qmodelindex.data()
            self.account_model.delete_acc(data)
            self.model.removeRows(index)
        else:
            return
