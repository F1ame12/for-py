import sqlite3
import os
import random
import json

#指定。db文件所在位置
#dbPath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","sqlite3Test","hr.db")
dbPath = os.path.join(os.path.dirname(__file__), 'chart.db')

#获得数据库连接对象
def getConnection(dbName):
    conn = sqlite3.connect(dbName)
    return conn

#通过id查找
def findById(id):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from user1 where id=?', (id,))
    values = cursor.fetchall()
    #print(values)

    cursor.close()
    conn.close()

    return values

#通过id和密码查找
def findByIdAndPass(id,password):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from user1 where id=? and password=?', (id,password))
    values = cursor.fetchall()
    #print(values)
    # print('select * from user1 where id=?,password=?', (id,password))
    cursor.close()
    conn.close()

    return values

#通过username和密码查找
def findByUsernameAndPass(username,password):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from user1 where username=? and password=?', (username,password))
    values = cursor.fetchall()
    #print(values)
    # print('select * from user1 where id=?,password=?', (id,password))
    cursor.close()
    conn.close()

    return values

#查找全部
def findAll():
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from user1')
    values = cursor.fetchall()
    #print(values)

    cursor.close()
    conn.close()
    return values

#插入
def insert(people):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    # sql = "insert into people(id,name,school,major,age,sex,phone) values (people['id'],people['name'],people['school'],people['major'],people['age'],people['sex'],people['phone'])
    # sql = "insert into people((id,name,school,major,age,sex,phone) values ('"+people['id']+"','"+people['name']+"','"+people['school']+"','"+people['major']+"','"+people['age']+"','"+people['sex']+"','"+people['phone']+"')"
    # sql = "insert into user1(id,username,netname,password) values ('"+people['id']+"','"+people['username']+"','"+people['netname']+"','"+people['password']+"','"+people['friend']+"')"
    value = cursor.execute("insert into user1(id,username,netname,password,friend) values ('"+people['id']+"','"+people['username']+"','"+people['netname']+"','"+people['password']+"','"+people['friend']+"')")
    
    cursor.close()
    conn.commit()
    conn.close()
    return value

#删除
def deleteById(id):
    conn = getConnection(dbPath)
    cursor = conn.cursor()

    cursor.execute("delete from user1 where id='"+id+"'")
    value = cursor.rowcount

    cursor.close()
    conn.commit()
    conn.close()
    return value

def randomStr(length=6):
    """随机n位(默认为8)ascii码存入集合生成随机字符串"""
    if type(length) != type(0):
        raise TypeError('参数应当为整型')
    char_list = []
    result_str = ''
    strRange = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(0, int(length)):
        num = random.randint(0, len(strRange)-1)
        char_list.append(strRange[num])
    return result_str.join(char_list)

def getFriendById(id):
    user = findById(id)
    friend = user[0][4]
    # print(type(friend))
    friend = json.loads(friend)
    for i in range(len(friend)):
        print(friend[i])
    return friend

def test_findById():
    id = '564321'
    l = findById(id)
    for i in l:
        print(i)

def test_deleteById():
    id = 'C43rsq'
    value = deleteById(id)
    if(value==0):
        print('未删除任何数据')
    else:
        print("已删除：id为"+id+"数据")

def test_findAll():
    l = findAll()
    for i in l:
        print(i)

def test_insert():
    id = randomStr()
    username = 'zhanhailun'
    netname = 'feathershine'
    password = 'admin'

    data = [
        {
            'id':'abcdef',
            'username':'123456'
        },
        {
            'id':'test2',
            'username':'test2'
        }
    ]
    friend = json.dumps(data)
    print ("Python 原始数据：", repr(data))
    print ("JSON 对象：", friend,type(friend))
    people = {'id':id,'username':username,'netname':netname,'password':password,'friend':friend}
    # sql = "insert into user1(id,username,netname,password,friend) values ('"+people['id']+"','"+people['username']+"','"+people['netname']+"','"+people['password']+"','"+people['friend']+"')"
    # print(sql)
    print(insert(people))

# test_insert()
# test_findById()
# test_deleteById()
# test_findAll()
# print(randomStr())
# getFriendById('EM5uzH')
# print(findByIdAndPass('EM5uzH','admin'))
print(findByUsernameAndPass('niujingxiang','admin'))

