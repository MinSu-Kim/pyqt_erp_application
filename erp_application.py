from PyQt5.QtWidgets import QApplication

from content.title_content_view import TitleContentWidget
from table_view.title_table_view import TitleTableViewWidget

if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    i = TitleContentWidget()
    t = TitleTableViewWidget()
    app.exec()

