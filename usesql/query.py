from sqlite3 import SQLITE_SAVEPOINT
import pymysql

connect_db = pymysql.connect(host = 'localhost', port = 3306, user = 'teddy', password = '*Zfgcj9l', charset = 'utf8', database = 'teddy')

#查詢資料
#sql_query = """
#SELECT 欄位1,欄位2,欄位3... FROM 資料表名稱 WHERE 條件式
#"""
def name_query(name):
        sql_query = f"""SELECT * FROM highercloud where name="{name}";
        """
        connect_db.ping() #重新連接的意思
        with connect_db.cursor() as cursor:
            #創建資料表
            #sql = sql_create
            #sql = sql_add
            sql = sql_query
            #sql = sql_update
            #sql = sql_delete
            #sql = sql_drop
            cursor.execute(sql)
        
            connect_db.commit()

            data = cursor.fetchall() #取得全部的資料
        connect_db.close()
        return data

def data_apply(name,age):
    sql_add = f"""INSERT INTO highercloud (NAME,AGE) VALUES ("{name}",{age})
    """
    connect_db.ping() #重新連接的意思
    with connect_db.cursor() as cursor:
        #創建資料表
        #sql = sql_create
        #sql = sql_add
        sql = sql_add
        #sql = sql_update
        #sql = sql_delete
        #sql = sql_drop
        cursor.execute(sql)
        connect_db.commit()
        connect_db.close()
    return "創建成功"

print(data_apply("Ted",25))

