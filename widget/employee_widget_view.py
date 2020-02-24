import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from content.emp_content_view import EmployeeContentWidget
from dao.employee_dao import EmployeeDao
from table_view.employee_table_view import EmployeeTableViewWidget


class EmployeeWidgetView(QWidget):
    def __init__(self):
        super().__init__()
        self.title_item = EmployeeContentWidget()
        self.table_view = EmployeeTableViewWidget()
        self.set_table_idx = None

        self.add_btn = QPushButton('추가')
        self.cancel_btn = QPushButton('취소')

        layout_insert = QHBoxLayout()
        layout_insert.addSpacerItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout_insert.addWidget(self.add_btn)
        layout_insert.addWidget(self.cancel_btn)
        layout_insert.setContentsMargins(10, 0, 10, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.title_item)
        layout.addLayout(layout_insert)
        layout.addWidget(self.table_view)

        self.setLayout(layout)
        self.set_context_menu(self.table_view)
        self.add_btn.clicked.connect(self.add_item)
        self.cancel_btn.clicked.connect(self.clear_item)
        # self.show()

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)

        update_action.triggered.connect(self.update_item)
        delete_action.triggered.connect(self.delete_item)

    def delete_item(self):
        try:
            selcted_item = self.table_view.get_selected_item() # {'idx':selected_index.row(), 'item':title}
            EmployeeDao.instance().delete_item(dto=selcted_item['item'])
            self.table_view.delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def add_item(self):
        title = self.title_item.get_item()
        if self.add_btn.text() == '추가':
            try:
                EmployeeDao.instance().insert_item(dto=title)
                self.table_view.add_item(title)
                self.title_item.clear_line_edit()
            except Exception as err:
                raise err
        else:
            try:
                EmployeeDao.instance().update_item(dto=title)
                self.table_view.update_item(self.set_table_idx, title)
                self.add_btn.setText('추가')
                self.title_item.clear_line_edit()
            except Exception as err:
                raise err

    def update_item(self):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        dict_title = self.table_view.get_selected_item()
        self.set_table_idx = dict_title['idx']
        print(dict_title['item'])
        self.title_item.set_item(dict_title['item'])
        self.add_btn.setText('수정')

    def clear_item(self):
        self.title_item.clear_line_edit()


if __name__ == '__main__':
    app = QApplication([])
    window = EmployeeWidgetView()
    window.show()
    app.exec()