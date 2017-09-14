from controllers.controller import Controller
from views.message_view import MessageView


class MessageController(Controller):
    def __init__(self, message_type, message):
        self.view = MessageView(message_type)
        super(MessageController, self).__init__(self.view)
        self.view.set_message(message)
        # Запуск окна
        if message_type != 'confirm':
            self.view.exec_()
