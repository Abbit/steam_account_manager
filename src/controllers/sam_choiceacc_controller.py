from controllers.confirm_conroller import SAMConfirmController
from views.sam_choiceacc_view import ChoiceAccView
from models.sam_list_model import AccountListModel
from applogic.applogic import AppLogic
from models.sam_account_model import SAMAccountModel

from resourses import strings


class SAMChoiceaccController:
    def __init__(self):
        self.applogic = AppLogic()
        self.account_model = SAMAccountModel()
        self.model = AccountListModel(self.account_model.take_accs())
        self.view = ChoiceAccView(self.model)
        self.view.show()

        self.view.ui.choiceAccButton.clicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.listView.doubleClicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.deleteButton.clicked.connect(self.DeleteBtnIsClicked)

    def ChoiceBtnIsClicked(self):
        data = self.view.ui.listView.selectedIndexes()[0].data()
        self.applogic.login(data)
        self.view.close()

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
