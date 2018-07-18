#pip install keyboard  监控键盘
import keyboard
from PIL import ImageGrab
import time
import sys
import os
import win32con
import win32clipboard as w
from 文字识别 import BaiDuAPI
from 剪切板 import GetTexts
#截图方法
def screenShot():
    #截图的开始
    if keyboard.wait('alt+ctrl+a') == None:
        #截图的结束
        if keyboard.wait('enter')   == None:
            time.sleep(0.01)
            #获取图片
            img  = ImageGrab.grabclipboard()
            #保存到项目中
            img.save("for-py/py-learn-code/code-blackChocolate/learn/day_5文件识别/picture.png")

for n in range(sys.maxsize):      
    print("第%d次截图"%(n+1))
    screenShot()
    #将图片转换成文本
    str =  BaiDuAPI("for-py/py-learn-code/code-blackChocolate/learn/day_5文件识别/password.ini").picture2Texts("for-py/py-learn-code/code-blackChocolate/learn/day_5文件识别/picture.png")
    print(str)
    #将识别的文字添加到剪切板
    GetTexts().setText(str)
    flag = input()
    flag = input("是否继续截图（Y/N）")
    if flag == "N":
        break
'''
print(sys.path)
'''