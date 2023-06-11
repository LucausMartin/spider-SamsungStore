import pymysql
# 封装增删改查
class Mysql(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = 'Lucaus260268mzx'
        self.db = 'spider'
        self.port = 3306
        self.charset = 'utf8'
        self.conn = None
        self.cursor = None

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    # 关闭数据库
    def close(self):
        self.conn.close()

    # 增删改
    def cud(self, sql, params):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
            self.conn.rollback()

    # 查
    def find(self, sql, params):
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)
            self.conn.rollback()                 