#!/usr/bin/python3
# -*- coding=utf-8 -*-

# 这里是python学习过程中的总结

# author: feathershine
'''
变量类型共有：整型int，字符串string，浮点型float，布尔型bool
但一个变量可以不限类型，可以存储以上各种类型，测试如下
'''
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
#print()是python提供的基本输出函数
#print函数可输出各类基本的数据类型
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
#is运算符 a is b   a is not b
#判断两个变量是否引用同一个对象，同一个返回True，不同返回False
'''
a = 50
b = 50
c = 100
print('a==b?',a is b)
print('a!=b?',a is not b)
print('a==c?', a is c)

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
print('输入半径')
r = int(input())
c=pai*r*r
print('面积是：',c)
#youngniu

#black-chocolate

if 真值表达式
    语句1
elif 真值表达式2
    语句2
elif 真值表达式 3
    语句3
else:
    语句4

import random

randber = random.randint(0,10)
number = int(input())
if number < randber:
    print("猜小了")
elif number > randber:
    print("猜大了")
else :
    print("猜对了")

#猜数字游戏   10  5  2 提示用户猜小了
'''

#black-chocolate
'''
基本输出函数：print
print("提示信息",value,value,....,sep="",end="\n",flush =False,file=sys.stdout)
"":提示信息
value:值
sep:分隔符(缺省的是一个空格)
end:结束标识（缺省的是换行符）
flush:缓冲  - 是否立即将流输出（True/False）
    -程序结束缓冲区中的内容
file :对象流  - 默认为sys.stdoutf

a = 10
b = 20
c = 30
c = "I'm a teacher"
print("输出",a,b,c,sep=",",end=".",flush=False)

字符串：
    序列的一种  - 按一定顺序进行排列
    ''               eg: 'I'm a teacher'出错
    ""               所见即所得
    '''  '''         所见即所得 
    """  """         所见即所得

字符串常用函数:
    len(str):   返回字符串的长度
    max(str):   返回字符串中最大的字符
    min(str):   返回字符串中最小的字符
    d = """I'm a teacher"""
    f = len(d)
    print("输出",f)
'''


#black-chocolate