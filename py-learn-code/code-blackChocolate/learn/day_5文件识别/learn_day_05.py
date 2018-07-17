#pip install keyboard  监控键盘
import keyboard

def screenShot():
    #截图的开始
    if keyboard.wait('alt+ctrl+a') == None:
        #截图的结束
        if keyboard.wait('enter')   == None:
            print("截图结束")
    #获取图片

screenShot()
