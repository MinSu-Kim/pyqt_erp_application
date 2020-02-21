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

        header = ['직책 코드', '직책 명']
        # tdao = TitleDao()
        # table_data = tdao.select_item()
        table_data = TitleDao.instance().select_item()
        self.model = TitleTableModel(data=table_data, header=header )
        self.tableView.setModel(self.model)

        self.ui.show()

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)