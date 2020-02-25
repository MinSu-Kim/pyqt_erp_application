from dto.Department import Department
from dto.Title import Title


class Employee():
    def __init__(self, **kwargs):
        # emp_no, emp_name, title, manager, salary, dept, hire_date, gender, passwd, pic
        self.__emp_no = kwargs['emp_no'] if 'emp_no' in kwargs else None
        self.__emp_name = kwargs['emp_name'] if 'emp_name' in kwargs else None
        self.__title = kwargs['title'] if 'title' in kwargs else None
        self.__manager = kwargs['manager'] if 'manager' in kwargs else None
        self.__salary = int(kwargs['salary']) if 'salary' in kwargs else None
        self.__dept = kwargs['dept'] if 'dept' in kwargs else None
        self.__hire_date = kwargs['hire_date'] if 'hire_date' in kwargs else None
        self.__passwd = kwargs['passwd'] if 'passwd' in kwargs else None
        self.__gender = kwargs['gender'] if 'gender' in kwargs else None
        self.__pic = kwargs['pic'] if 'pic' in kwargs else None
        self.__len = kwargs.__len__()

    @property
    def emp_no(self):
        return self.__emp_no

    @emp_no.setter
    def emp_no(self, emp_no):
        self.__emp_no = emp_no
        self.__len += 1

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        self.__emp_name = emp_name
        self.__len += 1

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender
        self.__len += 1

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, dept):
        self.__dept = dept;
        self.__len += 1

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager):
        self.__manager = manager
        self.__len += 1

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = int(salary)
        self.__len += 1

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title
        self.__len += 1

    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self.__hire_date = hire_date
        self.__len += 1

    @property
    def passwd(self):
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd):
        self.__passwd = passwd
        self.__len += 1

    @property
    def pic(self):
        return self.__pic

    @pic.setter
    def pic(self, pic):
        self.__pic = pic
        self.__len += 1

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        # emp_no, emp_name, gender, dept, manager, salary, title, hire_date, password
        return (i for i in (self.__emp_no, self.__emp_name, self.__gender, self.__dept, self.__manager, self.__salary, self.__title, self.__hire_date, self.__pic, self.__passwd))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        str_format = '{}('
        for k in range(self.__len):
            str_format += '{!r},'
        if len(str_format) == 3:
            str_format += ')'
        else:
            str_format = str_format[:len(str_format) - 1] + ')'
        return str_format.format(class_name, *self)

    def __hash__(self):
        return hash(self.__emp_no) ^ hash(self.__emp_name)

    def get_to_dict(self):
        return {
            'emp_no': self.__emp_no,
            'emp_name': self.__emp_name,
            'gender': self.__gender,
            'dept': self.__dept,
            'manager': self.__manager,
            'salary': self.__salary,
            'title': self.__title,
            'hire_date': self.__hire_date,
            'pic': self.__pic,
            'passwd':self.__passwd
        }


if __name__ == "__main__":
    kargs = {'emp_no': 1, 'emp_name': '김민수', 'gender': True, 'dept': Department(dept_no=1),
             'manager': Employee(**{'emp_no': 1}),
             'salary': 1500000, 'title': Title(title_no=1), 'hire_date': '2020-02-18',
             'passwd':'1234'}
    [print(k, end=', ') for k, v in kargs.items()]
    empList = [Employee(**kargs), Employee(**kargs)]

    [print(e.get_to_dict()) for e in empList]

    print(empList[0] == empList[1])

    print(Employee(**{'emp_no': 1, 'emp_name': '김민수'}).get_to_dict())

    print(tuple(empList[1]))

