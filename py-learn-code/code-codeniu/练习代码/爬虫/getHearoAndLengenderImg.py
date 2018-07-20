import os
import requests
import re#正则表达式的模块
import json

'''
1/获取js代码，取得每个英雄的id
2/拼接url地址
3/获取下载的图片的名称
4/下载图片
'''

#定义一个获取LOL图片的方法
def getLOLImage(url_js):
    # js = requests.get(url_js).content#content用于获取图片或视频的内容
    # html_js = js.decode()#字节转到字符串
    # print(type(html_js))
    # print(html_js)

    html_js = requests.get(url_js).text
    #print(html_js)
    #通过正则表达式匹配id .*?表示匹配所有   匹配的范围：keys与data之间的内容
    req = '"keys":(.*?),"data"'
    list_js = re.findall(req,html_js)
    # print(list_js)
    # print(type(list_js))
    
    #json:将str类型转换为字典类型
    dict_js = json.loads(list_js[0])
    # print(dict_js)

    #定义一个列表存放图片url
    pic_list = []


    #获得每个英雄的id
    for key in dict_js:
        # print(key)
        #拼接 ：英雄id+皮肤编号 假设每个英雄有20个皮肤
        for i in range(20):
            if i<10:
                hero_num = "00"+str(i)
            else:
                hero_num = "0"+str(i)

            hero_all = key+hero_num
            # print(hero_all)

            pic_url ="http://ossweb-img.qq.com/images/lol/web201310/skin/big"+hero_all+".jpg"
            # print(url)
            pic_list.append(pic_url)

    
    #获取英雄名字 生成图片名称
    imgPath = "C:\\Users\\Administrator\\Pictures\\LOL_Img\\"
    # print(dict_js.values())

    list_filePath = []

    for name in dict_js.values():
        # print(name)
        for i in range(20):
            file_path = imgPath+name+str(i)+'.jpg'
            list_filePath.append(file_path)
    
    #下载图片
    n = 0
    for picturl in pic_list:
        res = requests.get(picturl)
        n+=1
        if res.status_code == 200:
            #下载图片
            print("正在下载：",list_filePath[n])
            with open(list_filePath[n],'wb') as f:
                f.write(res.content)






url = 'http://lol.qq.com/biz/hero/champion.js'
getLOLImage(url)