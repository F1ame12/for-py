#pip install keyboard  监控键盘
import keyboard
from PIL import ImageGrab
import time
import sys
import os
import win32con
import win32clipboard as w

class GetTexts(object):
    '''
    把文字复制到剪切板
    '''
    def getText(self):
        #打开剪切板
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODE=TEXT)
        w.CloseClipboard()
        return d

    def setText(self,aStr):
        w.OpenClipboard()
        w.EmptyClipboard()
        d = w.SetClipboardData(win32con.CF_UNICODETEXT,aStr)
        w.CloseClipboard()

#GetTexts().setText('123')
d=GetTexts().getText()
print(d)
        
'''
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
    for n in range(5):
        print(sys.maxsize)
screenShot()
'''
print(sys.path)