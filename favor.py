#爬取p站首页的背景图  开始以为是定时请求后台，其实就是25张图，不知道多久换换 0.0

import urllib.request
import re
import json
import traceback
url="https://www.pixiv.net/"
i=25
path="C:/Users/Administrator/Pictures/收藏/p站/"
path2="/home/upsmart/task/2017.08/p/"
def get_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    # 发起请求
    result=urllib.request.urlopen(req)
    html=result.read().decode(encoding='utf-8',errors='strict')
    return html

def get_Url(data):
    t = data.find("init-config")
    n=re.search(r"id=\"init-config\"(.*)>$",data,re.M|re.I)
    o=re.search(r"'(.*)\'",n.group(),re.M|re.I)
    o=json.loads(eval(o.group()));
    landscape=o["pixivBackgroundSlideshow.illusts"]["landscape"]
    # return landscape[0]["url"]["1200x1200"]
    return landscape

def save(url,name):
	# 文件名字：landscape[j].illust_title
	# 作者：user_name
	# 600x600 ：url medium
	# 1200x1200 :url 1200x1200
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    req.add_header('Referer',"https://www.pixiv.net/")
    # urllib.request.urlretrieve(url,path+name+".jpg")
    response=urllib.request.urlopen(req).read()
    with open(path2+name, "wb") as file:
        try:
            file.write(response)
        except Exception as e:
            print("error")
            traceback.print_exc()
    return
def main(arrayObject):
    for obj in arrayObject:
        filename=obj["illust_title"]+"_"+obj["user_name"]+".jpg"
        url1=obj["url"]["1200x1200"]
        url2=obj["url"]["medium"]
        save(url1,filename)
    return

# 主程序运行
main(get_Url(get_html(url)))
