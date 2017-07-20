from views.sam_choiceacc_view import ChoiceAccView
from models.sam_list_model import AccountListModel
from applogic.applogic import AppLogic
from models.sam_account_model import SAMAccountModel


class SAMChoiceaccController:
    def __init__(self):
        self.applogic = AppLogic()
        self.model = AccountListModel(self.takeAccs())
        self.view = ChoiceAccView(self.model)
        self.view.show()

        self.fillView()

        self.view.ui.choiceAccButton.clicked.connect(self.ChoiceBtnIsClicked)
        self.view.ui.deleteButton.clicked.connect(self.DeleteBtnIsClicked)

    def ChoiceBtnIsClicked(self):
        pass

    def DeleteBtnIsClicked(self):
        pass

    def fillView(self):
        pass

    def takeAccs(self):
        sam_accounts = []
        accs = self.applogic.read_accs()
        for acc in accs:
            login = accs[acc]['login']
            password = accs[acc]['password']
            nickname = acc
            sam_account = SAMAccountModel(login, password, nickname=nickname)
            sam_accounts.append(sam_account)
        return sam_accounts