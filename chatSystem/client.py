#!/usr/bin/python3
# -*- coding=utf-8 -*-

import socket
import sys
import json
import threading
import mylogger
import baseinfo
import time
import tkinter
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import *



def main():
    cmd = input('输入1，2，3')
    client = ChatClient()
    if cmd == '1':
        client.uid = 'client1'
    elif cmd == '2':
        client.uid = 'client2'
    elif cmd == '3':
        client.uid = 'client3'
    elif cmd == '0':
        return
    client.start()

class ChatClient(object):

    LOG = mylogger.getLogger('Client')
    
    HOST = '140.143.57.234'
    PORT =  4700
    ADDR = (HOST, PORT)
    Text_Show = ''
    Send_Show = ''
    Send_Show2 = ''

    def __init__(self):
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.uid = 'client2'

    def setClientUid(self, uid):
        self.uid = uid

    def checkNet(self):
        """检查网络是否通畅"""
        timer = time.time()
        self.LOG.info('timer = %s' % timer)

        check_info = baseinfo.Info()
        check_info.setType('check')
        check_info.setUid(self.uid)
        
        check_info_dict = baseinfo.info2Dict(check_info)
        check_info_byte = json.dumps(check_info_dict).encode('utf-8')
        self.LOG.debug(check_info_byte)
        while True:
            nowtime = time.time()
            self.LOG.info('nowtime = %s' % nowtime)
            if nowtime - timer >= 3.0:
                return False
            self.client_sock.sendto(check_info_byte, self.ADDR)
            time.sleep(0.5)
            recv_data = self.client_sock.recv(1024)
            if recv_data:
                check_result_dict = json.loads(recv_data.decode('utf-8'))
                check_result = baseinfo.dict2Info(check_result_dict)
                print(recv_data)
                if check_result.msg == 'ok':
                    return True
    
    def waitMsg(self):
        while True:
            print("---测试客户端")
            self.LOG.info('等待接受信息')
            recv_data = self.client_sock.recv(1024)
            if recv_data:
                if self.Send_Show2.get() == '':
                    self.Text_Show.insert(tkinter.END,"人工智障机器人："+":"+time.strftime('%H:%M:%S',time.localtime(time.time()))+"\n",'green')
                    self.Text_Show.insert(tkinter.END,str(recv_data.decode('utf-8'))+'\n')
                    continue
                info_dict = json.loads(recv_data.decode('utf-8'))
                info = baseinfo.dict2Info(info_dict)
                msg = info.getMsg()
                senduid = info.getUid()
                self.Text_Show.insert(tkinter.END,senduid+":"+time.strftime('%H:%M:%S',time.localtime(time.time()))+"\n",'green')
                self.Text_Show.insert(tkinter.END,msg+'\n')
                self.LOG.info('[%s] %s' % (senduid, msg))
            else:
                self.Text_Show.insert(tkinter.END,"用户:"+self.Send_Show2.get()+"未上线\n")

    def sendMsg(self):
        senduid = self.Send_Show2.get()
        msg = self.Send_Show.get()
        self.Text_Show.insert(tkinter.END,"我："+time.strftime('%H:%M:%S',time.localtime(time.time()))+"\n",'green')
        self.Text_Show.insert(tkinter.END,self.Send_Show.get()+"\n")
        info = baseinfo.Info()
        info.setMsg(msg)
        info.setType('msg')
        info.setUid(self.uid)
        info.setRecvUid(senduid)
        info_dict = baseinfo.info2Dict(info)
        info_byte = json.dumps(info_dict).encode('utf-8')
        self.client_sock.sendto(info_byte, self.ADDR)
    
    '''验证登陆信息'''
    def verifyLogin(self,msg):
        info = baseinfo.Info()
        info.setType('login')
        info.setUid(self.uid)
        info.setMsg(msg)
        info_dict = baseinfo.info2Dict(info)

        # print(info,type(info))
        # print(info_dict,type(info_dict))
        info_byte = json.dumps(info_dict).encode('utf-8')
        self.client_sock.sendto(info_byte, self.ADDR)

        time.sleep(0.5)
        while True:
            result = self.client_sock.recv(1024)
            if result:
                result = result.decode('utf-8')
            result = json.loads(result)
            result = baseinfo.dict2Info(result)
            if result.getMsg() == '0':
                return False
            else:
                return True

    def sendLogOutMsg(self):
        info = baseinfo.Info()
        info.setType('exit')
        info.setUid(self.uid)
        info_dict = baseinfo.info2Dict(info)
        info_byte = json.dumps(info_dict).encode('utf-8')
        self.client_sock.sendto(info_byte, self.ADDR)

    def start(self):
        self.LOG.info('客户端开启')
        check_status = self.checkNet()
        self.LOG.info('网络验证结果: %s' % check_status)
        if check_status == True:

            #初始化GUI
            root=tkinter.Tk()
            root.title("聊天小程序客户端 ")
            #顶部显示部分
            frame1=Frame(root)
            frame1.pack()
            IP_Show_Label=Label(frame1,text="qqlite")
            IP_Show_Label.pack(side='left')

            #中部聊天框显示部分
            frame2=Frame(root)
            frame2.pack()
            self.Text_Show=ScrolledText(frame2,width=70,height=15)
            self.Text_Show.bind("<KeyPress>",lambda e:"break")
            self.Text_Show.pack(side="bottom",fill = 'both', expand = True)
            #底部消息发送部分
            frame3=Frame(root)
            frame3.pack()
            e3=StringVar()
            self.Send_Show=Entry(frame3, textvariable=e3,width=40)
            e4= StringVar()
            self.Send_Show2 = Entry(frame3, textvariable=e4,width=20)
            buttontext2 = tkinter.StringVar()
            buttontext2.set('发送')
            button_Send = tkinter.Button(frame3,width=10, textvariable=buttontext2,command=self.sendMsg)
            self.Send_Show.pack(side="left")
            self.Send_Show2.pack(side="left")
            button_Send.pack(side="left")
            frame3.pack()

            msg_thread = threading.Thread(target=self.waitMsg)
            msg_thread.start()

            root.mainloop()
            self.sendLogOutMsg()
           

         

if __name__ == '__main__':
    main()

