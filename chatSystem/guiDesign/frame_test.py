#!/usr/bin/python3
# -*- coding=utf-8 -*-

import qqliteframe
import wx
import sys
import os
import threading

sys.path.append(os.path.join(os.path.abspath('.'), 'chatSystem'))

import chatserver

class LoginWindow(qqliteframe.LoginFrame):

    def __init__(self, parent):
        qqliteframe.LoginFrame.__init__(self, parent)
        self.server = chatserver.ChatServer()
    
    def loginEvent(self, event):
        threading.Thread(target=self.server.start).start()
        # self.server.start()
        print('test')
        self.Hide()

app = wx.App(False)

frame = LoginWindow(None)

frame.Show(True)


app.MainLoop()
