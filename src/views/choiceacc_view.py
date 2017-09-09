from resourses import config
from views.view import View
from .ui.gen.choice_acc_dialog import Ui_Dialog


class ChoiceAccView(View):
    def __init__(self, model):
        self.ui = Ui_Dialog()
        super(ChoiceAccView, self).__init__(self.ui)
        self.model = model

        self.ui.listView.setModel(self.model)

        self.ui.listView.setIconSize(config.LISTVIEW_ITEM_ICON_SIZE)
        self.ui.listView.setSpacing(config.LISTVIEW_SPACING)
