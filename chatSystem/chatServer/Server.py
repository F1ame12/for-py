#!/usr/bin/python3
# -*- coding=utf-8 -*-

import baseServer

class ChatServer(baseServer.baseServer):
    def __init__(self, host = baseServer.HOST, port = baseServer.PORT, maxSocket = 10):
        self._host = host
        self._port = port
        self._maxSocketNum = maxSocket
    
    def cmdList(self, cmd = ""):
        if (cmd == "quit"):
            self._isClose = True
        else:
            print("[System-Cmd] Not Correct Cmd!")


if __name__ == "__main__":
    print("please do not run this file directly!")