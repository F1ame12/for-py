#!/usr/bin/python3
# -*- coding=utf-8 -*-

import baseServer

import Server

server = baseServer.baseServer(baseServer.HOST, baseServer.PORT)

realserver = Server.ChatServer()

realserver.run()



