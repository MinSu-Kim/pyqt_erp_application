import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction

from dao.employee_dao import EmployeeDao
from dao.title_dao import TitleDao
from dto.Employee import Employee
from dto.Title import Title
from model.employee_table_model import EmployeeTableModel
from model.title_table_model import TitleTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class EmployeeTableViewWidget(AbstractTableViewWidget):
    def __init__(self):
        super().__init__()
        # select emp_no, emp_name, title, manager, salary, dept, hire_date, gender from employee
        header = ['사원번호', '사원명', '성별', '부서', '직속상사', '급여', '직책', '입사일']
        self.table_data = [tuple(employee) for employee in EmployeeDao.instance().select_item()]
        print(self.table_data)
        self.model = EmployeeTableModel(data=self.table_data, header=header )
        self.tableView.setModel(self.model)

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)
        self.tableView.horizontalHeader().resizeSection(2, 40)
        self.tableView.horizontalHeader().resizeSection(3, 50)
        self.tableView.horizontalHeader().resizeSection(4, 40)
        self.tableView.horizontalHeader().resizeSection(5, 50)
        self.tableView.horizontalHeader().resizeSection(6, 40)
        self.tableView.horizontalHeader().resizeSection(7, 50)

    def delete_item(self, delete_idx):
        try:
            del self.table_data[delete_idx]
            self.model.removeRow(delete_idx)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def add_item(self, title):
        try:
            self.table_data.append(tuple(title))
            self.model.insertRow(len(self.table_data)+1)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def get_selected_item(self):
        try:
            selected_row_index = self.tableView.selectedIndexes()[0].row()
            tuple_title = self.table_data[selected_row_index] #tuple
            emp = self.table_data[selected_row_index]
            # emp = Employee()
            # emp.title_no = tuple_title[0]
            # emp.title_name = tuple_title[1]
            return {'idx': selected_row_index, 'item': emp}
        except Exception as err:
            print(err)

    def update_item(self, idx, title):
        try:
            self.table_data[idx] = tuple(title)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = EmployeeTableViewWidget()
    t.show()

    print("t.get_selected_item()", t.get_selected_item())
    app.exec()