from abc import abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class AbstractTableViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        # self.ui = uic.loadUi('../ui/table_view.ui')
        self.tableView = QTableView()
        # create the view
        # self.tableView = self.ui.custom_table_view
        self.model = None

        # table view 설정
        self.set_table_view_config()
        layout = QGridLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    @abstractmethod
    def set_column_size(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def set_table_view_config(self):
        # header size
        self.set_column_size()

        self.tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색
        # Set the alignment to the headers
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        # 셀 내용 수정불가
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # hide grid
        self.tableView.setShowGrid(True)
        # row단위 선택
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 헤더의 내용을 tableView의 크기에 맞춤
        self.tableView.horizontalHeader().setStretchLastSection(True)
