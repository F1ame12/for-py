#!/usr/bin/python3
# -*- coding=utf-8 -*-
import os
import wx
import guiDesign.noname as noname

app = wx.App(False)

mainwindow = noname.LoginWindow(None)
mainwindow.Show(True)

app.MainLoop()