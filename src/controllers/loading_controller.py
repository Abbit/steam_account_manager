from controllers.controller import Controller
from models.account_model import SAMAccountModel
from models.sam_list_model import AccountListModel
from views.loading_view import LoadingView


class LoadingController(Controller):
    def __init__(self):
        self.view = LoadingView()
        super(LoadingController, self).__init__(self.view)
        account_model = SAMAccountModel()
        self.model = AccountListModel(account_model.take_accs())
        # Запуск окна
        self.view.exec_()

    def get_model(self):
        return self.model
