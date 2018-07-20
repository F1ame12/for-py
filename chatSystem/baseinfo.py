#!usr/bin/python3
# -*- coding=utf-8 -*-

import json

class Info(object):

    def __init__(self):
        self.uid = 'default'
        self.itype = 'none'
        self.msg = 'default'

    def getUid(self):
        return self.uid
    
    def setUid(self, uid):
        self.uid = uid
    
    def getType(self):
        return self.itype
    
    def setType(self, itype):
        self.itype = itype

    def getMsg(self):
        return self.msg
    
    def setMsg(self, msg):
        self.msg = msg

def info2Dict(info):
    return {
        'uid': info.getUid(),
        'itype': info.getType(),
        'msg': info.getMsg()
    }
    
def dict2Info(infodict):
    info = Info()
    info.setUid(infodict.get('uid'))
    info.setType(infodict.get('itype'))
    info.setMsg(infodict.get('msg'))
    return info
