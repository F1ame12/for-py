#!usr/bin/python3

#pip install keyboard
#pip install pywin32
'''
安装包：
keyboard：键盘监听
Pillow：图片处理
pywin32：直接操控win32程序

功能描述：使用键盘监听，按下alt+ctrl+a
再按下enter的时候从粘贴板中复制截图到项
目目录中。以picture.png命名
'''
import keyboard
from PIL import Image
from PIL import ImageTk
from PIL import ImageGrab
import time
import sys
import mylogger
import random

log = mylogger.getLogger(loglevel = 'debug',name = 'keyboard')

def screenShot(path):
    #开始截图
    if keyboard.wait('alt+ctrl+a')==None:
        #截图的结束
        if keyboard.wait('enter')==None:
            time.sleep(0.01)
            log.debug('完成图片的保存')
            img=ImageGrab.grabclipboard()
            #保存到粘贴板
            randomNum = str(random.randrange(100))
            url = path+randomNum+'.png'
            print(url)
            img.save(url)
    #获取图片

def screenStart():
    count=1
    flag = 'yes'
    path = input('输入路径:')
    while  flag=='yes':
        print('按任意键键退出程序，按ctal+alt+a开始截图，enter结束')
        print("开始第%d次截图"%count)
        count+=1
        screenShot(path)
        flag = input('是否继续截图（yes/no）：')             
screenStart()