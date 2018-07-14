#!usr/bin/python3
# -*- coding=utf-8 -*-

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
testStr = "niujingxiang"
#print("切片：",testStr[0,2]) 
print("切片：",testStr[0:2])
print("切片：",testStr[0:2:1])
print("切片：",testStr[:3:1])#第一参数省略的话就相当于testStr[0:3:1]
print("切片：",testStr[2::1])#第一参数省略的话就相当于从索引为2的字符开始一直导结束testStr[2::1]
print("切片：",testStr[:5])#相当于[0:6:1]从开始位置截取5个
print("切片[-3:]：",testStr[-3:])# ang
print("切片[::-1]：",testStr[::-1])#gnaixgnijuin

#youngniu

# author: feathershine
import random
def random_str(length=8):
    """随机8位ascii码存入集合生成随机字符串"""
    #if (length is not type(0))
    char_list = []
    result_str = ''
    for x in range(0,8):
        ascii_num = random.randint(41,123)
        char_list.append(chr(ascii_num))
    return result_str.join(char_list)

str_test = input()
print('the input str\'s len is',len(str_test))
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
