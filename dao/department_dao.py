import inspect

from mysql.connector import Error
from pymysql import IntegrityError

from dao.abs_dao import Dao
from dao.singleton_instance import SingleTonInstance
from dto.Department import Department


class DepartmentDao(Dao, SingleTonInstance):

    def insert_item(self, sql='insert into department values(%s, %s, %s)', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        return self.do_query(query=sql, kargs=tuple(dto))

    def update_item(self, sql='update department set dept_name=%s, floor = %s WHERE dept_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = dto.dept_name, dto.floor, dto.dept_no
        return self.do_query(query=sql, kargs=t)

    def delete_item(self, sql='delete from department WHERE dept_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.dept_no,)
        return self.do_query(query=sql, kargs=t)

    def select_item(self, sql="select dept_no, dept_name, floor from department", dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        if dto is not None:
            t = (dto.dept_no,)
        return self.do_query(query=sql, kargs=t if dto is not None else None)

    def get_dto(self, **args):
        return Department(**args)

if __name__ == "__main__":
    try:
        print(DepartmentDao.instance().select_item(
            sql='select dept_no, dept_name, floor from department where dept_no = %s',
            dto=Department(**{'dept_no': 1})))
        DepartmentDao.instance().insert_item(dto=Department(**{'dept_no': 5, 'dept_name': '태스크포스', 'floor': 6}))
        print(DepartmentDao.instance().select_item())
        DepartmentDao.instance().update_item(dto=Department(**{'dept_name': '마케팅', 'floor': 6, 'dept_no':5}))
        print(DepartmentDao.instance().select_item())

        DepartmentDao.instance().delete_item(dto=Department(**{'dept_no': 5}))
        print(DepartmentDao.instance().select_item())
    except IntegrityError as e:
        print(e)

