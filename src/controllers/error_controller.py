from views.error_view import ErrorView


class SAMErrorController:
    def __init__(self, message):
        self.view = ErrorView(message)
        self.view.show()
