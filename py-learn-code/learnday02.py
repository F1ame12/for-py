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

#youngniu

# author: feathershine
def random_str():
    pass

str_test = input()
print('the input str\'s len is',len(str_test))
print('ths str max char is', max(str_test))
print('the str min char is', min(str_test))
print(str(123456))# 将其他数据类型转为字符串
<<<<<<< HEAD
str_test *= 3 #重复字符串
str_test += 'test' #连接字符串
print('now the str is', str_test)
str_list = []
str_list.append(str_test)
print('the list len is', len(str_list))



# feathershine
=======
# feathershine
>>>>>>> b894e11bae6d79ce81b7c7759d496da6cf0ccd0a
