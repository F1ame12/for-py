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
'''
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
'''

# 7.默认参数

    # Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
    # 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''
def add_end(L=[]):
    L.append('END')
    return L

test = add_end()
test = add_end()

print(test)
'''

'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

test = add_end()
test = add_end()

test1 = add_end([1,2,3])
print(test)
print(test1)
'''

# 8.关键字参数
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    print(type(kw))

person('niujingxiang',21,city='beijing')

others={'city':'beijing','job':'softwarer'}
person('niujingxiang',21,**others)
'''
# 9.可变参数
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print('calc(1,2,3):',calc(1,2,3))

nums = [1, 2, 3]
print('calc(*nums):',calc(*nums))

print('calc(nums[0],nums[1],nums[2]):',calc(nums[0],nums[1],nums[2]))
'''

#10.查看Python版本
# import sys
# print(sys.version_info.major)

