import inspect

from dao.singleton_instance import SingleTonInstance
from dao.test_abs_dao import Test_Dao
from dto.Title import Title


class Test_TitleDao(Test_Dao, SingleTonInstance):
    def insert_item(self, sql='insert into title values(%s, %s)', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        return self.do_query(query=sql, kargs=tuple(dto))

    def update_item(self, sql='UPDATE title SET title_name=%s WHERE title_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.title_name, dto.title_no)
        return self.do_query(query=sql, kargs=t)

    def delete_item(self, sql='DELETE FROM title WHERE title_no=%s', dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.title_no,)
        return self.do_query(query=sql, kargs=t)

    def select_item(self, sql="select title_no, title_name from title", dto=None):
        print("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        if dto is not None:
            t = (dto.title_no,)
        return self.do_query(query=sql, kargs=t if dto is not None else None)

    def get_dto(self, **args):
        return Title(**args)


if __name__ == "__main__":
    print(Test_TitleDao.instance().select_item())
    t = Title()
    t.title_no = 6
    t.title_name = '인턴'
    print(t)

    Test_TitleDao.instance().insert_item(dto=t)
    print(Test_TitleDao.instance().select_item(sql="select title_no, title_name from title where title_no=%s", dto=t))
    print(Test_TitleDao.instance().select_item())
    Test_TitleDao.instance().update_item(dto=t)
    print(Test_TitleDao.instance().select_item())
    Test_TitleDao.instance().delete_item(dto=t)
    print(Test_TitleDao.instance().select_item())
