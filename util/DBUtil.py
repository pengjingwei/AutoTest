# 操作数据库工具类
import cx_Oracle

user = "frame14000"
password = "1"
database = "172.16.101.233:1521/SJZT_DATA_SHARE"


# 增,删,改
def updata(sql, param):
    con = cx_Oracle.connect(user, password, database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    con.commit()
    cursor.close()
    con.close()


# 查
def select(sql, param, model="all", size=1):
    con = cx_Oracle.connect(user, password, database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if model == "all":
        return cursor.fetchall()
    elif model == "one":
        return cursor.fetchone()
    elif model == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()
