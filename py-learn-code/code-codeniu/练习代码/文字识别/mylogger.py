#!/usr/bin/python3
# -*- coding=utf-8 -*-

__author__ = 'feathershine'

import logging
import sys

def main():
    raise RuntimeError('不能直接运行模块！')
    

class Log(object):
    num = 5
    def __init__(self):
        return 


# TODO(feathershine): 尝试封装python自带logging模块的功能，提供更为简便的方法
def getLogger(**args):
    #获得一个根据参数设定的logger对象
    if len(args) == 0:
        raise AttributeError('缺少足够参数')
    if 'logname' in args:
        name = args.get('logname')
        if type(name) != type(''):
            raise TypeError('name参数应当为字符串')
    else:
        name = 'mylogger'
    if 'loglevel' in args:
        loglevel = args.get('loglevel')
        if type(loglevel) != type(''):
            raise TypeError('loglevel参数应当为字符串')
        else:
            if loglevel == 'info':
                loglevel = logging.INFO
            elif loglevel == 'debug':
                print('debug is choosed')
                loglevel = logging.DEBUG
            elif loglevel == 'warning':
                loglevel = logging.WARNING
            elif loglevel == 'error':
                loglevel = logging.ERROR
            elif loglevel == 'critical':
                loglevel = logging.CRITICAL
    if 'logformat' in args:
        logformat = args.get('logformat')
        if type(logformat) != type(''):
            raise TypeError('logformat参数应当为字符串')
    else:
        logformat = '[%(asctime)s] %(name)s [%(levelname)s] %(message)s'
    logger = logging.getLogger(name)
    stdhandle = logging.StreamHandler(sys.stderr)
    filehandle = logging.FileHandler('log.log','a','utf-8')
    logger.setLevel(loglevel)
    logformatter = logging.Formatter(logformat)
    stdhandle.setFormatter(logformatter)
    filehandle.setFormatter(logformatter)
    logger.addHandler(filehandle)
    logger.addHandler(stdhandle)
    return logger



if (__name__ == '__main__'):
    main()

