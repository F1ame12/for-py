#!usr/bin/python3
import random
from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

# myColor = ["red","blue","yellow","green","pink","gray","cyan"]

# def ran(width,height,myColor):
#     x = random.randrange(width)
#     y = random.randrange(height)
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     canvas_test.create_rectangle(x,y,x1,y1,fill = myColor,stipple="gray12")
#     canvas_test.pack()

tk = Tk()
tk.title("画图")
tk.resizable(1,1)

canvas_test = Canvas(tk,width=700,height=700,bg="#ED7457")

img = Image.open("D:/1.gif")
image = ImageTk.PhotoImage(img)
myImg = canvas_test.create_image(200,200,image=image)
canvas_test.pack()

for x in range(60):
    canvas_test.move(myImg,5,5)
    tk.update_idletasks()#快速重画屏幕
    tk.update()
    time.sleep(0.5)
    
tk.mainloop()

'''

#__*__coding:utf-8__*__
#python3
from tkinter import *
import random
import time
 
class Ball:#小球的类 
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas#传递画布值
        self.paddle=paddle#把挡板传递进来
        self.id=canvas.create_oval(10,10,25,25,fill=color)#画椭圆并且保存其ID
        self.canvas.move(self.id,245,100)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)#随机化列表
        self.x=start[0]
        self.y=-3
        self.canvas_heigh=self.canvas.winfo_height()#获取窗口高度并保存
        self.canvas_width=self.canvas.winfo_width()
        
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#返回相应ID代表的图形的当前坐标（左上角和右上角坐标）
        #使得小球不会超出窗口
        pad=self.canvas.coords(self.paddle.id)#获取挡板的坐标
        if pos[1]<=0 :
            self.y=3
        if pos[3]>=self.canvas_heigh or(pos[3]>=pad[1] and pos[2]>=pad[0] and pos[2]<=pad[2]):
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
            
class Paddle:#挡板的类
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.color=color
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.canvas_width=self.canvas.winfo_width()
        self.l=0
        self.r=0
 
    def draw(self):
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.l=0   
        if pos[2]>=self.canvas_width:
            self.r=0
            
    def turn_left(self,event):
        self.canvas.move(self.id,self.l,0)
        self.l=-20
 
    def turn_right(self,event):
        self.canvas.move(self.id,self.r,0)
        self.r=20
  
 
            
                   
tk=Tk()
tk.title('Game')
tk.resizable(0,0)#使得窗口大小不可调整
tk.wm_attributes('-topmost',1)#包含画布的窗口放在其他窗口的前面
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)#后面两个参数去掉边框
canvas.pack()
tk.update()
paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red')
 
canvas.bind_all('<KeyPress-Left>',paddle.turn_left)#绑定方向键
canvas.bind_all('<KeyPress-Right>',paddle.turn_right)
 
while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()#快速重画屏幕
    tk.update()
    time.sleep(0.01)
'''