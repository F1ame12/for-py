#!/usr/bin/python3
# -*- coding=utf-8 -*-
import keyboard
import mylogger
import os
import time
import win32con
import win32clipboard as w
from PIL import ImageGrab

log = mylogger.getLogger(loglevel='warning',name=__name__)

def screenShot():
    if keyboard.wait('alt+ctrl+q') == None:
        log.info('start grab')
        if keyboard.wait('enter') == None:
            time.sleep(1)
            im = ImageGrab.grabclipboard()
            if (im != None):
                log.info('snapshot is finished!')
            im.save('snapshot.png')


if __name__ == '__main__':
    print()
    screenShot()

