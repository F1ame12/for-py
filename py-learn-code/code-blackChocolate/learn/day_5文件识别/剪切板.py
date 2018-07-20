import win32con
import win32clipboard as w

class GetTexts(object):
    #把文字复制到剪切板
    def getText(self):
        #打开剪切板
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d
        

    def setText(self,aStr):
        w.OpenClipboard()
        w.EmptyClipboard()
        d = w.SetClipboardData(win32con.CF_UNICODETEXT,aStr)
        w.CloseClipboard()

#GetTexts().setText('123')
#d=GetTexts().getText()
#print(d)