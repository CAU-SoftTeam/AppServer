import pymysql
from config import get_config
import socket


class Database:
    def __init__(self):
        self.configs = get_config()
        self.config = {}
        self.config['MYSQL_DATABASE_USER'] = self.configs.database_user
        self.config['MYSQL_DATABASE_PASSWORD'] = self.configs.database_password
        self.config['MYSQL_DATABASE_DB'] = self.configs.database
        self.config['MYSQL_DATABASE_HOST'] = str(socket.gethostbyname(socket.gethostname()))
        self.config['MYSQL_DATABASE_CHARSET'] = self.configs.charset

    def get_connection(self):
        return pymysql.connect(host=self.config['MYSQL_DATABASE_HOST'], user=self.config['MYSQL_DATABASE_USER']
                               , password=self.config['MYSQL_DATABASE_PASSWORD'], db=self.config['MYSQL_DATABASE_DB']
                               , charset=self.config['MYSQL_DATABASE_CHARSET'])

    def set_scheduler(self):
        try:
            with self.getConnection() as conn:
                curs = conn.cursor()
                sql = """
                        """
                curs.execute(sql)
                conn.commit()
        except:
            pass
