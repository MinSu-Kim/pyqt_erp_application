import inspect

from mysql.connector import Error
from pymysql import IntegrityError

from dao.abs_dao import Dao, do_query
from dao.singleton_instance import SingleTonInstance


class DepartmentDao(Dao, SingleTonInstance):

    def insert_item(self, sql='insert into department values(%s, %s, %s)', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def update_item(self, sql='update department set dept_name=%s, floor = %s WHERE dept_no=%s', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def delete_item(self, sql='delete from department WHERE dept_no=%s', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def select_item(self, sql="select dept_no, dept_name, floor from department", **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return do_query(query=sql, kargs=tuple([v for v in kargs.values()]))


if __name__ == "__main__":
    print('select dept_no, dept_name, floor from department where dept_no = %s'.format(1))
    try:
        print(DepartmentDao.instance().select_item(
            sql='select dept_no, dept_name, floor from department where dept_no = %s',
            **{'dept_no': 1}))
        DepartmentDao.instance().insert_item(**{'dept_no': 5, 'dept_name': '태스크포스', 'floor': 6})
        print(DepartmentDao.instance().select_item())
        DepartmentDao.instance().update_item(**{'dept_name': '마케팅', 'floor': 6, 'dept_no':5})
        print(DepartmentDao.instance().select_item())

        DepartmentDao.instance().delete_item(**{'dept_no': 5})
        print(DepartmentDao.instance().select_item())
    except IntegrityError as e:
        print(e)
