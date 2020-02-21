from PyQt5.QtWidgets import QApplication

from dao.title_dao import TitleDao
from table_view.abstract_table_view import AbstractTableViewWidget
from table_view.department_table_view import DepartmentTableViewWidget
from table_view.title_table_view import TitleTableViewWidget

if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = TitleTableViewWidget()
    app.exec()

    # list = [{'title_no': 1, 'title_name': '사장'}, {'title_no': 2, 'title_name': '부장'}, {'title_no': 3, 'title_name': '과장'}, {'title_no': 4, 'title_name': '대리'}, {'title_no': 5, 'title_name': '사원'}]
    #
    # data = []
    # for row in list:
    #     print(row)
    #     list = []
    #     for k, v in row.items():
    #         list.append(v)
    #     data.append(tuple(list))
    #
    # print(data)
    # tdao = TitleDao()
    # tdao.delete_item(title_no=6)
    # tdao.select_item()
    # tdao.insert_item(6, '인턴')
    # tdao.select_item()
    # tdao.update_item(6, '계약직')
    # tdao.select_item()
    # tdao.delete_item(title_no=6)
    # tdao.select_item()
