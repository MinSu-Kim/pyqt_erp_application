from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt

from model.abstract_table_model import AbstractTableModel


class EmployeeTableModel(AbstractTableModel):
    # select emp_no, emp_name, title, manager, salary, dept, hire_date, gender from employee
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.TextAlignmentRole:
            if index.column() in [0, 1, 2, 3, 4, 6, 7, 8]:
                return Qt.AlignCenter
            if index.column() in [5]:
                return Qt.AlignVCenter | Qt.AlignRight
        if role != Qt.DisplayRole:
            return QVariant()
        if role == Qt.DisplayRole :
            if index.column() == 2:
                return '여' if self.data[index.row()][index.column()] == 0 else '남'
            if index.column() == 5:
                return format(self.data[index.row()][index.column()], ',')
            if index.column() == 7:
                return self.data[index.row()][index.column()].strftime("%Y-%m-%d")
            if index.column() == 8:
                return '있음' if self.data[index.row()][index.column()] == 1 else '없음'
            else:
                return self.data[index.row()][index.column()]