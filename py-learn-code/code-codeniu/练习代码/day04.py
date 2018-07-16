#!usr/bin/python3

#1.作用域
'''
def func1():
	enclosing = 1#enclosing作用域
	def fuc2():
	local = 2#局部作用域
'''
#2.图形用户界面
'''
import tkinter
from tkinter import *

#创建一个窗口
tk = tkinter.Tk()

tk.title("这里是标题")

tk.geometry('300x150')

tk.resizable(0,0)

def btnClick():
	print("点我quit")
	tk.quit()

#向窗体中添加组件
B = Button(tk,text = "按钮",command=btnClick)#两个参数 第一个参数是这个button所要添加到的窗体的位置
#设置布局
B.pack()
#进入主循环等待操作
tk.mainloop()
'''
#3.gui的小例子
'''
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
'''


#4.gui组建的应用

from tkinter import *
#from PIL import Image, ImageTk

#创建一个窗口
tk = Tk()
tk.title("这里是标题")
tk.geometry('400x600')
tk.resizable(0,0)

def btnClick():
	print("点我quit")
	tk.quit()

#1添加按钮组建


img=PhotoImage(file='D:/1.jpg')
btn_close = Button(tk,text = "退出按钮",image=img,command=btnClick,bg='red',activebackground='yellow')
btn_close.pack()

#2添加label组建
label_hello = Label(tk,text="换用来到python的世界")
label_bitmap = Label(tk,bitmap="error")
label_bitmap.pack()
label_hello.pack()

#3在Label中显示图片
# photo = PhotoImage(file="D:\\1.jpg")
# bmp = BitmapImage(file="logo.xbm")
# label_image = Label(tk,image = photo)
# image = Image.open("D:\\1.jpg")
# photo = ImageTk.PhotoImage(image)
# label_image = Label(tk,image = photo)
# label_image.pack()

#4一个单行文本输入框。可以用来接受用户的输入，但是只能输入一行。
e = StringVar() # 使用textvariable属性，绑定字符串变量e 
entry_username = Entry(tk,textvariable = e) 
e.set('请输入……') 
entry_username.pack()

#5密码隐藏
entry_passworld = Entry(tk,show="*") 
entry_passworld.pack()  

#6radioButton
def sel():
   selection = "You selected the option " + str(var.get())
   print(selection)
#创建整型变量，用于绑定，相同的整型变量是为同一组
var = IntVar()
R1 = Radiobutton(tk, text="Option 1", variable=var, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(tk, text="Option 2",variable=var,value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(tk, text="Option 3", variable=var, value=3,command=sel)
R3.pack( anchor = W)


#7.checkoutButton
checkBtn = Checkbutton(tk,text="this is a checkbtn").pack()

#8.canvas画布
canvas_test = Canvas(tk,width=400,height=300,bg="pink")
# canvas_test.create_line(10,10,100,100,width=3,fill="yellow",dash=1)
# canvas_test.create_line(100,100,150,150,width=3,fill="yellow",dash=255)
# canvas_test.create_line(150,150,300,0,width=3,fill="yellow",dash=255)
canvas_test.create_line(300,0,300,300,width=3,fill="yellow",dash=255)

canvas_test.create_rectangle(50,50,150,150,fill='blue',outline='green',width=2)

rt=canvas_test.create_rectangle(0,0,50,50,fill='black',outline='purple',stipple='gray12')

canvas_test.create_rectangle(0,0,10,10)
canvas_test.create_rectangle(10,10,60,60)
canvas_test.create_oval(10,10,60,60)

canvas_test.pack()

canvas_test.coords(rt,150,150,250,250)
#进入主循环等待操作
tk.mainloop()
