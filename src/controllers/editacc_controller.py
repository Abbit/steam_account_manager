# coding=utf-8
from controllers.controller import Controller
from controllers.message_controller import MessageController
from views.editacc_view import EditAccView
from models.account_model import SAMAccountModel

from resourses import strings


class EditaccController(Controller):
    def __init__(self, model, index, data):
        self.view = EditAccView()
        super(EditaccController, self).__init__(self.view)
        self.index = index
        self.data = data
        self.model = model
        self.fillView()
        # Привязка кнопок к функциям
        self.view.ui.buttonBox.clicked.connect(self.BtnIsClicked)
        self.view.ui.buttonBox.rejected.connect(self.cancelEdit)
        # Запуск окна
        self.view.exec_()

    def BtnIsClicked(self):
        login = self.view.ui.login_lineEdit.text()
        newpassword = self.view.ui.passwrd_lineEdit.text()
        if newpassword is "":
            error_message = strings.password_error_message
            message_controller = MessageController('error', error_message)
            return -1
        newsteamlink = self.view.ui.steamlink_lineEdit.text()
        newdescription = self.view.ui.description_lineEdit.text()
        SAMAccountModel.delete_acc(login)
        self.model.removeRows(self.index)
        newaccount = SAMAccountModel.create_new_acc(login=login,
                                                    password=newpassword,
                                                    steamlink=newsteamlink,
                                                    description=newdescription)
        self.model.insertRows(self.index, newaccount)
        self.view.close()

    def cancelEdit(self):
        self.view.close()

    def fillView(self):
        acc = SAMAccountModel.take_acc(self.data)
        self.view.ui.login_lineEdit.setText(acc.login)
        self.view.ui.passwrd_lineEdit.setText(acc.password)
        self.view.ui.steamlink_lineEdit.setText(acc.steamlink)
        self.view.ui.description_lineEdit.setText(acc.description)
