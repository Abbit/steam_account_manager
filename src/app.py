import sys
from PyQt5 import QtWidgets
from controllers.main_contoller import SAMMainController
from models.account_model import SAMAccountModel
from models.sam_list_model import AccountListModel


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        account_model = SAMAccountModel()
        model = AccountListModel(account_model.take_accs())
        self.controller = SAMMainController(model)


def exception_hook(type_, value, tb):
    logger.error('Unhandled top level exception:\n%s', ''.join(traceback.format_exception(type_, value, tb)))

if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = App(sys.argv)
    sys.exit(app.exec_())
