
from tkinter import *
import subprocess
import os
import sys
counter = 0
def counter_label(label):
    counter = 0
    def count():
      global counter
      counter += 1
      #配置属性
      #区间大小
      label.config(width=10, height=2)
      #文本内容
      label.config(text=str(counter/3600%24/10)+str(counter/3600%24%10)+':'+str(counter/60%60/10)+str(counter/60%60%10)+':'+str(counter%60/10)+str(counter%60%10))
      #字体颜色
      label.config(fg='red')
      #label位置
      label.config(anchor='c')
      #after函数的第一个参数设置毫秒数后，调用count函数
      label.after(1, count)
    count()
 
def Pause():
  # subprocess.call("pause",shell=True)
  # os.system('pause')
  # input()
 
  sys.exit()
 
root = Tk()
root.title("计时器")
label = Label(root)
label.pack(side='left')
#查找方法或属性
# print help(label.config)
# print help(label.after)
counter_label(label)
button = Button(root, text='Stop', width=5, command=Pause,anchor='c').pack(side='right')#或command=root.destory小伙窗口
root.mainloop()