#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os
import sys
import time
import socket
import threading

HOST = "0.0.0.0"
PORT = 4700

class baseServer(object):
    _host = ""
    _port = 0
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _maxSocketNum = 0
    _isClose = False
    _stdout = sys.stdout
    def __init__(self, host = HOST, port = PORT, maxSocket = 10):
        self._host = host
        self._port = port
        self._maxSocketNum = maxSocket

    #服务器基类基本监听函数
    def serverListen(self):
        self._socket.bind((self._host, self._port))
        self._socket.listen(self._maxSocketNum)
        print("[System] Server is Start!")
        while(True):
            if (self._isClose):
                self._socket.close()
                break
            sock, addr = self._socket.accept()
            print("[System] New Connection -- (" + sock + ", " + addr + ")")
            processThread = threading.Thread(target=self.serverFunc, name="processThread", args=(sock, addr))
            processThread.start()
        print("[System] Server is Close!")          

    #服务器基类基本运行函数
    def run(self):
        serverListenThread = threading.Thread(target=self.serverListen, name="ServerCmdThread")
        serverListenThread.start()
        while (self._isClose == False):
            userCmd = input()
            serverListenThread.
            self.cmdList(userCmd)

    def serverFunc(self):
        pass

    #子类继承实现服务器命令集
    def cmdList(self, cmd = ""):
        pass 
        


if __name__ == "__main__":
    print("please do not run this file directly!")