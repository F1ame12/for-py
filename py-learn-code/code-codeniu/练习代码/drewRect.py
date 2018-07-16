
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
