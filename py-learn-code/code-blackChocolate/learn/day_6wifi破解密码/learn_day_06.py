#pip install comtypes
#pip install pywifi
#pip install tests
#引入wifi模块
import pywifi
#引入wifi模块部分变量
from pywifi import const
import time
import itertools
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
    #获得无线网卡的名字
    #print(iface.name())
    #校验系统代码格式Ctrl+Alt+L
    #获得无线网卡的连接状态 0未连接 4连接
    print(iface.status())
    if iface.status() == const.IFACE_CONNECTED:
        print("连接")
    else:
        print("未连接")

getWifi()

#扫描附近的wifi
def nearby():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    #扫描wifi
    iface.scan()
    time.sleep(5)
    result = iface.scan_results()
    llist = []
    for nwifi in range(len(result)):
       llist.append(result[nwifi].ssid)
    llist = list(set(llist))
    llist.sort()
    for i in range(len(llist)):
        print(llist[i])

nearby()