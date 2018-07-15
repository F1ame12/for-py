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