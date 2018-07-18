#pip install comtypes
#pip install pywifi
#pip install tests
#引入wifi模块
import pywifi
#引入wifi模块部分变量
from pywifi import const
'''
环境安装路径
import sys
#在E:\python 3.6\Lib\site-packages目录下建立mypath.pth文件来保证模块导入的路径正确
print(sys.path)
'''
def getWifi():
    #获得Wifi接口
    wifi = pywifi.PyWiFi()
    print(wifi)
    #获得第一个无线网卡
    iface = wifi.interfaces()[0]
    print(iface.name())
getWifi()