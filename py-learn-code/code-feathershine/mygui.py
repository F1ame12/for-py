#!/usr/bin/python3
# -*- codng=utf-8 -*-

from tkinter import *

def main():
    app = Application()
    app.mainloop()
    return 

class Application(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWedgets()

    def createWedgets(self):
        self.master.geometry('200x400')
        label = Label(self, text='hello world!')
        label.pack()
        button = Button(self, text='Close', command=self.quit)
        button.pack()
        

if __name__ == '__main__':
    main()


