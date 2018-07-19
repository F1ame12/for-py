import socket
import threading
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('0.0.0.0',9999))
#开始监听端口，参数表示等待连接的最大数量
s.listen(1000)
print("Waiting for connection...")

#每个连接都必须创建一个新线程来处理
def tcplink(sock,addr):
    print("Accept new connection from %s:%s..."%addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            sock.send(('远方服务器不想理你，一脚踹开了你').encode('utf-8'))
            break
        sock.send(('老牛傻逼,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed'%addr)

#接受来自客户端的连接 accept()会等待并返回一个客户端的连接
while True:
    #接受一个新连接
    sock,addr=s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



        