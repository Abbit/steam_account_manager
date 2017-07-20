from views.sam_addacc_view import AddAccView
from applogic.applogic import AppLogic


class SAMAddaccController:
    def __init__(self):
        self.applogic = AppLogic()
        self.view = AddAccView()
        self.view.show()

        self.view.ui.pushButton.clicked.connect(self.BtnIsClicked)

    def BtnIsClicked(self):
        # self.applogic.add_acc(self.views.ui.login_lineEdit.text(),
        #                       self.views.ui.passwrd_lineEdit.text(),
        #                       self.views.ui.steamlink_lineEdit.text())
        self.view.close()