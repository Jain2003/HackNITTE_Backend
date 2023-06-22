import sqlite3
import hashlib

adminPassword = "root"
salt = "huh"
execution_key = "abcd"
#to change to env variables


def connect():
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        print("DataBase Connected")
    except:
        print("Database Error")
        return None,None
    return cursor, con


def createTables():

    cursor, con = connect()
    if cursor == None or con == None:
        return 0
    cursor.execute("create table if not exists admin(username varchar, password varchar)")
    con.commit()
    print("Tables are created")
    cursor.execute("select name from sqlite_master where type = 'table'")
    print("Tables")
    for i in cursor:
        print(i[0])
    cursor.execute("select * from admin")
    for i in cursor:
        print(i,"asdfsdf")
    cursor.execute("select * from admin where username = 'admin' ")
    flag = 0
    for i in cursor:
        flag = 1
    if flag == 0:
        password = hashlib.md5((adminPassword + salt).encode())
        cursor.execute(f"insert into admin values('admin','{password.hexdigest()}')")
        con.commit()
    con.close()


def authenticate_admin(username,password):
    cursor, con = connect()
    if cursor is None or con is None:
        return 0

    password = hashlib.md5((password + salt).encode()).hexdigest()
    cursor.execute("select * from admin")
    flag = 0
    for i in cursor:
        if i[0] == username and i[1] == password:
            flag = 1
        break
    if flag:
        return True
    else:
        return False
    con.close()

def run_query(query,key):
    if key != execution_key:
        return "Invalid Key"

    cursor, con = connect()
    if cursor is None or con is None:
        return "DataBase Error"

    try:
        cursor.execute(query)
        con.commit()
    except:
        return "Invalid Query"
    result = []
    for i in cursor:
        result.append(i)

    con.close()
    return str(result)
