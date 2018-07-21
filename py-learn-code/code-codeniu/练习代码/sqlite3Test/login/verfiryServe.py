import socket
import threading
import time
import dbUtil
import json

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))
#开始监听端口，参数表示等待连接的最大数量
s.listen(1000)
print("Waiting for connection...")

#每个连接都必须创建一个新线程来处理
def tcplink(sock,addr):
    print("Accept new connection from %s:%s..."%addr)
    # sock.send(b'serve:now you can send me some msg')

    data = sock.recv(1024).decode()#str

    

    while True:
        data = sock.recv(1024).decode()#str
        print('接收到的数据',data)
        data_dict = json.loads(data)
        print(data_dict,type(data_dict))
        time.sleep(1)

        #如果接受到的数据是'exit',就断开连接
        if data == '退出':
            sock.send(('主动断开连接请求已接受，已断开连接').encode('utf-8'))
            break
        
        sock.send(('此消息来自服务器').encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed'%addr)

#接受来自客户端的连接 accept()会等待并返回一个客户端的连接
while True:
    #接受一个新连接
    sock,addr=s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



        