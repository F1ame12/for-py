#!/usr/bin/python3
# -*- codeing=utf-8 -*-

import singup_fame_design
import wx
import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'),'chatSystem'))
import mylogger

class SingupWindow(singup_fame_design.SingupFrame):
    LOG = mylogger.getLogger('SingupWindow')

    def __init__(self,parent):
        singup_fame_design.SingupFrame.__init__(self,parent)


app = wx.App(False) 
frame = SingupWindow(None) 
frame.Show(True) 
#start the applications 
app.MainLoop()     