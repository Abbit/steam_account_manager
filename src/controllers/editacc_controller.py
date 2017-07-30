from controllers.error_controller import SAMErrorController
from views.editacc_view import EditAccView
from models.account_model import SAMAccountModel

from resourses import strings


class SAMEditaccController:
    def __init__(self, model, index, data):
        self.index = index
        self.data = data
        self.account_model = SAMAccountModel()
        self.model = model
        self.view = EditAccView()
        self.fillView()
        self.view.show()

        self.view.ui.buttonBox.clicked.connect(self.BtnIsClicked)
        self.view.ui.buttonBox.rejected.connect(self.cancelEdit)

    def BtnIsClicked(self):
        login = self.view.ui.login_lineEdit.text()
        newpassword = self.view.ui.passwrd_lineEdit.text()
        if newpassword is "":
            error_message = strings.password_error_message
            error_controller = SAMErrorController(error_message)
            error_controller.view.exec_()
            return -1
        newsteamlink = self.view.ui.steamlink_lineEdit.text()
        newdescription = self.view.ui.description_lineEdit.text()
        newaccount = SAMAccountModel(login=login,
                                     password=newpassword,
                                     steamlink=newsteamlink,
                                     description=newdescription)
        newaccount.delete_acc(login)
        self.model.removeRows(self.index)
        newaccount.add_acc()
        self.model.insertRows(self.index, newaccount)
        self.view.close()

    def cancelEdit(self):
        self.view.close()

    def fillView(self):
        acc = self.account_model.take_acc(self.data)
        self.view.ui.login_lineEdit.setText(acc.login)
        self.view.ui.passwrd_lineEdit.setText(acc.password)
        self.view.ui.steamlink_lineEdit.setText(acc.steamlink)
        self.view.ui.description_lineEdit.setText(acc.description)
