
import re
import requests
import json

'''
1.获取js文件源代码，取得每个英雄的ID
2.拼接URL地址
3.获取下载的图片名称  eg:Ezral0
4.下载图片
'''

#定义一个获取图片的方法
def getLOLImage():
    url_js ='http://lol.qq.com/biz/hero/champion.js'
    #content用于获取图片或者视频的内容
    #js = requests.get(url_js).content
    #byte -> str
    #html_js = js.decode()
    #print(html_js)
    html_js = requests.get(url_js).text
    #通过正则表达式匹配ID .*? 表示匹配所有
    req = '"keys":(.*?),"data"'
    list_js = re.findall(req,html_js)
    #print(type(list_js))
    #str - dict
    dict_js = json.loads(list_js[0])
    #print(type(dict_js))

    #定义一个列表存放url
    pic_list = []

    #获取每个英雄的ID
    for key in dict_js:
        #英雄ID
        #print(key)
        #拼接英雄ID加皮肤编号
        for i in range(20):
            if i < 10:
                hero_num = "00" + str(i) #001-009
            else:
                hero_num = "0"  + str(i) #010-0**
            #拼接ID与皮肤编号
            hero_all = key + hero_num
            #print(hero_num)
            #拼接皮肤网址
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big'+hero_all+'.jpg'
            #print(url)
            pic_list.append(url)

    #获取英雄的名字 生成图片名称
    path = 'C:\\Users\\VULCAN\\Desktop\\lolpic\\'

    #定义一个列表存放图片路径
    list_filePath = []
    #print(dict_js.values())  获得字典中所有的名字 values
    #print(dict_js.keys())    获得字典中所有的id key
    index = 0
    for name in dict_js.values():
        #print(name)
        #file_path = path + name 每个英雄只会有一个皮肤，被覆盖了
        for i in range(20):
            file_path = path + name + str(i) + '.jpg' 
            list_filePath.append(file_path)

    #下载图片
    n = 0
    for picurl in pic_list:
        res = requests.get(picurl)
        n = n + 1
        if res.status_code == 200:
            print("正在下载：%s"%list_filePath[n])
            #保存图片 wb 二进制形式写入11
            with open(list_filePath[n],'wb') as f:
                f.write(res.content)
getLOLImage()