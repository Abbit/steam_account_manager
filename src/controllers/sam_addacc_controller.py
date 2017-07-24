from controllers.error_controller import SAMErrorController
from views.sam_addacc_view import AddAccView
from models.sam_account_model import SAMAccountModel

from resourses import strings


class SAMAddaccController:
    def __init__(self):
        self.view = AddAccView()
        self.view.show()

        self.view.ui.pushButton.clicked.connect(self.BtnIsClicked)

    def BtnIsClicked(self):
        login = self.view.ui.login_lineEdit.text()
        password = self.view.ui.passwrd_lineEdit.text()
        if (login is "") or (password is ""):
            error_message = strings.login_error_message
            error_controller = SAMErrorController(error_message)
            error_controller.view.exec_()
            return -1
        steamlink = self.view.ui.steamlink_lineEdit.text()
        description = self.view.ui.description_lineEdit.text()
        account_model = SAMAccountModel(login=login,
                                        password=password,
                                        steamlink=steamlink,
                                        description=description)
        account_model.add_acc()
        self.view.close()
