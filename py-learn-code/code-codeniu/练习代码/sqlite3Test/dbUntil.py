import sqlite3
import os

#dbPath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","sqlite3Test","hr.db")
dbPath = os.path.join(os.path.dirname(__file__), 'hr.db')

def getConnection(dbName):
    conn = sqlite3.connect(dbName)
    return conn

def findById(id):
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from people where id=?', (id,))
    values = cursor.fetchall()
    #print(values)

    cursor.close()
    conn.close()

    return values

def findAll():
    conn = getConnection(dbPath)
    cursor = conn.cursor()
    cursor.execute('select * from people')
    values = cursor.fetchall()
    #print(values)

    cursor.close()
    conn.close()

    return values



def test_findById():
    id = '002'
    l = findById(id)
    for i in l:
        print(i)

def test_findAll():
    l = findAll()
    for i in l:
        print(i)


test_findById()
test_findAll()


