from PyQt5.QtWidgets import QApplication

from dao.department_dao import DepartmentDao
from dto.Department import Department
from model.department_table_model import DepartmentTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class DepartmentTableViewWidget(AbstractTableViewWidget):
    def __init__(self):
        super().__init__()

        header = ['부서 번호', '부서명', '위치']
        self.table_data = [tuple(dept) for dept in DepartmentDao.instance().select_item()]
        # table에 data 로드
        self.model = DepartmentTableModel(data=self.table_data, header=header)
        self.tableView.setModel(self.model)

        # self.ui.setGeometry(300, 300, 600, 200) # 창의 좌표(x, y) 크기(width, height)

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)
        self.tableView.horizontalHeader().resizeSection(2, 30)

    def delete_item(self, delete_idx):
        try:
            del self.table_data[delete_idx]
            self.model.removeRow(delete_idx)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def add_item(self, dept):
        try:
            self.table_data.append(tuple(dept))
            self.model.insertRow(len(self.table_data)+1)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def get_selected_item(self):
        try:
            selected_row_index = self.tableView.selectedIndexes()[0].row()
            tuple_dept = self.table_data[selected_row_index] #tuple
            dept = Department()
            dept.dept_no = tuple_dept[0]
            dept.dept_name = tuple_dept[1]
            dept.floor = tuple_dept[2]
            return {'idx': selected_row_index, 'item': dept}
        except Exception as err:
            print(err)

    def update_item(self, idx, dept):
        try:
            self.table_data[idx] = tuple(dept)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)


if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = DepartmentTableViewWidget()
    t.show()
    app.exec()