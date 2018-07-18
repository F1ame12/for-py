#!/usr/bin/python3
# -*- coding=utf-8 -*-
import socket
import mylogger
import threading
import time



def client():
    log = mylogger.getLogger('Client')
    print('输入服务器地址及端口号：')
    inputstr = str(input())
    host = inputstr.split(' ')[0]
    port = int(inputstr.split(' ')[1])
    log.info('IP: %s Port: %d' % (host, port))
    log.info('开始连接server')
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host,port))
    print('发送命令：')
    while True:
        cmd = input()
        if cmd == 'quit':
            break
        else:
            cmd = cmd.encode('utf-8')
        log.info('正在发送命令,cmd = %s' % cmd)
        mysocket.send(cmd)
        time.sleep(1)
        buffer = []
        while True:
            d = mysocket.recv(1024)
            if d.decode('utf-8') == 'exit':
                break
            if d:
                buffer.append(d)
            else:
                break
            data = b''.join(buffer)
            log.info('服务器返回信息: \n%s' % data.decode('utf-8'))
        
        log.info('信息接受完毕，开始下一轮命令输入')
    log.info('已中断与server的连接')

def server():
    log = mylogger.getLogger('Server')
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log.info('正在建立服务器')
    mysocket.bind('127.0.0.1', 9999)
    mysocket.listen(10)
    log.info('服务器建立完成！等待连接')
    while True:
        sock, addr = mysocket.accept()
        t = threading.Thread(target=serverfunc, args=(sock, addr))
        t.start

def serverfunc(sock, addr):
    log = mylogger.getLogger('ServerFunction')
    log.info('开始处理客户端请求')
    sock.send('老牛是傻逼！\n'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        #log.info('服务器接受数据: %s' % )
        time.sleep(1)
        if not data or data.decode('utf-8') == 'quit':
            break
        if data.decode('utf-8') == 'fuck':
            sock.send('老牛是个大沙雕！\n'.encode('utf-8'))
        else:
            sendstr = '客户端数据: %s' % data.decode('utf-8')
            sock.send(sendstr.encode('utf-8'))
        sock.close()
        log.info("服务器发送数据结束")

if __name__ == '__main__':
    log = mylogger.getLogger('mysocket')
    print('选择启动项-1、server 2、client')
    select = input()
    if '1' == select:
        server()
    elif '2' == select:
        client()