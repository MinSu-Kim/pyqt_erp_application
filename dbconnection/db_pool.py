from pymysqlpool.pool import Pool


class DatabasePool(object):
    def __init__(self):
        self.__cnxPool = Pool(host='localhost', port=3306, user='user_pyqt_erp', password='rootroot', db='pyqt_erp')
        self.__cnxPool.init()

    def __enter__(self):
        self.conn = self.__cnxPool.get_conn()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cnxPool.release(self.conn)


if __name__ == "__main__":

    with DatabasePool() as conn:
        print("conn", conn)