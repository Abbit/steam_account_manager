from controllers.controller import Controller
from views.confirm_view import ConfirmView


class ConfirmController(Controller):
    def __init__(self, message):
        self.view = ConfirmView()
        super(ConfirmController, self).__init__(self.view)
        self.view.set_message(message)
        # Запуск окна
        self.view.exec_()
