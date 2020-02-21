import inspect

from mysql.connector import Error

from dao.abs_dao import Dao


class TitleDao(Dao):
    def __init__(self):
        super().__init__()

    def insert_item(self,  title_no=None, title_name=None):
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

    def select_item(self, **kargs):
        print("\n{}()".format(inspect.stack()[0][3]), end=' => ')
        sql = "select title_no, title_name from title"
        try:
            res = self.do_query(query=sql)
            print(res)
            return res
        except Error:
            return False



if __name__ == '__main__':
    tdao = TitleDao()
    tdao.select_item()

