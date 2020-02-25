import imghdr
import inspect
import os

from pymysql import IntegrityError

from dao.abs_dao import Dao
from dao.singleton_instance import SingleTonInstance
from dto.Department import Department
from dto.Employee import Employee
from dto.Title import Title


class EmployeeDao(Dao, SingleTonInstance):

    def insert_item(self, sql='insert into employee(emp_no, emp_name, gender, dept, manager, salary, title, hire_date, pic, pass) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, password(%s))', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        print(dto.get_to_dict())
        print(dto)
        return self.do_query(query=sql, kargs=tuple(dto))

    def update_item(self, sql='UPDATE employee SET emp_name=%s, gender=%s, dept=%s, manager=%s, salary=%s, title=%s, hire_date=%s, pass=password(%s), pic=%s WHERE emp_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = dto.emp_name, dto.gender, dto.dept, dto.manager, dto.salary, dto.title, dto.hire_date, dto.passwd, dto.pic, dto.emp_no
        return self.do_query(query=sql, kargs=t)

    def delete_item(self, sql='delete from employee where emp_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.emp_no,)
        return self.do_query(query=sql, kargs=t)

    def select_item(self, sql='select emp_no, emp_name, title, manager, salary, dept, hire_date, gender, if (pic is not null, 1, 0) as pic from employee', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        if dto is not None:
            if isinstance(dto, Employee):
                t = (dto.emp_no,)
            if isinstance(dto, Department):
                t = (dto.dept_no,)
        return self.do_query(query=sql, kargs=t if dto is not None else None)

    def select_pic_by_empno(self, sql='select pic from employee where emp_no = %s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.emp_no,)
        return self.do_query(query=sql, kargs=t)

    def get_dto(self, **args):
        print('get_dto ', args)
        return Employee(**args)


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def __write_file(self, data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    file_ext = imghdr.what(filename)
    os.rename(filename, filename+'.'+file_ext)
    return str(filename+'.'+file_ext)


if __name__ == "__main__":
    try:
        emp = Employee()
        emp.emp_no = 1003
        res = EmployeeDao.instance().select_pic_by_empno(dto=emp)
        print(type(res), res)
    except IntegrityError as e:
        print(e)
"""
    try:
        print(EmployeeDao.instance().select_item())

        emp = Employee()
        emp.emp_no = 1004
        emp.emp_name = '서현진'
        emp.gender = False
        emp.dept = Department(**{'dept_no': 1})
        emp.manager = Employee(**{'emp_no': 4377})
        emp.salary = 4000000
        emp.title = Title(**{'title_no':2})
        emp.hire_date = '2000-02-11'
        emp.passwd = '1234'
        # emp_no, emp_name, gender, dept, manager, salary, title, hire_date, pass
        EmployeeDao.instance().insert_item(dto=emp)
        print(EmployeeDao.instance().select_item())

        f = '../images/1003.jpeg'
        data = read_file(os.path.abspath(f))
        img_file = os.path.basename(f).split('.')[0]
        print('__load_img----------------', data, img_file)

        emp.pic = data
        EmployeeDao.instance().update_img(dto=emp)
        print(EmployeeDao.instance().select_item())

        emp.emp_name = '수지'
        emp.gender = False
        emp.dept = Department(**{'dept_no': 3})
        emp.manager = Employee(**{'emp_no': 1003})
        emp.salary = 2000000
        emp.title = Title(**{'title_no': 3})
        emp.hire_date = '2001-02-11'
        emp.passwd = '2222'
        EmployeeDao.instance().update_item(dto=emp)
        print(EmployeeDao.instance().select_item())

        print(EmployeeDao.instance().delete_item(dto=emp))
        print(EmployeeDao.instance().select_item())
    except IntegrityError as e:
        print(e)
"""