import sqlite3


class SQLLiteDBContextManager:
    def __int__(self,db_name):
        self.db_name=db_name
        self.conn = None

    #wykonuje sie przed naszym zadaniem

    def __enter__(self):
        self.conn = sqlite3.connect('sqlite_python.db')
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()



lista=[]

db_name= "my_database.db"


with SQLLiteDBContextManager(db_name) as conn:
    cursor=conn.cursor()
    cursor.execute("Create Table users(id integer primary key, name text)")
