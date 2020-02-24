from PyQt5.QtCore import Qt, QSize, QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class EmployeeContentWidget(QWidget):
    def __init__(self):
        super().__init__()
        root_layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(root_layout)
        self.init_component(root_layout)

    def init_component(self, root_layout):
        item_size = QSize(150, 40)

        self.lbl_no = QLabel('사원 번호', self)
        self.lbl_no.setAlignment(Qt.AlignCenter)
        self.lbl_no.setMinimumSize(item_size)
        self.lbl_name = QLabel('사원명', self)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setMinimumSize(item_size)

        self.le_no = QLineEdit()
        self.le_no.setMinimumSize(item_size)
        self.le_name = QLineEdit()
        self.le_name.setMinimumSize(item_size)

        self.lbl_gender = QLabel('성별', self)
        self.lbl_gender.setAlignment(Qt.AlignCenter)
        self.lbl_gender.setMinimumSize(item_size)

        layout_gender = QHBoxLayout()
        self.rb_male = QRadioButton('남', self)
        self.rb_male.setChecked(True)
        # self.rb_male.setMinimumSize(item_size)
        layout_gender.addWidget(self.rb_male)

        self.rb_female = QRadioButton('여', self)
        # self.rb_female.setMinimumSize(item_size)
        layout_gender.addWidget(self.rb_female)

        btn_group = QButtonGroup()
        btn_group.addButton(self.rb_male)
        btn_group.addButton(self.rb_female)
        # layout_gender.setContentsMargins(10, 0, 10, 0)

        #직속상사
        self.lbl_manager = QLabel('직속 상사', self)
        self.lbl_manager.setAlignment(Qt.AlignCenter)
        self.lbl_manager.setMinimumSize(item_size)

        self.cb_manager = QComboBox(self)
        self.cb_manager.setMinimumSize(item_size)
        self.cb_manager.addItem('직속상사1')
        self.cb_manager.addItem('직속상사2')
        self.cb_manager.setCurrentIndex(-1)

        # 급여
        self.lbl_salary = QLabel('급여', self)
        self.lbl_salary.setAlignment(Qt.AlignCenter)
        self.lbl_salary.setMinimumSize(item_size)

        self.sp_salary = QSpinBox()
        self.sp_salary.setMinimumSize(item_size)
        self.sp_salary.setRange(1500000, 5000000)
        self.sp_salary.setSingleStep(100000)
        self.sp_salary.setGroupSeparatorShown(True);
        self.sp_salary.setAlignment(Qt.AlignRight)
        echo_group = QGroupBox('사원', self)

        #부서
        self.lbl_dept = QLabel('부서', self)
        self.lbl_dept.setAlignment(Qt.AlignCenter)
        self.lbl_dept.setMinimumSize(item_size)

        self.cb_dept = QComboBox(self)
        self.cb_dept.setMinimumSize(item_size)
        self.cb_dept.addItem('부서1')
        self.cb_dept.addItem('부서2')
        self.cb_dept.setCurrentIndex(-1)

        # 입사일
        self.lbl_hire_date = QLabel('입사일', self)
        self.lbl_hire_date.setAlignment(Qt.AlignCenter)
        self.lbl_hire_date.setMinimumSize(item_size)

        self.de_hire_date = QDateEdit(self)
        self.de_hire_date.setMinimumSize(item_size)
        self.de_hire_date.setDate(QDate.currentDate())
        self.de_hire_date.setMinimumDate(QDate(1900, 1, 1))
        self.de_hire_date.setMaximumDate(QDate(2100, 12, 31))
        self.de_hire_date.setDisplayFormat('yyyy-MM-dd')
        self.de_hire_date.setAlignment(Qt.AlignCenter)

        # 직책
        self.lbl_title = QLabel('직책', self)
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setMinimumSize(item_size)

        self.cb_title = QComboBox(self)
        self.cb_title.setMinimumSize(item_size)
        self.cb_title.addItem('직책1')
        self.cb_title.addItem('직책2')
        self.cb_title.setCurrentIndex(-1)

        #비밀번호
        self.lbl_pass1 = QLabel('비밀 번호', self)
        self.lbl_pass1.setAlignment(Qt.AlignCenter)
        self.lbl_pass1.setMinimumSize(item_size)

        self.le_pass1 = QLineEdit()
        self.le_pass1.setEchoMode(QLineEdit.Password)
        self.le_pass1.setMinimumSize(item_size)

        self.lbl_pass2 = QLabel('비밀 번호 확인', self)
        self.lbl_pass2.setAlignment(Qt.AlignCenter)
        self.lbl_pass2.setMinimumSize(item_size)
        self.le_pass2 = QLineEdit()
        self.le_pass2.setEchoMode(QLineEdit.Password)
        self.le_pass2.setMinimumSize(item_size)

        self.lbl_pass_confirm = QLabel('불일치', self)
        self.lbl_pass_confirm.setStyleSheet('color: red')
        self.lbl_pass_confirm.setAlignment(Qt.AlignCenter)
        self.lbl_pass_confirm.setMinimumSize(item_size)

        #사진
        self.pixmap = QPixmap('python.png')
        self.pixmap.scaledToHeight(275)
        lbl_img = QLabel()
        lbl_img.setMinimumSize(QSize(200, 275))
        lbl_img.setPixmap(self.pixmap)
        lbl_img.setAlignment(Qt.AlignCenter)
        lbl_img.setFrameShape(QFrame.Box)
        lbl_img.setFrameShadow(QFrame.Sunken)

        self.btn_pic = QPushButton('사진 추가')
        self.btn_pic.setMinimumSize(item_size)

        group_layout = QGridLayout()
        echo_group.setLayout(group_layout)
        group_layout.addWidget(self.lbl_no,           0, 0, 1, 1)
        group_layout.addWidget(self.le_no,            0, 1, 1, 1)
        group_layout.addWidget(self.lbl_name,         1, 0, 1, 1)
        group_layout.addWidget(self.le_name,          1, 1, 1, 1)
        group_layout.addWidget(self.lbl_salary,       2, 0, 1, 1)
        group_layout.addWidget(self.sp_salary,        2, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass1,        3, 0, 1, 1)
        group_layout.addWidget(self.le_pass1,         3, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass2,        4, 0, 1, 1)
        group_layout.addWidget(self.le_pass2,         4, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass_confirm, 5, 1, 1, 1)

        group_layout.addWidget(self.lbl_hire_date,    0, 2, 1, 1)
        group_layout.addWidget(self.de_hire_date,     0, 3, 1, 1)
        group_layout.addWidget(self.lbl_gender,       1, 2, 1, 1)
        group_layout.addLayout(layout_gender,         1, 3, 1, 1)
        group_layout.addWidget(self.lbl_manager,      2, 2, 1, 1)
        group_layout.addWidget(self.cb_manager,       2, 3, 1, 1)
        group_layout.addWidget(self.lbl_dept,         3, 2, 1, 1)
        group_layout.addWidget(self.cb_dept,          3, 3, 1, 1)
        group_layout.addWidget(self.lbl_title,        4, 2, 1, 1)
        group_layout.addWidget(self.cb_title,         4, 3, 1, 1)

        group_layout.addWidget(lbl_img,               0, 5, 4, 1)
        group_layout.addWidget(self.btn_pic,          4, 5, 1, 1)

        horizontalSpacer = QSpacerItem(150, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        group_layout.addItem(horizontalSpacer,          0, 4, 1, 1)

        root_layout.addWidget(echo_group)

"""
    def get_item(self):
        try:
            dept_no = self.le_no.text()
            dept_name = self.le_name.text()
            floor = self.le_floor.text()
            dept = Department(**{'dept_no': int(dept_no), 'dept_name': dept_name, 'floor':floor})
            print(dept)
            return dept;
        except Exception as err:
            print(err)

    def set_item(self, dept):
        self.le_no.setText(str(dept.dept_no))
        self.le_name.setText(dept.dept_name)
        self.le_floor.setText(str(dept.floor))

    def clear_line_edit(self):
        self.le_no.setText('')
        self.le_name.setText('')
        self.le_floor.setText('')
"""


if __name__ == '__main__':
    app = QApplication([])
    t = EmployeeContentWidget()
    t.show()
    app.exec()
