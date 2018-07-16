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
'''
from tkinter import *
import random
#创建一个窗口
tk = Tk()
#设置窗体的标题
tk.title("我的第一个窗体")
#设置窗体的尺寸
tk.geometry('600x300')
#窗口大小是否可调整  分别表示x,y两个方向，0表示不可变，1表示可变
tk.resizable(1,1)
def btnClick():
    print("点击了按钮")
    #退出（通常配合响应事件使用）
    tk.quit()
#向窗口中添加画布
canvas = Canvas(tk,width=200,height=200)
canvas.pack()

#绘制一条线
canvas.create_line(10,10,100,100,width=3,fill="red",dash=10)
#绘制一个圆
canvas.create_oval(10,10,100,100)

#绘制一个矩形
myColor = ["red","blue","yellow","green","pink","gray","cyan"]
def ran(width,height,myColor):
    x = random.randrange(width)
    y = random.randrange(height)
    x1 = y +random.randrange(width)
    y1 = x +random.randrange(height)
    canvas.create_rectangle(x, y, x1, y1,fill=myColor,stipple="gray25")

for num in range(100):
    ran(200,200,myColor[num%7])



#绘制一个多边形
points = [90,10,70,22,70,36,94,50,118,30]
canvas.create_polygon(points, fill='', width=3,outline="pink")

#向窗体中添加组件
B = Button(tk,text="我是按钮",command = btnClick)

L = Label(tk,text = "这是个Label")
R = Radiobutton(tk,text = "这是个RadioButton")
T = Text(tk)
S = Scrollbar(tk,orient=HORIZONTAL)

#设置布局
B.pack(side = BOTTOM)

L.pack(side = RIGHT)
R.pack()
T.pack()
S.pack()

#进入主循环  等待操作
tk.mainloop()
'''
from tkinter import *
from PIL import Image,ImageTK
tk = Tk()
tk.title("我的第二个窗体")
tk.resizable(1,1)
canvas = Canvas(tk,width=500,height=500)
#绘制一张图片
canvas.pack() 
tk.mainloop()