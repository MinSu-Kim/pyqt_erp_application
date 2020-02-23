import inspect
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from content.title_content_view import TitleContentWidget
from dao.title_dao import TitleDao
from table_view.title_table_view import TitleTableViewWidget


class TitleWidgetView(QWidget):
    def __init__(self):
        super().__init__()
        self.title_item = TitleContentWidget()
        self.table_view = TitleTableViewWidget()
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
        copy_action = QAction("수정", tv)
        quit_action = QAction("삭제", tv)
        tv.addAction(copy_action)
        tv.addAction(quit_action)

        copy_action.triggered.connect(self.update_item)
        quit_action.triggered.connect(self.delete_item)

    def delete_item(self):
        try:
            selcted_item = self.table_view.get_selected_item()
            TitleDao.instance().delete_item(**{'title_no': selcted_item['item'].title_no})
            self.table_view.get_delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def add_item(self):
        title = self.title_item.get_title()
        if self.add_btn.text() == '추가':
            try:
                TitleDao.instance().insert_item(**title.get_item_dict())
                self.table_view.add_item(title)
                self.title_item.clear_line_edit()
            except Exception as err:
                raise err
        else:
            try:
                TitleDao.instance().update_item(**{'title_name':title.title_name, 'title_no':title.title_no})
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
        self.title_item.set_title(dict_title['item'])
        self.add_btn.setText('수정')

    def clear_item(self):
        self.title_item.clear_line_edit()


if __name__ == '__main__':
    app = QApplication([])
    window = TitleWidgetView()
    window.show()
    app.exec()

    # app = QApplication(sys.argv)
    # gallery = TitleWidgetView()
    # gallery.show()
    # sys.exit(app.exec_())