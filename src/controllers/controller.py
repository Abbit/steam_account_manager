# coding=utf-8
class Controller(object):
    def __init__(self, view):
        self.view = view
        self.view.show()
