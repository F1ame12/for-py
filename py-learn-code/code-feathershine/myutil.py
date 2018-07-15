#!/usr/bin/python3
# -*- coding=utf-8 -*-

__author__ = 'feathershine'

if __name__ == '__main__':
    raise RuntimeError('不能直接运行模块！')
else:
    import random

def randomStr(length=8):
    """随机n位(默认为8)ascii码存入集合生成随机字符串"""
    if type(length) != type(0):
        raise TypeError('参数应当为整型')
    char_list = []
    result_str = ''
    strRange = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(0, int(length)):
        num = random.randint(0, len(strRange)-1)
        char_list.append(strRange[num])
    return result_str.join(char_list)

def delRepeatStr(str1, str2, **option):
    """输入两个字符串，分别去除两字符串相同的部分"""
    if type(str1) != type(''):
        raise TypeError('参数1必须是字符串')
    if type(str2) != type(''):
        raise TypeError('参数2必须是字符串')
    if len(str1) <= len(str2):
        slist = list(str1)
        llist = list(str2)
    else:
        slist = list(str2)
        llist = list(str1)
    for i in range(slist):
        index_llist = llist.index(slist[i])
            
    

    return 
