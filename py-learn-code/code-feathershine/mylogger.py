#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging
import sys
import time

__author__ = 'feathershine'

def main():
    # raise RuntimeError('不能直接运行模块！')
    a = Log()
    print(a.test())

class Log(object):
    """dfsfdsdfdsf"""
    def __init__(self, **args):
        if len(args) == 0:
            self.baseLogger()

    def baseLogger(self):
        self._logger = self.getLogger()
        self._logger.setLevel(logging.DEBUG)
        self._handle = self.getHandle('console')
        self._formatter = self.getFormatter()
        self._handle.setFormatter(self._formatter)

    def test():
        return self._logger

    def getLogger(logname):
        """test"""
        logging.error(logname)
        return logging.getLogger(logname)
    
    def getHandle(logtype, **args):
        if logtype == 'file':
            if 'path' in args:
                path = args.get('path')
            else:
                path = 'log-' + time.strftime(r'%Y-%m-%d') + '.log'
            if 'mode' in args:
                mode = args.get('mode')
            else:
                mode = 'a'
            if 'encoding' in args:
                encoding = args.get('encoding')
            else:
                encoding = 'utf-8'
            return logging.FileHandler(path, mode, encoding)
        elif logtype == 'console':
            return logging.StreamHandler(stderr)

    def getFormatter():
        logformat = '[%(asctime)s] %(name)s [%(levelname)s] %(message)s'
        return logging.Formatter(logformat)
    
    def info(msg):
        self._logger.info(msg)
    
    def debug(msg):
        self._logger.debug(msg)
    
    def warning(msg):
        self._logger.warning(msg)
    
    def error(msg):
        self._logger.error(msg)
    
    def critical(msg):
        self._logger.critical(msg)
    

'''
# TODO(feathershine): 尝试封装python自带logging模块的功能，提供更为简便的方法
def getLoggerTest(**args):
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
'''


if (__name__ == '__main__'):
    main()

