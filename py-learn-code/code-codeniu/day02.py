#!usr/bin/python3
# -*- coding=utf-8 -*-

import random

'''
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
'''

#ord()函数
print('\u4e2d\u6587')
niu=ord('牛')
jing=ord('靖')
xiang=ord('翔')
print('牛靖翔',niu,jing,xiang)
print('牛靖翔','牛靖翔'.encode('utf-8'))

#for循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#函数
def menu():
    print("有房吗？")
    print("有车吗？")
    print("有钱吗？")
menu()

#rang()函数 range(101)生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print("1+2+.....+100=",sum)

#打印54321
print("打印5-1：")
for x in range(5,0,-1):
    print(x)

#打印10以内的奇数
print("打印10以内的奇数：")
for x in range(1,11,2):
    print(x)