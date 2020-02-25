from abc import ABCMeta, abstractmethod
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
    def insert_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def delete_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_dto(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    def do_query(self, **kwargs):
        print(kwargs)
        try:
            with DatabasePool() as conn:
                cursor = conn.cursor()
                if 'select' in kwargs['query'].lower():
                    if kwargs['kargs'] is not None:
                        cursor.execute(kwargs['query'], kwargs['kargs'])
                    else:
                        cursor.execute(kwargs['query'])
                    res = []
                    [res.append(self.get_dto(**row)) for row in iter_row(cursor, 5)]
                else:
                    if kwargs['kargs'] is not None:
                        cursor.execute(kwargs['query'], kwargs['kargs'])
                    else:
                        cursor.execute(kwargs['query'])
                    conn.commit()
                    res = f"{cursor.rowcount} rows affected."
                return res
        except Exception as err:
            print(err)