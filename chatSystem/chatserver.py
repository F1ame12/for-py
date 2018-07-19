#!/usr/bin/python3
# -*- coding=utf-8 -*-

import os
import mylogger
import socket
import threading
import sys
import asyncio
import time

LOG = mylogger.getLogger('chatserver')
ADDR = ('127.0.0.1', 6666)

def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(ADDR)
    LOG.info('服务器开始监听消息 服务器ADDR= %s' % str(ADDR))
    msgthread = threading.Thread(target=msgDeal, args=sock)
    msgthread.start()
    while True:
        LOG.info('服务器等待指令输入')
        cmd = input()
        if cmd == 'shutdown':
            break
        elif cmd == 'reboot':
            new = threading.Thread(target=start())
            new.start()
            break
        else:
            print("命令 %s 无效" % cmd)

def msgDeal(sock):
    while True:
        clientsock, addr = sock.accept()
        t = threading.Thread(target=getMsg, args=(clientsock, addr))
        t.start()

def getMsg(sock, addr):
    LOG.info("新连接: %s" % addr)
    msg = []
    while True:
        data = sock.recv(1024)
        if data.decode('utf-8') == 'quit':
            sock.close()
            LOG.info("连接 %s 已与服务器断开连接" % str(addr))
            break
        elif not data:
            msg.append(data)
        msg = b''.join(msg)
        sendmsg = '[Server] hello! your command is %s' % msg.decode('utf-8')
        sock.send(sendmsg.encode('utf-8'))


        



if __name__ == '__main__':
    start()