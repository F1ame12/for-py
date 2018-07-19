#!/usr/bin/python3
# -*- coding=utf-8 -*-

import os
import mylogger
import socket
import threading
import sys
import asyncio
import time

LOG = mylogger.getLogger('chatclient')
ADDR = ('127.0.0.1', 6666)

def main():
    start()

def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('正在连接服务器……')
    sock.connect(ADDR)
    print('服务器连接成功！')
    while True:
        print('请输入指令：', end = ' ')
        cmd = input()
        sock.send(cmd.decode('utf-8'))
        if cmd == 'quit':
            LOG.info('已与服务器中断连接')
            break
        threading.Thread(target=getMsg, args=(sock, addr))


def getMsg(sock, addr):
    msg = []
    while True:
        data = sock.recv(1024)
        if not data:
            break
        msg.append(data)
    msg = b''.join(msg)
    LOG.info('服务器返回信息: %s' % msg.decode('utf-8'))
    print('[Client] %s' % msg.decode('utf-8'))



if __name__ == "__main__":
    start()
