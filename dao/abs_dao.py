import inspect
from abc import ABCMeta, abstractmethod

from mysql.connector import Error

from dbconnection.db_pool import DatabasePool


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


class Dao(metaclass=ABCMeta):

    @abstractmethod
    def insert_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def delete_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")

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
                [res.append(row) for row in iter_row(cursor, 5)]
                return res
