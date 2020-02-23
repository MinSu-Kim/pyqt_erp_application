import json
import logging.config

from pymysqlpool.pool import Pool

# config = json.load(open('../log/logger.json'))
# logging.config.dictConfig(config)
# logger = logging.getLogger(__name__)


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
    """
        해당 코드는 working directory를 설정하여 절대경로를 고정시켜주는 역할을 합니다. 
        즉 해당 모듈을 어디에서 호출을 하든 절대경로를 해당 경로로 고정이 됩니다.
        import os
    
        print(os.get_exec_path(), os.getcwd())
        os.chdir(os.getcwd())
    """

    with DatabasePool() as conn:
        logger.info('%s conn', conn)
        print("conn", conn)
