from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView

from dao.title_dao import TitleDao
from model.abstract_table_model import AbstractTableModel
from model.title_table_model import TitleTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class TitleTableViewWidget(AbstractTableViewWidget):
    def __init__(self):
        super().__init__()

        # table_data = [(1,'사장'),(2, '부장')]
        header = ['직책 코드', '직책 명']
        tdao = TitleDao()
        list = tdao.select_item()

        table_data = []
        for row in list:
            list = [v for k, v in row.items()]
            table_data.append(tuple(list))

        self.model = TitleTableModel(data=table_data, header=header )
        self.tableView.setModel(self.model)

        self.ui.show()

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)