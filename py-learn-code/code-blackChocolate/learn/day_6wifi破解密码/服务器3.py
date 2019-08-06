import socket
import time
import tkinter
from tkinter.scrolledtext import ScrolledText
import threading
import requests
import tkinter
from tkinter import *
import sys
import json
import mylogger
import baseinfo


global cs,Text_Show,Send_Show
global list,dict1
#调用人工智能对话的函数，返回人工智能回答
def AI_Talk(s): 
    response = requests.post("http://www.tuling123.com/openapi/api", data={ 
        "key":"9b4b5244340c471abfe2abf52e96b3d9",
        "info":s,
        "useid":"123456"
    })
    response = response.json() 
    answer=response['text'] 
    return answer

#线程二函数，用来进行对话
def Sever_Thread(data,caddr,num,ss): 
    print(num)
    D = {num:caddr}
    dict1.update(D)

    Text_Show.insert('end',"客户端@"+str(caddr[1])+"已连接!\n") 
    #while True: 
    # 接收数据 
    if data == "quit": 
        Text_Show.insert('end',"客户端@"+str(caddr[1])+"终止了对话\n") 
        Text_Show.see(tkinter.END)
    else: 
        Text_Show.insert('end',"来自客户端@"+str(caddr[1])+"的消息为："+data+'\n') 
        Text_Show.see(tkinter.END) 
    data = data + str(caddr[1])
    list[num] = data
    #发送数据 
    time.sleep(0.2) 
    if dict1.get(1) != None:
        D = dict1.get(1)
        print(D)
        #data=AI_Talk(data) 
        #data = '请输入发送至客户端的数据: 123123' #如果要手动输入的话就要设置好线程sleep时间不然还没有输入，就已经到其他线程了，就会发不出去。 
        ss.sendto(data.encode('utf-8'),D)
    else:
        ss.sendto(("你的对方没有连接网络").encode('utf-8'),caddr)

#线程一函数，监听端口，一旦有客户端接入，开启线程二
def Sever_Accept(ss):
    num = -1
    while True: 
        num = num + 1
        data,caddr= ss.recvfrom(1024)
        data1 = data.decode('utf-8')
        Thread2 = threading.Thread(target=Sever_Thread, args=(data1,caddr,num,ss)) 
        Thread2.start() 

#线程守护 Thread2.start()#服务器初始化
def Sever_Init(): 
    HOST = '0.0.0.0' 
    PORT = 4700 
    ADDR = (HOST, PORT) 
    ss = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ss.bind(ADDR)
    #ss.listen(20) 
    #允许最大监听数 
    Thread1=threading.Thread(target=Sever_Accept,args=(ss,)) 
    Thread1.daemon=True 
    #线程守护 
    Thread1.start()
#主函数
if __name__ == "__main__": 
    list = [0,0,0,0,0]
    dict1 = {}
    root=tkinter.Tk()
    root.title("聊天小程序服务器端 ") 
    frame1=Frame(root) 
    frame1.pack() 
    IP_Show_Label=Label(frame1,text="默认IP:127.0.0.1\n默认端口为6000\n无法更改!!!") 
    IP_Show_Label.pack(side='left') 
    frame2=Frame(root) 
    frame2.pack() 
    Text_Show=ScrolledText(frame2,width=100,height=30) 
    Text_Show.bind("<KeyPress>",lambda e:"break") 
    Text_Show.pack(side="bottom",fill = 'both', expand = True) 
    Sever_Init() 
    root.mainloop()

