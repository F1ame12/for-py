#!/usr/bin/python3
# -*- coding=utf-8 -*-

import os
import mylogger
import socket
import threading
import sys
import time

LOG = mylogger.getLogger('chatclient')
ADDR = ('127.0.0.1', 6666)

def main():
    start()

def start():
    hasconnect = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('正在连接服务器……')
    hasconnect = checkConn(sock)
    while True:
        print('请输入指令：')
        cmd = input()
        if hasconnect:
            sock.send(cmd.encode('utf-8'))
            time.sleep(0.5)
            t = threading.Thread(target=getMsg, args=(sock,))
            t.start()
        if cmd == 'quit':
            print('已与服务器中断连接')
            break
        if cmd == 'reconnect':
            print('正在重新连接服务器')
            hasconnect = checkConn(sock)

def checkConn(sock):
    """ sock连接成功返回True否则返回False """
    try:
        sock.connect(ADDR)
    except ConnectionRefusedError as e:
        print('与服务器连接失败')
    else:
        print('服务器连接成功！')
        return True
    return False

def getMsg(sock):
    msg = []
    LOG.debug('shit')
    while True:
        data = sock.recv(1024)
        if not data:
            break
        msg.append(data)
    msg = b''.join(msg)
    LOG.info('服务器返回信息: %s' % msg.decode('utf-8'))
    print(msg.decode('utf-8'))



if __name__ == "__main__":
    start()
