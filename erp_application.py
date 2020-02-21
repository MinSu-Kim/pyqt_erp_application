from PyQt5.QtWidgets import QApplication

from table_view.title_table_view import TitleTableViewWidget

if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = TitleTableViewWidget()
    app.exec()

