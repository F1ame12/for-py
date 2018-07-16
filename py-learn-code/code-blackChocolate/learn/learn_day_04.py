'''
a = 1                   #全局变量
def func():     
    b = 2               #局部变量
    print(a)
    def inner():
        c = 3           #更局部的变量
        print(a)
        print(b)
        print(c)
    inner()
func()
'''
'''
a = 1
def test():
    a+=1    #a=a+1  根据查找顺序，先查右边的局部变量，发现没有，报错
test()
'''
'''
name='python'
def test1():
    print(name)
def test2():
    test1()
test2()

name = 'python'
def test():
    name = 'java'
    def test2():
        name = 'php'
        print(name)
    test2()
test()
'''
'''
name='python'
def test1():
    name = 'php'
    print(name)
def test2():
    test1()
test2()

name = 'Python'
def test1():
    name = 'java'
    print(name)
    test2()
def test2():
    print(name)

test1()

class student(object):
    num  = 3

print(student.num)
student.num = 4
print(student.num)
student1 = student()
student1.num = 5
print(student.num)
'''
from tkinter import *

#创建一个窗口
tk = Tk()
#设置窗体的标题
tk.title("我的第一个窗体")
#设置窗体的尺寸
tk.geometry('300x150')
#窗口大小是否可调整  分别表示x,y两个方向，0表示不可变，1表示可变
tk.resizable(1,1)
def btnClick():
    print("点击了按钮")
    #退出（通常配合响应事件使用）
    tk.quit()
#向窗体中添加组件
B = Button(tk,text="我是按钮",command = btnClick)
L = Label(tk,text = "这是个Label")
R = Radiobutton(tk,text = "这是个RadioButton")
T = Text(tk)
S = Scrollbar(tk,orient=HORIZONTAL)
#设置布局
B.pack()
L.pack()
R.pack()
T.pack()
S.pack()
#进入主循环  等待操作
tk.mainloop()