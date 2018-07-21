from tkinter import *
import os
from tkinter import messagebox
import socket
import json

root = Tk()
  
root.title("login")
root.geometry('400x300')
root.resizable(0,0)

#添加lable欢迎语
lable1 = Label(root,text = '欢迎使用qqlite即时通讯系统').pack()

#添加输入username，password文本
fm1 = Frame(root)
lable_username = Label(fm1,text = 'username').pack(side=LEFT)
entry_content_username = StringVar()
entry_username = Entry(fm1,textvariable = entry_content_username)
entry_content_username.set('请输入……') 
entry_username.pack(side=LEFT)
fm1.pack(side=TOP, fill=NONE, expand=YES)

fm2 = Frame(root)
lable_password = Label(fm2,text = 'password').pack(side=LEFT)
entry_content_password = StringVar()
entry_content_password.set('')
entry_password = Entry(fm2,show='*',textvariable=entry_content_password).pack(side=LEFT)
fm2.pack(side=TOP, fill=NONE, expand=YES)


#显示用户列表
# users = dbUtil.findAll()
# listb = Listbox(root)
# for item in users:
#     listb.insert(0,item)
# listb.pack()


#退出按钮的点击事件
def btn_click_quit():
	print("点我quit")
	root.quit()

#登陆按钮的点击事件
def btn_click_ok():
    username=entry_content_username.get()
    password=entry_content_password.get()
    data = {'username':username,'password':password}
    data_str = json.dumps(data)
    data_byte = data_str.encode('utf-8')
    
    #验证用户和密码
    if username=='':
        messagebox.askokcancel('error', '用户名不能为空')
    elif password=='':
        messagebox.askquestion('error', '密码不能为空')
    else:
        #将账号密码发送到服务器
        
        msg = connectToServe(data_byte)
        print(msg)
        



#与服务器建立连接
def connectToServe(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1',9999))
    # 接收欢迎消息:
    return_msg = s.recv(1024).decode('utf-8')
    
    s.send(data)

    # s.send(('退出').encode('utf-8'))
    return return_msg

#添加退出按钮
quit_btn = Button(root,text = "quit",command=btn_click_quit).pack(side=LEFT)

#添加登陆按钮
quit_btn = Button(root,text = 'ok',command=btn_click_ok).pack(side=LEFT)



root.mainloop()
