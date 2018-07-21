import sqlite3
import os

#指定。db文件所在位置
#dbPath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","sqlite3Test","hr.db")
dbPath = os.path.join(os.path.dirname(__file__), 'hr.db')

#获得数据库连接对象
def getConnection(dbName):
    conn = sqlite3.connect(dbName)
    return conn

#通过id查找
def findById(id):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from people where id=?', (id,))
    values = cursor.fetchall()
    #print(values)

    cursor.close()
    conn.close()

    return values
#查找全部
def findAll():
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from people')
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
    value = cursor.execute("insert into people(id,name,school,major,age,sex,phone) values ('"+people['id']+"','"+people['name']+"','"+people['school']+"','"+people['major']+"','"+people['age']+"','"+people['sex']+"','"+people['phone']+"')")
    cursor.close()
    conn.commit()
    conn.close()
    return value

#删除
def deleteById(id):
    pass


def test_findById():
    id = '564321'
    l = findById(id)
    for i in l:
        print(i)

def test_findAll():
    l = findAll()
    for i in l:
        print(i)

def test_insert():
    people = {'id':'15427038','name':'niu','school':'beijingdaxue','major':'software','age':'22','sex':'nan','phone':'110',}
    print(insert(people))

# test_insert()
test_findById()
# test_findAll()


