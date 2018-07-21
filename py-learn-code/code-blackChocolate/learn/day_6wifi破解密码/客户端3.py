import socket
import time
import tkinter
from tkinter.scrolledtext import ScrolledText
import threading
import requests
import tkinter
from socket import *
from tkinter import *

global cs,Text_Show,Send_Show

#发送按键的函数
def Click_Send():
    sendData=Send_Show.get() #获取输入内容
    if sendData == 'quit':
        Text_Show.insert(tkinter.END,"与服务器连接已断开"+"\n")
        Text_Show.see(tkinter.END)
        cs.sendall(bytes(sendData, encoding="utf8"))
        cs.close()
    else:
        Text_Show.insert(tkinter.END,"客户端:"+sendData+"\n")
        Text_Show.see(tkinter.END)
        cs.sendall(bytes(sendData, encoding="utf8"))
    Send_Show.delete(0,END)

#线程函数，循环接受客户端消息
def Receive_Data():
    while True:
        accept_data = str(cs.recv(1024), encoding="utf8")
        Text_Show.insert(tkinter.END,"服务器:"+accept_data+"\n")
        Text_Show.see(tkinter.END)

#主函数
if __name__ == "__main__":
    #初始化GUI
    root=tkinter.Tk()
    root.title("聊天小程序客户端 ")
    #顶部显示部分
    frame1=Frame(root)
    frame1.pack()
    IP_Show_Label=Label(frame1,text="本程序默认IP:127.0.0.1\n默认端口为6000\n无法更改!!!")
    IP_Show_Label.pack(side='left')

    #中部聊天框显示部分
    frame2=Frame(root)
    frame2.pack()
    Text_Show=ScrolledText(frame2,width=70,height=15)
    Text_Show.bind("<KeyPress>",lambda e:"break")
    Text_Show.pack(side="bottom",fill = 'both', expand = True)
    #底部消息发送部分
    frame3=Frame(root)
    frame3.pack()
    e3=StringVar()
    Send_Show=Entry(frame3, textvariable=e3,width=60)
    buttontext2 = tkinter.StringVar()
    buttontext2.set('发送')
    button_Send = tkinter.Button(frame3,width=10, textvariable=buttontext2,command=Click_Send )
    Send_Show.pack(side="left")
    button_Send.pack(side="left")
    frame3.pack()

    #初始化TCP协议
    HOST='127.0.0.1'
    PORT=4700
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    cs=socket(AF_INET,SOCK_DGRAM)
    cs.connect(ADDR)
    thread=threading.Thread(target=Receive_Data)
    thread.start()

    root.mainloop() 