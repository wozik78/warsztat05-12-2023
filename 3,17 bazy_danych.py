import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("baza została podłaczonoa")

except sqlite3.Error as e:
    print("bład podczas połączenia bazy ",e)
finally:
    if sql_connection:
        sql_connection.close()
        print('baza została zamknięta')

