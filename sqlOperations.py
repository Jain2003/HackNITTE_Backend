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
    cursor.execute("create table if not exists contest(name varchar, desc varchar, input varchar, output varchar, sample varchar)")
    con.commit()
    cursor.execute("create table if not exists contestDetails(name varchar, start varchar, id varchar)")
    con.commit()
    cursor.execute("create table if not exists user(name varchar, email varchar, rollno varchar, password varchar, codechef varchar, codeforces varchar, leetcode varchar, rcc varchar, rcf varchar, rlc varchar)")
    con.commit()
    cursor.execute("create table if not exists announcement(announcement varchar)")
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


def get_native_contests():
    cursor,con = connect()
    if con is None or cursor is None:
        return 0
    cursor.execute("select * from contest")
    temp = []
    for i in cursor:
        temp.append(i)
    Result = {}
    ind = 0
    for i in range(len(temp)):
        Result[chr(ord('A')+i)] = temp[i]
    return Result


def get_native_contest_details():
    cursor, con = connect()
    if con is None or cursor is None:
        return 0
    cursor.execute("select  * from contestDetails")
    result = []
    for i in cursor:
        result.append(i)
        break
    return result

def regiter_user(data):
    cursor, con = connect()
    if con is None or cursor is None:
        return 0
    cursor.execute(f"select * from user where name = '{data[0]}'")
    flag = 0
    for i in cursor:
        flag = 1
        break
    if flag:
        return False
    # try:
    data[3] = hashlib.md5((data[3] + salt).encode()).hexdigest()
    cursor.execute(f"insert into user values('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{data[6]}','{data[7]}','{data[8]}','{data[9]}')")
    con.commit()
    return True
    # except:
    #     return False

def login_user(username,password):
    cursor, con = connect()
    if con is None or cursor is None:
        return 0
    cursor.execute(f"select password from user where name = '{username}'")
    passc = None
    for i in cursor:
        passc = i
        break
    if passc == None:
        return False
    hashed = hashlib.md5((password + salt).encode()).hexdigest()
    if hashed == passc[0]:
        return True
    else:
        return False

def get_user_details(name):
    cursor, con = connect()
    if con is None or cursor is None:
        return 0

    cursor.execute(f"select * from user where name = '{name}' ")

    for i in cursor:
        res = [i[0],i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[9]]
        break
    return res

def get_all_user_details():
    cursor, con = connect()
    if con is None or cursor is None:
        return 0

    cursor.execute('select name,rcc,rcf,rlc,rollno from user')
    R = []
    for i in cursor:
        if len(i) > 0:
            R.append([int(i[1]) + int(i[2]) + int(i[3]), i[0], i[4]])
    return R

def get_announcement():
    cursor, con = connect()
    if con is None or cursor is None:
        return 0
    cursor.execute('select * from announcement')
    res = ''
    for i in cursor:
        res = i[0]
    return res
