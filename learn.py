#!/usr/bin/python3
# -*- coding=utf-8 -*-

# 这里是python学习过程中的总结

# author: feathershine
'''
变量类型共有：整型int，字符串string，浮点型float，布尔型bool
但一个变量可以不限类型，可以存储以上各种类型，测试如下
'''
print('====变量类型测试====')
varA = 50
print(varA)
varA = 'hello world'
print(varA)
varA = 0.5
print(varA)
varA = True
print(varA)
print('====End====')
'''
print()是python提供的基本输出函数
print函数可输出各类基本的数据类型
'''
print('1.hello world!')
#不同数据之间通过逗号可分开，实际输出逗号会转化为空格
print('2.this','is',1,'word')
#字符串可通过“+”拼接，“*”表示重复
print('3.hello'+'world')
print('4.repeat twice'*2)
#print亦可以格式化输出，常用替换符整型%d、浮点型%f、字符串%s
print('5.num is %d' % 666)
print('6.num is %f' % 5.5)
print('6.string is %s' % 'test')

def fun(a):
    if a>50:
        print('true')
    else:
        print('false')
    return

num = 55
fun(num)
print(num)

# feathershine


