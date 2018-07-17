#!/usr/bin/python3
# -*- coding=utf-8 -*-

import mylogger
import myutil
import mygui


#logging.basicConfig(level=logging.DEBUG)
logger = mylogger.getLogger(loglevel='debug',name='test')

logger.debug('test log text')
print('fine!')


a = mylogger.Log()
print(a.num)
app = mygui.Application()

app.mainloop()


'''
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
'''
