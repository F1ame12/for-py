#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging
import sys
import os
import time

__author__ = 'feathershine'

# TODO(feathershine) 尝试封装logging模块，调试代码过程中出现异常，暂停尝试

def main():
    # raise RuntimeError('不能直接运行模块！')
    logpath = os.path.join(os.path.abspath('.'), 'logs', 'log')
    a = Log(name='helloBUG', level='debug', handle='file')
    a.info('test words')

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    filehandle = logging.FileHandler('log.log','a','utf-8')
    consolehandle = logging.StreamHandler(sys.stderr)
    formatstr = '[%(asctime)s] %(name)s [%(levelname)s] %(message)s'
    formatter = logging.Formatter(formatstr)
    filehandle.setFormatter(formatter)
    consolehandle.setFormatter(formatter)
    logger.addHandler(filehandle)
    logger.addHandler(consolehandle)
    return logger

# class Log(object):
#     """
#     Log(self[, name='', level='', handle=''])
#     name: debug显示名
#     level: debug级别从低到高为 info < debug < warning < error < critical
#     handle: debug输出设备 可选 console / file / all
#     """

#     def getFormatter(self):
#         logformat = '[%(asctime)s] %(name)s [%(levelname)s] %(message)s'
#         return logging.Formatter(logformat)
    
#     def getLevel(self, level):
#         leveldict = {'info': logging.INFO,
#                     'debug': logging.DEBUG,
#                     'warning': logging.WARNING,
#                     'error': logging.error,
#                     'critical': logging.CRITICAL}
#         return leveldict.get(level)

#     def getLogger(self, **args):
#         """test"""
#         if 'name' in args:
#             return logging.getLogger(args.get('name'))
#         else:
#             return logging.getLogger('Log')
    
#     def getHandle(self, logtype, **args):
#         if logtype == 'file':
#             if 'path' in args:
#                 path = args.get('path')
#             else:
#                 path = 'log-' + time.strftime(r'%Y-%m-%d') + '.log'
#             if 'mode' in args:
#                 mode = args.get('mode')
#             else:
#                 mode = 'a'
#             if 'encoding' in args:
#                 encoding = args.get('encoding')
#             else:
#                 encoding = 'utf-8'
#             handle = logging.FileHandler(path, mode, encoding)
#         elif logtype == 'console':
#             handle = logging.StreamHandler(sys.stderr)
#         return handle

#     def __init__(self, **args):
        
#         if len(args) == 0:
#             self.baseLogger(self)
#         else:
#             self.optionLogger(**args)

#     def baseLogger(self):
#         self._logger = self.getLogger()
#         self._logger.setLevel(logging.DEBUG)
#         self._handle = self.getHandle('console')
#         self._formatter = self.getFormatter()
#         self._handle.setFormatter(self._formatter)
#         self._logger.addHandler(self._handle)
    
#     def optionLogger(self, **args):
#         if 'name' in args:
#             self._logger = self.getLogger(name=args.get('name'))
#         else:
#             self._logger = self.getLogger()
#         if 'level' in args:
#             self._logger.setLevel(self.getLevel(args.get('level')))
#         else:
#             self._logger.setLevel(logging.DEBUG)
#         return
#         # if 'handle' in args:

#         # else:
#         #     self._handle.append(self.getHandle('console')   
#         # self._handle.setFormatter(self.getFormatter())
#         # self._logger.addHandler(self._handle)

#     def info(self, msg):
#         self._logger.info(msg)
    
#     def debug(self, msg):
#         self._logger.debug(msg)
    
#     def warning(self, msg):
#         self._logger.warning(msg)
    
#     def error(self, msg):
#         self._logger.error(msg)
    
#     def critical(self, msg):
#         self._logger.critical(msg)

    

# if __name__ == '__main__':
#     main()

