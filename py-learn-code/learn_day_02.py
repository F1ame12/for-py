#!usr/bin/python3
# -*- coding=utf-8 -*-
import random
#youngniu

#1.test print()
value=10
number=20
print("print函数的用法",value,number,sep="，",end="。",flush=False)

#2.test str
str1="my name is niu jingxiang"
str2="""I'm a 18's old boy"""
print("max(str)的用法：",max(str1),"len(str)的用法：",len(str1))
print("min()的用法：",min(str1))

#3.字符串运算
str_link = "niu"+"jingxiang"
print("1.str+str:",str_link)
str_link+=str_link
print("2.str+=:",str_link)
print("3.str_link*3:",str_link*3)

#4.in|not in 运算符
if "niu" in "niujingxiang":
    print("niujingxiang 中有 niu")

#5.切片
testStr = "Niujingxiang"
testNumber='123456'
#print("切片：",testStr[0,2]) 
print("切片：",testStr[0:2])
print("切片：",testStr[0:2:1])
print("切片：",testStr[:3:1])#第一参数省略的话就相当于testStr[0:3:1]
print("切片：",testStr[2::1])#第一参数省略的话就相当于从索引为2的字符开始一直导结束testStr[2::1]
print("切片：",testStr[:5])#相当于[0:6:1]从开始位置截取5个
print("切片[-3:]：",testStr[-3:])# ang
print("切片[::-1]：",testStr[::-1])#gnaixgnijuin

#6.字符串的操作
print("变小写：",testStr.lower())
print("变大写：",testStr.upper())
print("判断是否为英文字母：",testStr.isalpha())
print("判断是否为数字：",testStr.isdigit())
<<<<<<< HEAD
print("返回字符串中子字符串的个数：",testStr.count('ing',0,len(testStr)))
=======
print("判断是否为数字：",testNumber.isdigit())
print("去掉两端的空白字符：",testStr.strip())
print("返回字符串中子字符串的个数：",testStr.count("ng"))

#7.循环
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

>>>>>>> 57e6081783f3397609a7d3505efef4c3a3bf96db
#youngniu



# author: feathershine
import random
def random_str(length=8):
    """随机8位ascii码存入集合生成随机字符串"""
    #if (length is not type(0))
    char_list = []
    result_str = ''
    strRange = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(0, int(length)):
        num = random.randint(0, len(strRange)-1)
        char_list.append(strRange[num])
    return result_str.join(char_list)

str_test = input()
print('the input str\'s len is', len(str_test))
print('ths str max char is', max(str_test))
print('the str min char is', min(str_test))
print(str(123456))# 将其他数据类型转为字符串
str_test *= 3 #重复字符串
str_test += 'test' #连接字符串
print('now the str is', str_test)
str_list = []
str_list.append(str_test)
print('the list len is', len(str_list))
print('we create 3 random str is',random_str(),random_str(),random_str())


# feathershine
 
#black-chocolate
'''
s = "Hello Python"
print(s.lower(),s.upper(),s.title(),s.isdigit(),s.islower(),
s.isupper(),s.isalpha(),s.strip(),s.rstrip(),s.lstrip(),s.count("He"),
s.find("Py"),s.replace("l","o",1))
'''
s = input()
print(s.replace("123","321"))  

number = int(input())
randber = random.randint(0,10)
while number != randber: 
    number = int(input())
    if number < randber:
        print("猜小了")
    else:
        print("猜大了")
print("猜的针对，真聪明")
#black-chocolate
