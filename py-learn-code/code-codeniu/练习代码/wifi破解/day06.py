# import sys

# pakeage_path = "F:\\develop\\Program Files\\python37\\lib\\site-packages"
# python37_path = "F:\\develop\\Program Files\\python37"
# work_path = "f:\\develop\\PythonWorkspace\\for-py\\py-learn-code\\code-codeniu\\练习代码"

import pywifi
import time

wifi = pywifi.PyWiFi()
print(wifi)

iface = wifi.interfaces()[0]
print(iface.name())

#print(iface.status())
#const.IFACE_CONNECTED
if iface.status()==4:
    print("连接")
else:
    print("未连接")


#扫描附近的wifi
def getNearbyWifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)
    result = iface.scan_results()
    print(set(result))
    
    l_list = []

    # for nwifi in result:
    #     nwifi_str = str(nwifi.ssid)
    #     print(nwifi_str)
    for nwifi in range(len(result)):
        # print(nwifi,result[nwifi].ssid,result[nwifi].signal)
        l_list.append(result[nwifi].ssid)

    l_list = list(set(l_list))
    l_list.sort()    
    for i in range(len(l_list)):
        print(l_list[i])


getNearbyWifi()