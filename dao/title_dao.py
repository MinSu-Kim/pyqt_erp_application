import inspect

from mysql.connector import Error
from pymysql import IntegrityError

from dao.abs_dao import Dao
from dao.singleton_instance import SingleTonInstance
from dto.Title import Title


class TitleDao(Dao, SingleTonInstance):

    def insert_item(self, sql='insert into title values(%s, %s)', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return self.do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def update_item(self, sql='UPDATE title SET title_name=%s WHERE title_no=%s', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return self.do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def delete_item(self, sql='DELETE FROM title WHERE title_no=%s', **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return self.do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def select_item(self, sql="select title_no, title_name from title", **kargs):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, kargs, end=' => '))
        return self.do_query(query=sql, kargs=tuple([v for v in kargs.values()]))

    def get_dto(self, **args):
        # return tuple(v for k, v in args.items())
        return Title(**args)

        # return tuple(v for k, v in args.items())
        #return tuple(v for k, v in args.items())


if __name__ == "__main__":
    try:
        print(TitleDao.instance().select_item(
            sql='select title_no, title_name from title where title_no = %s and title_name = %s',
            **{'title_no': 1, 'title_name': '사장'}))
        # TitleDao.instance().insert_item(**{'title_no': 6, 'title_name': '인턴'})
        print(TitleDao.instance().select_item())
        TitleDao.instance().update_item(**{'title_name': '계약직', 'title_no': 6})
        print(TitleDao.instance().select_item())

        TitleDao.instance().delete_item(**{'title_no': 6})
        print(TitleDao.instance().select_item())
    except IntegrityError as e:
        print(e)
