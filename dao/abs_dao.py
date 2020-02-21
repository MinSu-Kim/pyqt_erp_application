from abc import ABCMeta, abstractmethod
from dbconnection.db_pool import DatabasePool


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def get_dto(**args):
    return tuple(v for k, v in args.items())


def do_query(**kwargs):
    with DatabasePool() as conn:
        cursor = conn.cursor()
        if 'select' in kwargs['query'].lower():
            if kwargs['kargs'] is not None:
                cursor.execute(kwargs['query'], kwargs['kargs'])
            else:
                cursor.execute(kwargs['query'])
            res = []
            [res.append(get_dto(**row)) for row in iter_row(cursor, 5)]
        else:
            if kwargs['kargs'] is not None:
                cursor.execute(kwargs['query'], kwargs['kargs'])
            else:
                cursor.execute(kwargs['query'])
            conn.commit()
            res = f"{cursor.rowcount} rows affected."
        return res


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

