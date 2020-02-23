from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction

from dao.title_dao import TitleDao
from dto.Title import Title
from model.title_table_model import TitleTableModel
from table_view.abstract_table_view import AbstractTableViewWidget


class TitleTableViewWidget(AbstractTableViewWidget):
    def __init__(self):
        super().__init__()
        header = ['직책 코드', '직책 명']
        self.table_data = TitleDao.instance().select_item()
        self.model = TitleTableModel(data=self.table_data, header=header )
        self.tableView.setModel(self.model)

    def set_column_size(self):
        self.tableView.horizontalHeader().resizeSection(0, 40)
        self.tableView.horizontalHeader().resizeSection(1, 50)

    def get_delete_item(self, deleteIdx):
        del self.table_data[deleteIdx]
        self.model.removeRow(deleteIdx)
        self.model.layoutChanged.emit()

    def add_item(self, title):
        try:
            self.table_data.append(title.get_item_tuple())
            # self.model.data.append(title.get_item_tuple())
            self.model.insertRow(len(self.table_data)+1)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def get_selected_item(self):
        selected_index = self.tableView.selectedIndexes()[0]
        title = Title()
        title.title_no = self.table_data[selected_index.row()][0]
        title.title_name = self.table_data[selected_index.row()][1]
        return {'idx':selected_index.row(), 'item':title}

    def update_item(self, idx, title):
        try:
            self.table_data[idx] = title.get_item_tuple()
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = TitleTableViewWidget()
    t.show()
    app.exec()