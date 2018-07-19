global Text_Show
#调用人工智能对话的函数，返回人工智能回答
def AI_Talk(s): 
    response = requests.post("http://www.tuling123.com/openapi/api", data={ "key": "5636c0854e88430383a861151bf764ca", "info": s, "userid": "123456" })
    response = response.json() 
    answer=response['text'] 
    return answer
#线程二函数，用来进行对话
def Sever_Thread(sock,caddr): 
    Text_Show.insert('end',"客户端@"+str(caddr[1])+"已连接!\n") 
    while True: 
        # 接收数据 
        data = str(sock.recv(1024).decode('UTF-8')) 
        if data == "quit": 
            Text_Show.insert('end',"客户端@"+str(caddr[1])+"终止了对话\n") 
            Text_Show.see(tkinter.END) break 
        else: 
            Text_Show.insert('end',"来自客户端@"+str(caddr[1])+"的消息为："+data+'\n') 
            Text_Show.see(tkinter.END) 
        #发送数据 
        time.sleep(0.2) 
        data=AI_Talk(data) 
        #data = '请输入发送至客户端的数据: 123123' #如果要手动输入的话就要设置好线程sleep时间不然还没有输入，就已经到其他线程了，就会发不出去。 
        sock.sendall(bytes(data, 'UTF-8')) 
        sock.close()
#线程一函数，监听端口，一旦有客户端接入，开启线程二
def Sever_Accept(ss):
    while True: 
        sock,caddr=ss.accept() 
        Thread2 = threading.Thread(target=Sever_Thread, args=(sock,caddr)) 
        Thread2.daemon=True 
#线程守护 Thread2.start()#服务器初始化
def Sever_Init(): 
    HOST = '' PORT = 4700 ADDR = (HOST, PORT) 
    ss = socket(AF_INET, SOCK_STREAM, 0) 
    ss.bind(ADDR) ss.listen(20) 
    #允许最大监听数 
    Thread1=threading.Thread(target=Sever_Accept,args=(ss,)) 
    Thread1.daemon=True 
    #线程守护 
    Thread1.start()
#主函数
if __name__ == "__main__": 
    root=tkinter.Tk() root.title("聊天小程序服务器端 ") 
    frame1=Frame(root) frame1.pack() 
    IP_Show_Label=Label(frame1,text="默认IP:127.0.0.1\n默认端口为6000\n无法更改!!!") 
    IP_Show_Label.pack(side='left') 
    frame2=Frame(root) frame2.pack() 
    Text_Show=ScrolledText(frame2,width=100,height=30) 
    Text_Show.bind("<KeyPress>",lambda e:"break") 
    Text_Show.pack(side="bottom",fill = 'both', expand = True) 
    Sever_Init() root.mainloop()