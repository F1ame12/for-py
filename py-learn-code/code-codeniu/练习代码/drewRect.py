#!usr/bin/python3
import random
from tkinter import *
from PIL import Image, ImageTK

myColor = ["red","blue","yellow","green","pink","gray","cyan"]

def ran(width,height,myColor):
    x = random.randrange(width)
    y = random.randrange(height)
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    canvas_test.create_rectangle(x,y,x1,y1,fill = myColor,stipple="gray12")
    canvas_test.pack()

tk = Tk()
tk.title("画图")
tk.resizable(1,1)

canvas_test = Canvas(tk,width=500,height=500,bg="pink")


canvas_test.pack()
tk.mainloop()
