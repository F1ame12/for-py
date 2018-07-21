#!/usr/bin/python3
# -*- coding=utf-8 -*-

import qqliteframe
import wx
import sys
import os
import threading
import json
from tkinter import messagebox
from tkinter import *


sys.path.append(os.path.join(os.path.abspath('.'), 'chatSystem'))

import client
import mylogger

class LoginWindow(qqliteframe.LoginFrame):

    LOG = mylogger.getLogger('LoginWindow')

    root = Tk()

    def __init__(self, parent):
        qqliteframe.LoginFrame.__init__(self, parent)
        self.c = client.ChatClient()
    
    def loginEvent(self, event):
        username = self.user_id_input.GetValue()
        password = self.user_pwd_input.GetValue()
        data = {'username':username,'password':password}
        data_str = json.dumps(data)
        data_byte = data_str.encode('utf-8')

        self.LOG.info(username)
        self.LOG.info(password)
        #验证用户和密码
        if username=='':
            messagebox.askokcancel('error', '用户名不能为空')
        elif password=='':
            messagebox.askquestion('error', '密码不能为空')
        else:
            netState = self.c.checkNet()
            if netState:
                #服务器连接正常 向服务器发送用户信息
                print('服务器连接正常 向服务器发送用户信息')
                result = self.c.verifyLogin(data)
                if result:
                    threading.Thread(target=self.c.start).start()
                    self.Hide()
                else:
                    messagebox.askquestion('error', '账号或密码错误')
            else:
                messagebox.askquestion('error', '检查服务器状态')
            # threading.Thread(target=self.client.start).start()
            # self.server.start()
            # print('test')

app = wx.App(False)

frame = LoginWindow(None)

frame.Show(True)


app.MainLoop()
