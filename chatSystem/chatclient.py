#!/usr/bin/python3
# -*- coding=utf-8 -*-

import socket
import sys
import json
import mylogger
import baseinfo
import time

def main():
    client = ChatClient()
    client.start()

class ChatClient(object):

    LOG = mylogger.getLogger('Client')
    
    HOST = '127.0.0.1'
    PORT = 9999
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def checkNet(self):
        """检查网络是否通畅"""
        timer = time.time()
        self.LOG.info('timer = %s' % timer)
        check_info = baseinfo.Info()
        check_info.setType('check')
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
    
    def sendMsg(self,addr, msg):
        pass

    def start(self):
        self.LOG.info('客户端开启')
        check_status = self.checkNet()
        self.LOG.info('网络验证结果: %s' % check_status)



if __name__ == '__main__':
    main()


