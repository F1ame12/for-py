# /usr/bin/python3
# -*- coding=utf-8 -*-
import random
# 这里是python学习过程中的总结

# author: feathershine
'''
变量类型共有：整型int，字符串string，浮点型float，布尔型bool
但一个变量可以不限类型，可以存储以上各种类型，测试如下
'''
print('====变量类型测试====')
varA = 50
print('1.', varA)
varA = 'hello world'
print('2.', varA)
varA = 0.5
print('3.', varA)
varA = True
print('4.', varA)
print('====End====')
'''
print()是python提供的基本输出函数
print函数可输出各类基本的数据类型
'''
print('====print输出测试====')
print('1.hello world!')
#不同数据之间通过逗号可分开，实际输出逗号会转化为空格
print('2.this','is',1,'word')
#字符串可通过“+”拼接，“*”表示重复
print('3.hello'+'world')
print('4.repeat twice'*2)
#print亦可以格式化输出，常用替换符整型%d、浮点型%f、字符串%s
print('5.num is %d %d' % (666,555))
print('6.num is %f' % 5.5)
print('6.string is %s' % 'test')
print('====End====')
#运算符(+、-、*、/、//（整除，“地板除”）、**（幂运算）)
print('2*2=%f 5/2=%f 5//2=%f 5**2=%d' % (2*2,5/2,5//2,5**2))
'''
is运算符 a is b   a is not b
判断两个变量是否引用同一个对象，同一个返回True，不同返回False
'''
a = 50
b = 50
c = 100
print('a==b?',a is b)
print('a!=b?',a is not b)
print('a==c?', a is c)

#for循环
for x in range(1,6):
    print('num is',x)

name = input()
print(name)

# feathershine


#youngniu
#===数据运算===
print('===数据运算===')
# 1地板除运算：//，向下取整
print(-5//2)
print(5//2)
# 2幂运算：**
print(2**2)

print('===计算面积===')
pai=3.1415926
#print('输入半径')
r = int(input('输入半径：'))
c=pai*r*r
print('面积是：',c)

a='niu'
b='jing'

a1=1
b1=2

a2=False
b2=True

print(a or b)
print(a1 or b1)
print(a2 or b2)

#产生0-10的随机整数，包括0和10
print('产生一个0-10的随机数',random.randint(0,10))

#猜数字游戏
a = random.randint(0,10)
flag = True
while(flag):
    b=int(input('猜一个0-10的随机数，包括0与10:'))
    if(b<a):
        print('猜小了')
    elif(b>a):
        print('猜大了')
    else:
        print('恭喜，猜对了')
        flag=False

#youngniu