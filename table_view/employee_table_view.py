from PyQt5.QtWidgets import QApplication

from dao.employee_dao import EmployeeDao
from model.employee_table_model import EmployeeTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class EmployeeTableViewWidget(AbstractTableViewWidget):
    def __init__(self, row_data=None):
        super().__init__()
        # select emp_no, emp_name, title, manager, salary, dept, hire_date, gender from employee
        header = ['사원번호', '사원명', '성별', '부서', '직속상사', '급여', '직책', '입사일', '증명사진']
        self.table_data = [tuple(employee)[:-1] for employee in row_data]
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
        self.tableView.horizontalHeader().resizeSection(8, 50)

    def delete_item(self, delete_idx):
        try:
            del self.table_data[delete_idx]
            self.model.removeRow(delete_idx)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def add_item(self, emp):
        try:
            self.table_data.append(tuple(emp)[:-1])
            self.model.layoutChanged.emit()
            print('self.table_data', self.table_data, end='\n')
        except Exception as err:
            print(err)

    def get_selected_index(self):
        try:
            return self.tableView.selectedIndexes()[0].row()
        except Exception as err:
            print(err)

    def get_selected_item(self):
        selected_idx = self.get_selected_index()
        return self.table_data[selected_idx]

    def update_item(self, idx, emp):
        try:
            print('--------', idx, emp, self.table_data)
            self.table_data[idx] = tuple(emp)[:-1]
            print('--------', idx, emp, self.table_data)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = EmployeeTableViewWidget(row_data=EmployeeDao.instance().select_item())
    t.show()

    print("t.get_selected_item()", t.get_selected_index())
    app.exec()