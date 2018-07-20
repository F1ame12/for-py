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

class ChatServer(object):
    LOG = mylogger.getLogger('Server')
    HOST = '127.0.0.1'
    PORT = 9999

    def __init__(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.usermanager = UserConnManager()

    def checkWithCircle(self, connmanager):
        """每隔10分钟检查用户池用户在线状况"""
        user_list = connmanager.getList()
        threadlock = threading.RLock()
        if len(user_list) != 0:
            self.LOG.info('开始检查在线状况')
            threadlock.acquire()
            for x in user_list:
                if x.get('isalive') == False:
                    connmanager.rmfromList(x[0])
            threadlock.release()
        else:
            self.LOG.info('在线用户池为空 跳过此轮检查')

    def start(self):
        self.LOG.debug(self.server_sock)
        self.server_sock.bind((self.HOST, self.PORT))
        self.LOG.info('服务器绑定地址 %s' % str((ChatServer.HOST, ChatServer.PORT)))
        threading.Timer(10*60, self.checkWithCircle,self.usermanager).start()
        self.LOG.info('用户池检查线程开始计时')
        self.LOG.info('等待客户端发送信息')
        stop_status = False
        while not stop_status:
            recv_data, recv_addr = self.server_sock.recvfrom(1024)
            if recv_data:
                jsonstr = recv_data.decode('utf-8')
                infodict = json.loads(jsonstr)
                info = baseinfo.dict2Info(infodict)
                if info.getType() == 'msg':
                    self.LOG.info('客户端发送信息: %s' % info.getMsg())
                elif info.getType() == 'check':
                    check_info = baseinfo.Info()
                    check_info.setType('check')
                    check_info.setMsg('ok')
                    check_info_dict = baseinfo.info2Dict(check_info)
                    check_info_byte = json.dumps(check_info_dict).encode('utf-8')
                    self.server_sock.sendto(check_info_byte, recv_addr)
                    self.LOG.info('服务端->客户端: %s' % check_info_byte)
                    # self.usermanager.add2List(info.uid, recv_addr)
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

    def add2List(self, uid, addr):
        self.threadlock.acquire()
        self.online_user_list[uid] = {'addr': addr, 'isalive': True}
        self.threadlock.release()

    def rmfromList(self, uid):
        self.threadlock.acquire()
        self.online_user_list.pop(uid)
        self.threadlock.release()

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

