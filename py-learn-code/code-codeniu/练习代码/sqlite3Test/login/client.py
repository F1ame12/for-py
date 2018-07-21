import socket

def connectToServe(user,pas):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1',9999))
    # 接收欢迎消息:
    return_msg = s.recv(1024).decode('utf-8')
    
    s.send(user.encode('utf-8'))
    s.send(pas.encode('utf-8'))

    s.send(b'exit')
    s.close()
    return return_msg

connectToServe(1,2)