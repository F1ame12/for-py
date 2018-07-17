#!usr/bin/python3
# -*- coding=utf-8 -*-

import os
import PIL
import tkinter
# from tkinter import *
from PIL import Image

class App(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidget()
    def createWidget(self):
        label = tkinter.Label(self, text='hello world')
        label.pack()

# pic = Image.open(os.path.join(os.path.abspath('.'), '/code-codeniu/练习代码/1.gif'))
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'), 'py-learn-code','code-codeniu','练习代码','1.gif'))
app = App()
# app.mainloop()
