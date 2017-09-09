from controllers.controller import Controller
from controllers.error_controller import ErrorController
from views.addacc_view import AddAccView
from models.account_model import SAMAccountModel

from resourses import strings


class AddaccController(Controller):
    def __init__(self):
        self.view = AddAccView()
        super(AddaccController, self).__init__(self.view)
        # Привязка кнопок к функциям
        self.view.ui.pushButton.clicked.connect(self.BtnIsClicked)
        # Запуск окна
        self.view.exec_()

    def BtnIsClicked(self):
        login = self.view.ui.login_lineEdit.text()
        password = self.view.ui.passwrd_lineEdit.text()
        if (login is "") or (password is ""):
            error_message = strings.login_error_message
            error_controller = ErrorController(error_message)
            return -1
        steamlink = self.view.ui.steamlink_lineEdit.text()
        description = self.view.ui.description_lineEdit.text()
        account_model = SAMAccountModel()
        account_model.create_new_acc(login=login,
                                     password=password,
                                     steamlink=steamlink,
                                     description=description)
        self.view.close()
