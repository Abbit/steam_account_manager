from PyQt5 import QtCore


class AccountListModel(QtCore.QAbstractListModel):
    def __init__(self, accounts=[], parent=None):
        super(AccountListModel, self).__init__(parent)
        self.__accounts = accounts

    def rowCount(self, parent):
        return len(self.__accounts)

    def data(self, index, role):
        if role == QtCore.Qt.ToolTipRole:
            return self.__accounts[index.row()].description

        # if role == QtCore.Qt.DecorationRole:
        #     row = index.row()
        #     icon = QtGui.QIcon()
        #     if self.__accounts[row].steamlink is not "":
        #         icon.addFile(models.get_avatar(self.__accounts[row].steamlink))
        #     else:
        #         icon.addFile(models.get_default_avatar())

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.__accounts[row]
            return value.nickname

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # def insertRows(self, position, rows, item, parent=QtCore.QModelIndex()):
    #     self.beginInsertRows(parent, position, position + rows - 1)
    #
    #     for i in range(rows):
    #         self.__accounts.insert(position, item)
    #
    #     self.endInsertRows()
    #     return True

    def removeRows(self, position, rows=1, parent=QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            value = self.__accounts[position]
            self.__accounts.remove(value)

        self.endRemoveRows()
        return True
