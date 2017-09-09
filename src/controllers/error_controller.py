from controllers.controller import Controller
from views.error_view import ErrorView


class ErrorController(Controller):
    def __init__(self, message):
        self.view = ErrorView()
        super(ErrorController, self).__init__(self.view)
        self.view.set_message(message)
        # Запуск окна
        self.view.exec_()

