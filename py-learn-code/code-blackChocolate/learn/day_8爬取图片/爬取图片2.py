import re
import requests
import json



def designName():
    url = 'http://www.uustv.com/'
    name = ''
    data = {
        'word':name,
        'sizes':60,
        'fonts':'jfcs.ttf',
        'fontcolor':'#000000'
    }
    #模拟浏览器向服务器发送请求
    #post 隐藏参数  get  不会隐藏参数，会将其展现出来
    result = requests.post(url,data=data)
    #设定编码
    result.encoding = 'utf-8'
    #获得页面内容
    html = result.text
    req1 = '<div class="tu">.*?<img src="(.*?)" /></div>'
    print(html)
    list_js = re.findall(req1,html)
    print(list_js)


designName()