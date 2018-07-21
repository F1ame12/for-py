#!/usr/bin/python3
# -*- coding=utf-8 -*-

import socket
import sys
import json
import mylogger
import baseinfo
import threading

def main():
    server = ChatServer()
    # server.cmdStart()
    server.start()
    # a = {
    #     'client1': {
    #         'addr': ('127.0.0.1', 9999),
    #         'isalive': True
    #     },
    #     'client2':{
    #         'addr': ('127.0.0.1', 6666),
    #         'isalive': True
    #     }
    # }
    # for x in a.items():
    #     print(x)
    #     print(x[1].get('addr'))

class ChatServer(object):
    LOG = mylogger.getLogger('Server')
    HOST = '127.0.0.1'
    PORT = 9999

    def __init__(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.usermanager = UserConnManager()

    def checkOnlineWithCircle(self, connmanager):
        """每隔10分钟检查用户池用户在线状况"""
        user_list = connmanager.getList()
        threadlock = threading.RLock()
        if len(user_list) != 0:
            self.LOG.info('开始检查在线状况')
            threadlock.acquire()
            for x in user_list:
                if x[1].get('isalive') == False:
                    connmanager.rmfromList(x[0])
            threadlock.release()
        else:
            self.LOG.info('在线用户池为空 跳过此轮检查')

    def checkWebResponce(self, addr):
        check_info = baseinfo.Info()
        check_info.setType('check')
        check_info.setMsg('ok')
        check_info_dict = baseinfo.info2Dict(check_info)
        check_info_byte = json.dumps(check_info_dict).encode('utf-8')
        self.server_sock.sendto(check_info_byte, addr)
        self.LOG.info('服务端->客户端: %s' % check_info_byte)

    def start(self):
        self.LOG.debug(self.server_sock)
        self.server_sock.bind((self.HOST, self.PORT))
        self.LOG.info('服务器绑定地址 %s' % str((ChatServer.HOST, ChatServer.PORT)))
        threading.Timer(10*60, self.checkOnlineWithCircle, (self.usermanager,)).start()
        self.LOG.info('用户池检查线程开始计时')
        self.LOG.info('等待客户端发送信息')
        stop_status = False
        while not stop_status:
            recv_data, recv_addr = self.server_sock.recvfrom(1024)
            if recv_data:
                jsonstr = recv_data.decode('utf-8')
                infodict = json.loads(jsonstr)
                info = baseinfo.dict2Info(infodict)
                if self.usermanager.isOnline(info.getUid()) == True:
                    self.usermanager.update2List(info.getUid(), recv_addr)
                if info.getType() == 'msg':
                    self.LOG.info('客户端->服务端: %s' % recv_data)
                    for x in self.usermanager.getList():
                        self.LOG.debug('当前用户列表: %s', x)
                    if self.usermanager.isOnline(info.getRecvUid()) == True:
                        self.server_sock.sendto(recv_data, self.usermanager.getAddr(info.getRecvUid()))
                    else:
                        self.LOG.info('用户 %s 不在线' % info.getRecvUid())
                    ####
                elif info.getType() == 'check':
                    self.checkWebResponce(recv_addr)
                    self.usermanager.add2List(info.getUid(), recv_addr)
                elif info.getType() == 'exit':
                    self.usermanager.rmfromList(info.getUid())
                    self.LOG.info('客户端 %s 已离线' % info.getUid())
            
    #TODO(feathershine) 未完成服务器控制台指令输入
    def cmdStart(self):
        def cmd(self):
            command = input()
            if command == 'quit':
                exit()
        threading.Thread(target=cmd, args=(self)).start()
        self.LOG.info('控制台线程开启')

class UserConnManager():
    """在线用户池"""
    online_user_list = {} #采用字典实现"列表"
    threadlock = threading.RLock()
    def __init__(self):
        pass

    def getList(self):
        return self.online_user_list.items()

    def getAddr(self, uid):
        return self.online_user_list[uid]['addr']

    def add2List(self, uid, addr):
        self.threadlock.acquire()
        self.online_user_list[uid] = {'addr': addr, 'isalive': True}
        """
        {
            {
                "uid": 'client1',
                "addr": ('127.0.0.1', 9999),
                "isalive": True
            },
            {
                "uid": 'client1',
                "addr": ('127.0.0.1', 9999),
                "isalive": True
            }
        }
        """
        self.threadlock.release()

    def rmfromList(self, uid):
        self.threadlock.acquire()
        self.online_user_list.pop(uid)
        self.threadlock.release()

    def update2List(self, uid, addr):
        self.add2List(uid, addr)

    def isOnline(self, uid):
        result = self.online_user_list.get(uid)
        if result == None:
            return False
        else:
            if result.get('isalive') == True:
                return True
            else:
                return False




if __name__ == '__main__':
    main()

