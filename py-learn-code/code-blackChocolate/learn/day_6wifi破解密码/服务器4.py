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
'''
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
'''
def main():
    server = ChatServer()
    # server.cmdStart()
    server.start()
    # a = {
    #     'client1': {
    #         'addr': ('127.0.0.1', 9999),
    #         'isalive': True
    #     },
    #     'client2':{
    #         'addr': ('127.0.0.1', 6666),
    #         'isalive': True
    #     }
    # }
    # for x in a.items():
    #     print(x)
    #     print(x[1].get('addr'))

class ChatServer(object):
    LOG = mylogger.getLogger('Server')
    HOST = '0.0.0.0'
    PORT = 4700
    Text_Show = ''
    def __init__(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.usermanager = UserConnManager()

    def checkOnlineWithCircle(self, connmanager):
        """每隔10分钟检查用户池用户在线状况"""
        user_list = connmanager.getList()
        threadlock = threading.RLock()
        if len(user_list) != 0:
            self.LOG.info('开始检查在线状况')
            threadlock.acquire()
            for x in user_list:
                if x[1].get('isalive') == False:
                    connmanager.rmfromList(x[0])
            threadlock.release()
        else:
            self.LOG.info('在线用户池为空 跳过此轮检查')

    def checkWebResponce(self, addr):
        check_info = baseinfo.Info()
        check_info.setType('check')
        check_info.setMsg('ok')
        check_info_dict = baseinfo.info2Dict(check_info)
        check_info_byte = json.dumps(check_info_dict).encode('utf-8')
        self.server_sock.sendto(check_info_byte, addr)
        self.LOG.info('服务端->客户端: %s' % check_info_byte)

    #线程守护 Thread2.start()#服务器初始化
    def Sever_Init(self):
        Thread1=threading.Thread(target=self.chatStart,args=()) 
        Thread1.daemon=True 
        #线程守护 
        Thread1.start()


    def chatStart(self):
        self.LOG.debug(self.server_sock)
        self.server_sock.bind((self.HOST, self.PORT))
        self.LOG.info('服务器绑定地址 %s' % str((ChatServer.HOST, ChatServer.PORT)))
        threading.Timer(10*60, self.checkOnlineWithCircle, (self.usermanager,)).start()
        self.LOG.info('用户池检查线程开始计时')
        self.LOG.info('等待客户端发送信息')
        stop_status = False
        while not stop_status:
            recv_data, recv_addr = self.server_sock.recvfrom(1024)
            if recv_data:
                jsonstr = recv_data.decode('utf-8')
                print("--",jsonstr)
                infodict = json.loads(jsonstr)
                info = baseinfo.dict2Info(infodict)
                if self.usermanager.isOnline(info.getUid()) == True:
                    self.usermanager.update2List(info.getUid(), recv_addr)
                if info.getType() == 'msg':
                    self.LOG.info('客户端->服务端: %s' % recv_data)
                    for x in self.usermanager.getList():
                        self.LOG.debug('当前用户列表: %s', x)
                    if self.usermanager.isOnline(info.getRecvUid()) == True:
                        self.Text_Show.insert('end',"来自客户端@"+str(info.getUid())+"发给"+str(info.getRecvUid())+"的消息为："+str(info.getMsg())+'\n') 
                        #print("-----这里是测试的" + str(self.usermanager.getAddr(info.getRecvUid())))
                        self.server_sock.sendto(recv_data, self.usermanager.getAddr(info.getRecvUid()))
                    else:
                        self.LOG.info('用户 %s 不在线' % info.getRecvUid())
                        self.server_sock.sendto(''.encode('utf-8'), recv_addr)
                        self.Text_Show.insert('end'," 用户 %s 不在线 " % info.getRecvUid()+'\n')
                    ####
                elif info.getType() == 'check':
                    self.checkWebResponce(recv_addr)
                    self.usermanager.add2List(info.getUid(), recv_addr)
                    self.Text_Show.insert('end',"客户端@"+str(info.getUid())+"已连接!\n") 
                elif info.getType() == 'exit':
                    self.usermanager.rmfromList(info.getUid())
                    self.LOG.info('客户端 %s 已离线' % info.getUid())
                    self.Text_Show.insert('end',"客户端@"+str(info.getUid())+"已断线!\n")
        

    def start(self):
        #窗体
        dict1 = {}
        root=tkinter.Tk()
        root.title("聊天小程序服务器端 ") 
        frame1=Frame(root) 
        frame1.pack() 
        IP_Show_Label=Label(frame1,text="默认IP:127.0.0.1\n默认端口为6000\n无法更改!!!") 
        IP_Show_Label.pack(side='left') 
        frame2=Frame(root) 
        frame2.pack() 
        self.Text_Show=ScrolledText(frame2,width=100,height=30) 
        self.Text_Show.bind("<KeyPress>",lambda e:"break") 
        self.Text_Show.pack(side="bottom",fill = 'both', expand = True) 
        self.Sever_Init() 
        root.mainloop()
        
        
        
            
    #TODO(feathershine) 未完成服务器控制台指令输入
    def cmdStart(self):
        def cmd(self):
            command = input()
            if command == 'quit':
                exit()
        threading.Thread(target=cmd, args=(self)).start()
        self.LOG.info('控制台线程开启')

class UserConnManager():
    """在线用户池"""
    online_user_list = {} #采用字典实现"列表"
    threadlock = threading.RLock()
    def __init__(self):
        pass

    def getList(self):
        return self.online_user_list.items()

    def getAddr(self, uid):
        return self.online_user_list[uid]['addr']

    def add2List(self, uid, addr):
        self.threadlock.acquire()
        self.online_user_list[uid] = {'addr': addr, 'isalive': True}
        """
        {
            {
                "uid": 'client1',
                "addr": ('127.0.0.1', 9999),
                "isalive": True
            },
            {
                "uid": 'client1',
                "addr": ('127.0.0.1', 9999),
                "isalive": True
            }
        }
        """
        self.threadlock.release()

    def rmfromList(self, uid):
        self.threadlock.acquire()
        self.online_user_list.pop(uid)
        self.threadlock.release()

    def update2List(self, uid, addr):
        self.add2List(uid, addr)

    def isOnline(self, uid):
        result = self.online_user_list.get(uid)
        if result == None:
            return False
        else:
            if result.get('isalive') == True:
                return True
            else:
                return False




if __name__ == '__main__':
    main()
