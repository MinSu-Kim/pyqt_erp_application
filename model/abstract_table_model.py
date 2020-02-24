from abc import ABCMeta, abstractmethod

from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QModelIndex


class AbstractTableModel(QAbstractTableModel):
    def __init__(self, data=None, header=None):
        super().__init__()
        self.data = data or [()]
        self.header = header or [()]

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    @abstractmethod
    def data(self, index, role):
        raise NotImplementedError("Subclass must implement abstract method")

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()

