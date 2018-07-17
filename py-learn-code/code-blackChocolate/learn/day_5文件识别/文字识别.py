#pip install aip            #百度提供的接口
#pip install configparser   #参数解析
from aip import AipOcr
import configparser

class BaiDuAPI(object):
    #初始化方法，构造方法
    def __init__(self,filePath):
        #获得参数解析方法
        target = configparser.ConfigParser()
        #读取文件,并设置解码格式
        target.read(filePath,encoding="utf-8-sig")
        #获取【我的密码】下的【app_id】的值
        app_id = target.get('我的密码','app_id')
        app_key = target.get('我的密码','api_key')
        secret_key = target.get('我的密码','secret_key')
        print(app_id,app_key,secret_key)
        self.client = AipOcr(app_id,app_key,secret_key)
        
BaiDuAPI("for-py/py-learn-code/code-blackChocolate/learn/day_5文件识别/password.ini")