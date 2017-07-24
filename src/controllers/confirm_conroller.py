from views.confirm_view import ConfirmView


class SAMConfirmController:
    def __init__(self, message):
        self.view = ConfirmView(message)
        self.view.show()
