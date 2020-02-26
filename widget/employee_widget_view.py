import inspect
from builtins import print

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from content.emp_content_view import EmployeeContentWidget
from dao.employee_dao import EmployeeDao
from dto.Employee import Employee
from table_view.employee_table_view import EmployeeTableViewWidget


class EmployeeWidgetView(QWidget):
    def __init__(self):
        super().__init__()
        self.emp_item = EmployeeContentWidget()
        self.row_data = EmployeeDao.instance().select_item()
        self.table_view = EmployeeTableViewWidget(self.row_data)
        self.set_table_idx = None

        self.add_btn = QPushButton('추가')
        self.cancel_btn = QPushButton('취소')

        layout_insert = QHBoxLayout()
        layout_insert.addSpacerItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout_insert.addWidget(self.add_btn)
        layout_insert.addWidget(self.cancel_btn)
        layout_insert.setContentsMargins(10, 0, 10, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.emp_item)
        layout.addLayout(layout_insert)
        layout.addWidget(self.table_view)

        self.setLayout(layout)
        self.set_context_menu(self.table_view)
        self.add_btn.clicked.connect(self.add_item)
        self.cancel_btn.clicked.connect(self.clear_item)

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
            selected_item_index = self.table_view.get_selected_index()
            emp = self.row_data[selected_item_index]
            EmployeeDao.instance().delete_item(dto=emp)
            self.table_view.delete_item(selected_item_index)
            self.clear_item()
        except Exception as err:
            print(err)
            raise err

    def add_item(self):
        emp = self.emp_item.get_item()
        print(emp)
        if self.add_btn.text() == '추가':
            try:
                EmployeeDao.instance().insert_item(dto=emp)
                emp.pic= 1
                self.row_data.append(emp)
                self.table_view.add_item(emp)
                self.emp_item.clear_line_edit()
                self.row_data.append(emp)
            except Exception as err:
                print(err)
                raise err
        else:
            try:
                EmployeeDao.instance().update_item(dto=emp)
                emp.pic = 1
                self.table_view.update_item(self.set_table_idx, emp)

                self.add_btn.setText('추가')
                self.emp_item.clear_line_edit()
                for i, row in enumerate(self.row_data):
                    if row.emp_no == emp.emp_no:
                        self.row_data[i] = emp
            except Exception as err:
                print(err)
                raise err

    def update_item(self):
        try:
            print("\n______ {}() ______".format(inspect.stack()[0][3]))
            selected_item = self.table_view.get_selected_item()
            self.set_table_idx = self.table_view.get_selected_index()
            for e in self.row_data:
                if e.emp_no == selected_item[0]:
                    print(e)
                    emp = e
            print('update item', type(emp), emp)
            self.emp_item.set_item(emp)
            self.add_btn.setText('수정')
        except Exception as err:
            print(err)

    def clear_item(self):
        self.emp_item.clear_line_edit()
        self.add_btn.setText('추가')


if __name__ == '__main__':
    app = QApplication([])
    window = EmployeeWidgetView()
    window.show()
    app.exec()