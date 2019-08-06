#pip install aip    百度提供的接口
#pip install configparser 参数解析
from aip import AipOcr
import configparser
import os

class BaiDuApi(object):
    def __init__(self,filePath):
        target=configparser.ConfigParser()
        target.read(filePath,encoding='utf-8-sig')

        app_id = target.get("我的密码","app_id")
        api_key = target.get("我的密码","api_key")
        secret_key = target.get("我的密码","secret_key")

        #print(app_id,api_key,secret_key)
        self.client=AipOcr(app_id,api_key,secret_key)

    def getPicture(self,filePath):
        with open(filePath,'rb') as fp:
            return  fp.read()

    def picture2Texts(self,filePath):
        img = self.getPicture(filePath)
        texts=self.client.basicGeneral(img)
        print(texts)
        allText = ''
        for word in texts['words_result']:
            allText +=word.get("words",'')+"\n"
        #print(allText)
        return allText



filePath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","文字识别","password.ini")
# print(filePath)
# BaiDuApi(filePath)
imgPath=os.path.join(os.path.abspath("."),"py-learn-code","code-codeniu","练习代码","文字识别","img.png")

if __name__=='__main__':    
    BaiDuApi(filePath).picture2Texts(imgPath)
