#1.
'''
str = input("输入字符串")
print("第一个字符为:%s"%str[0]+"中间的一个字符为:%s"%str[(len(str)-1)//2])
'''

#2.列表的基本用法
'''
friends = ['niu','zhan','sun']
for x in friends:
    print (x)

friends.append('new')
print("来个新来的")
for x in friends:
    print (x)

friends.insert(1,'boss')
print("来个boss在第二位")
for x in friends:
    print (x)

print("弹出第三个")
friends.pop(2)
for x in friends:
    print (x)
'''
#3.字符统计
'''
str = list(input("输入字符串:"))
str1 = set(str)#set()函数:对列表进行去重

print("队列表进行去重:")
for x in str1:
    print(x)

for x in str1:
    print("字符%s出现的次数:"%x, str.count(x))
'''

#4.列表的基本操作
'''
print(['a',1]>['b',2]) #flase
list1 = [2,3,4]
print(list1[0:2])
'''

#5.
'''
l=[1,2,3,4,5,6]
print(l[0::2])
'''

#6.自定义函数
def sayHello(name):
    print("你好",name)

sayHello("niu")

def func(y):
    x=y
    print("func()")
    return x,132,"大连"

a,b,c = func([1,2])
d = func([1,2])
print(a)
print(b)
print(c)
print(d)
print("type(a)的值:",type(a))
print("type(d)的值:",type(d))


a = 1
print(id(a))

def funb (a):
    print(id(a))

funb(a)