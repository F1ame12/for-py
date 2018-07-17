'''
str  = "dfsfsdefsfdfse"
print(set(str))

L = [2,3,4]             
L[0:1] = [1.1,1.2]  
print(L)     
L[2:]  = [3.3,4.4,5.5]
print(L)   
L[:]   = [3,4]    
print(L)

L = [1,2,3,4,5,6]
print(L)
L[0::2] = [1.1,2.2,3.3]
print(L)
#L[0:10:2]=[1.1,2.2,3.3,4.4,5.5] 报错
#print(L)
#L[0::2]=[0.1,0.3]  报错
#print(L)
L[::2]="ABC"
print(L)
#L[::2]="ABCD" 报错
#print(L)

x = [1,2,3,4,5,6]
print(len(x),max(x),min(x),sum(x),any(x),all(x))

list = [1,2,3,4]
list.append("5")
list = [1,2,3,4,"2",'2']
print(list.count("2"),type("2"),type('2'),type(list),type([]),type({}))

def func(y):
    x = y
    print("func()")
    return x,123,"大连"

def func():
    pass
a = func([1,2])
print(a,type(a))

a,b,c = func([1,2])
print(a)
print(b)
print(c)

x,y,z = 1,2,3
def add(a,b,c):
    return a+b+c
num1  = add(z,x,y)
num2  = add(12,13,14)
num3  = add(1,2,3)
print(num1,num2)

def func(a=[]):
    a.append("Q")
    return a
print(func())
print(func())
print(func())

def func(a,b=2):
    pass

def func(a,b=2):#默认参数必须在位置参数的后面
    return a**b
print(func(10,10))

def func(a = []):
    if a is 1:
        a = []
    a.append("Q")
    return a
q = func()
print(q,id(q))
w = func()
print(q,id(w))
e = func()
print(q,id(e))

def func(*args):
    print(type(args))
    for arg in  args:
        print(arg)
func("a","b","c",1,1)
list = [1,2,3]
func(list)
func(*list)

def func(**kwargs):
    print(type(kwargs))
    for arg in kwargs:
        print(arg,kwargs[arg])
dict = {
    'a':1,
    'b':2,
    'c':3
}
#func(dict) 报错，当前参数为位置参数  元祖加一个*  字典加两个**
func(**dict) 
'''
def func(name,age,*,sex):
    print(name,age,sex)

func("张三",20,sex="男")
