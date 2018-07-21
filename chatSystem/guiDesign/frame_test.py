#!/usr/bin/python3
# -*- coding=utf-8 -*-

import qqliteframe
import wx

app = wx.App(False)

frame = qqliteframe.LoginFrame(None)

frame.Show(True)


app.MainLoop()
