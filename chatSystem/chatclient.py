#!/usr/bin/python3
# -*- coding=utf-8 -*-

import socket
import sys
import json
import threading
import mylogger
import baseinfo
import time

def main():
    cmd = input()
    client = ChatClient()
    if cmd == '1':
        client.uid = 'client1'
    elif cmd == '2':
        client.uid = 'client2'
    elif cmd == '3':
        client.uid = 'client3'
    client.start()

class ChatClient(object):

    LOG = mylogger.getLogger('Client')
    
    HOST = '127.0.0.1'
    PORT = 9999
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.uid = 'client1'

    def checkNet(self):
        """检查网络是否通畅"""
        timer = time.time()
        self.LOG.info('timer = %s' % timer)
        check_info = baseinfo.Info()
        check_info.setType('check')
        check_info.setUid(self.uid)
        check_info_dict = baseinfo.info2Dict(check_info)
        check_info_byte = json.dumps(check_info_dict).encode('utf-8')
        self.LOG.debug(check_info_byte)
        while True:
            nowtime = time.time()
            self.LOG.info('nowtime = %s' % nowtime)
            if nowtime - timer >= 3.0:
                return False
            self.client_sock.sendto(check_info_byte, self.ADDR)
            time.sleep(0.5)
            recv_data = self.client_sock.recv(1024)
            if recv_data:
                check_result_dict = json.loads(recv_data.decode('utf-8'))
                check_result = baseinfo.dict2Info(check_result_dict)
                if check_result.msg == 'ok':
                    return True
    
    def waitMsg(self):
        while True:
            self.LOG.info('等待接受信息')
            recv_data = self.client_sock.recv(1024)
            if recv_data:
                info_dict = json.loads(recv_data.decode('utf-8'))
                info = baseinfo.dict2Info(info_dict)
                msg = info.getMsg()
                senduid = info.getUid()
                self.LOG.info('[%s] %s' % (senduid, msg))

    def sendMsg(self, senduid, msg):
        info = baseinfo.Info()
        info.setMsg(msg)
        info.setType('msg')
        info.setUid(self.uid)
        info.setRecvUid(senduid)
        info_dict = baseinfo.info2Dict(info)
        info_byte = json.dumps(info_dict).encode('utf-8')
        self.client_sock.sendto(info_byte, self.ADDR)

    def sendLogOutMsg(self):
        info = baseinfo.Info()
        info.setType('exit')
        info.setUid(self.uid)
        info_dict = baseinfo.info2Dict(info)
        info_byte = json.dumps(info_dict).encode('utf-8')
        self.client_sock.sendto(info_byte, self.ADDR)

    def start(self):
        self.LOG.info('客户端开启')
        check_status = self.checkNet()
        self.LOG.info('网络验证结果: %s' % check_status)
        if check_status == True:
            
            sendto = input()
            msg = input()
            msg_thread = threading.Thread(target=self.waitMsg, args=(self,))
            if msg == 'quit':
                self.sendLogOutMsg()
                return
            else:
                self.sendMsg(sendto, msg)
            time.sleep(5)



if __name__ == '__main__':
    main()


