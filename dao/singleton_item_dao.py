import inspect

from mysql.connector import Error

from dao.abs_dao import get_dto, iter_row
from dao.singleton_instance import SingleTonInstance
from dbconnection.db_pool import DatabasePool


class ItemDao(SingleTonInstance):

    def insert_item(self, *query, title_no=None, title_name=None):
        print("\n{}()".format(inspect.stack()[0][3]), end=' => ')
        sql = "insert into title values(%s, %s)"
        args = (title_no, title_name)
        try:
            res = self.do_query(query=sql, kargs=args)
            print(res)
        except Error as err:
            raise err

    def update_item(self, title_no=None, title_name=None):
        print("\n{}()".format(inspect.stack()[0][3]), end=' => ')
        sql = "UPDATE title SET title_name=%s WHERE title_no=%s"
        args = (title_name, title_no)
        try:
            res = self.do_query(query=sql, kargs=args)
            print(res)
            return True
        except Error:
            return False

    def delete_item(self, title_no=None):
        print("\n{}()".format(inspect.stack()[0][3]), end=' => ')
        sql = "DELETE FROM title WHERE title_no=%s"
        args = (title_no,)
        try:
            res= self.do_query(query=sql, kargs=args)
            print(res)
            return True
        except Error:
            return False

    def select_item(self, *query):
        print("\n{}() => {}".format(inspect.stack()[0][3], query[0]))
        try:
            return self.do_query(query=query[0])
        except Error:
            return False

    def do_query(self, **kwargs):
        with DatabasePool() as conn:
            cursor = conn.cursor()
            if 'SELECT'.lower() not in kwargs['query'].lower():
                if kwargs['kargs'] is not None:
                    cursor.execute(kwargs['query'], kwargs['kargs'])
                else:
                    cursor.execute(kwargs['query'])
                conn.commit()
                affected = f"{cursor.rowcount} rows affected."
                return affected
            else:
                cursor.execute(kwargs['query'])
                res = []
                [res.append(get_dto(**row)) for row in iter_row(cursor, 5)]
                return res


if __name__ == "__main__":
    print(ItemDao.instance().select_item("select title_no, title_name from title"))
    print(ItemDao.instance().select_item("select dept_no, dept_name, floor from department"))
    print(ItemDao.instance().select_item("select emp_no, emp_name, gender, dept, manager, salary, title, hire_date from employee"))